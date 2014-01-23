# Copyright (C) 2009  Eric C. Schug
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
'''
Provided Extended Wrapping of CLIPS objects to be more python like
Constructs are build using native Python types which are forwarded to
the CLIPS engine as needed. Automatic forwarding of changes in the python 
versions, however two way forwarding is limited do limitations of the CLIPS engine, 
so all changes must originate within python.
'''

#TODO: list of stuff
# * map id back to rule and call function
# * add wrapping of rule conditions
# * add wrapping to support COOL types
# * add wrappers to support misc functions
# * add wrappers to support globals
# * add wrappers to support instances


# standard imports
import types
import copy
import re

# extra imports
import clips
#from string import Template
if 0:
    #TODO: autogenerate script
    from Cheetah.Template import Template

    #define autocode templates for CLIPS
    clips_tmpl = Template.compile('''
    #def Module
    (defmodule $name (export ?ALL))

    #end def Module

    #def Rule
    (defrule $modulename::$name "blabla"
        $conditions
        =>    
        (python-call rule_autocallback $unique_id $rule_vars )
    ;    (printout t 'in $modulename::$name ' crlf )
        )

    #end def Rule

    #def Template
    (deftemplate $modulename::$name
        (slot unique_id (default-dynamic (gensym*)) )
    #for $slotname,$slot in $exportslots.iteritems()
        ($slot.slot_style $slotname  
    #if $slot.default!=None
            (default $slot.default)
    #end if
    #if $slot.clipstype!=None
            (type $slot.clipstype)
    #end if
            )
    #end for
        )

    #end def Template

    #def Fact
    (assert $name
    #for $name, $value in $slots
        ($name $value)
    #end for
        )
    #end def Fact
    ''')

def attribute_propdef(props, propdef):
    '''
    Simplifies declaration of properties or attributes and converts to dict of dicts
    @type props: list (or tuple) of (propname, default) tuples 
    @param props: list of allowed attributes for propdef, attribute order is important
    @param propdef: the propery definitions for the attributes
    propdef = 'x' # export attribute x
    propdef = 'x,y' # export attributes x and y
    propdef = {'x': 'str'} #export attribute x which is a string
    propdef = {'x':('str','value')} # and has a default value of 'value'
    propdef = {'x':('type':'str', 'default':'value')} # and bla, bla
    @rtype: dict of dicts
    '''
    #TODO: may need make a copy of propdef
    if(isinstance(propdef, types.StringTypes)):
        # if string split
        propdef = [item.strip() for item in propdef.split(',')]
    if(isinstance(propdef, (types.TupleType, types.ListType))):
        # if list convert to dict
        propdef = dict([(item, {}) for item in propdef])
    if(not isinstance(propdef, types.DictionaryType)):
        raise TypeError('Property definition must be a string or dictionary not a %s'
                         % type(propdef))
    npropdef={}
    for name, ipropvalues in propdef.iteritems():
        #if(isinstance(ipropvalues, types.StringTypes)):
        #    #don't see a need to parse string for this
        #    ipropvalues = (ipropvalues, )
        if(isinstance(ipropvalues, (types.TupleType, types.ListType))):
            #if list convert to dict
            prop_keys=[item[0] for item in props]
            ipropvalues = dict(zip(prop_keys[:len(ipropvalues)], ipropvalues))
        elif(not isinstance(ipropvalues, types.DictionaryType)):
            raise TypeError('Property definition for %s must be a string or dictionary not a %s'
                             % (name, type(ipropvalues)))
        else:
            a = set(propdef.keys()).difference(props)
            if(a):
                raise AttributeError('Property definition for %s contains one or more unknown properties %s' % (name, ', '.join(a)) )
        nprops=dict(props)
        nprops.update(ipropvalues)
        npropdef[name]=nprops
    #print npropdef
    return npropdef

def rule_autocallback(id, *matchargs):
    print 'executing rule_callback', id,  matchargs
    rule=Rule.rule_index(id)
    rule.function(*matchargs)
    #print rule

clips.RegisterPythonFunction(rule_callback, 'rule_autocallback')


    
class Rule(object):
    'CLIPS rule definition'
    _rules_list=[]
    @staticmethod
    def append_rule(rule):
        'append rule to internal list'
        Rule._rules_list.append(rule)
    @staticmethod
    def rule_id(rule):
        'get unique id for the rule'
        return Rule._rules_list.index(rule)
    @staticmethod
    def remove_rule(rule):
        'remove rule from internal list'
        Rule._rules_list.remove(rule)
    @staticmethod
    def rule_index(id):
        return Rule._rules_list[id]
    
    def __init__(self, name, conditions, function, rule_vars = None):
        Rule.append_rule(self)
        self.name = name
        self.conditions = conditions
        self.function = function
        if(rule_vars):
            self.rule_vars = rule_vars
        else:
            self.rule_vars = ' '.join( re.findall(r'(\?\w+)',self.conditions))
    def get_id(self):
        'Return a unique id for this rule'
        return Rule.rule_id(self)
    def clips_init(self, modulename):
        namespace={'modulename':modulename}
        self.unique_id=self.get_id()
        namespace.update(self.__dict__)
        #print namespace
        cheetah=clips_tmpl(namespaces=namespace)
        strdef=cheetah.Rule()
        return  strdef
    def __str__(self):
        return 'Rule %s %s %s' % (self.name, self.conditions, self.function)
        
class CLIPSobj(object):
    'Base Class for CLIPS Constructs'
    def module_by_name(self, name):
        return self.engine.get_module(name)
    def __init__(self, name=None):
        # name specified or inherited
        self.name = (name or self.__class__.__name__)
        #allow late binding of module
        self._module = None
        self._rules = {}
        self.engine = None
    
    #TODO: defrule = classmethod, staticmethod or instance
    def new_rule(self, name, conditions, function, rule_vars=None):
        ''' declare a CLIPS rule which executes a function when a set conditions
        are satisfied
        @param name: rule name for referencing
        @param conditions: rules activation conditions
        @param function: the python function to execute
        @type function: any python callable
        @param rule_args: rule variables to pass to function
        '''
        #allow rules to be define from any construct so that 
        #rules requiring then can be deleted when the construct is deleted
        #and making it more OO
        
        if(self.module):
            #TODO: check for overwrites of Rules
            pass
        self._rules[name] = Rule(name, conditions, function, rule_vars)

    def clips_init(self, modulename):
        'forwarding of definition to clips'
        #module = module_by_name(self.modulename)
        strdef=''
        for name, item in self._rules.iteritems():
            strdef+=item.clips_init(modulename)
        return strdef
    def get_module(self):
        'return module'
        return self._module
    def set_module(self, module):
        'set module to connect to'
        self._module = module
    module = property(get_module, set_module, doc='CLIPS module to bind to')
    def __del__(self):
        # delete rules
        pass

class BaseModule(CLIPSobj):
    modulename = '*'
    def __init__(self, name):
        CLIPSobj.__init__(self, name=name)
        self.name = name
        #self.code_tmpl = clipstemps['module']
        self._constructs=[]
    def __del__(self):
        CLIPSobj.__del__(self)
    def add_construct(self, construct):
        self._constructs.append(construct)
    def get_module(self):
        'return module (itself)'
        return self
    module = property(get_module, doc='override always return self')
    def clips_init(self):
        'forwarding of definition to clips'
        #return self.template(di)
        namespace={}
        namespace.update(self.__dict__)
        #print namespace
        cheetah=clips_tmpl(namespaces=namespace)
        strdef=cheetah.Module()
        strdef+='; Rules from %s\n\n' % self.name
        strdef+=CLIPSobj.clips_init(self, self.name)
        for item in self._constructs:
            strdef+=item.clips_init(self.name)
        return strdef
        #clips.Build('' % self.name)

clips_typemap={
               types.StringType:'STRING', 
               types.IntType:'INTEGER', 
               types.LongType:'INTEGER', 
               types.FloatType:'FLOAT', 
               }

class SlotDef:
    'Defines CLIPS Slot'
    def __init__(self, dictdef):
        self.slot_style='slot'
        for name, value in dictdef.iteritems():
            setattr(self, name, value)
        if(isinstance(self.type, (types.ListType, types.TupleType))):
            self.clipstype=[self.map_type(itype) for itype in self.type]
        else:
            self.clipstype=self.map_type(self.type)
    def map_type(self, typedef):
        if(clips_typemap.has_key(typedef)):
            return clips_typemap[typedef]
        elif(typedef == types.ListType):
            self.slot_style='multislot'
            return None
        else:
            return None

class BaseTemplate(CLIPSobj):
    '''
    Base class for wrapping CLIPS template
    Access Template slots via dictionary calls e.g. 
        print fact['slotname'] 
        fact['slotname'] = value
    exportslots = 'x' # export attribute x
    exportslots = 'x,y' # export attributes x and y
    exportslots = {'x': 'str'} #export attribute x which is a string
    exportslots = {'x':('str','value')} # and has a default value of 'value'
    exportslots = {'x':('type':'str', 'default':'value')} # and bla, bla
    '''
    exportslots = None
    
    def __init__(self, exportslots=None,  name=None):
        CLIPSobj.__init__(self, name=name)
        # exportslots specified or inherited
        #TODO: if specified as empty [] should be empty
        self.exportslots = (exportslots or self.exportslots or {})
        #verify slots definition and convert dict of dicts
        slot_props=(('type', types.NoneType),  ('default', None), ('constraint', None), ('doc', None))
        slotsdef = attribute_propdef(slot_props, self.exportslots)
        #print slotsdef
        self.exportslots=dict([(name, SlotDef(slot)) for name, slot in slotsdef.iteritems()])
        self.clips_id = None
        # slots are dict of self and not se
        #self._slots = {}
        #for name, islotdef in slotsdef.iteritems():
        #    if(callable(islotdef['default'])):
        #        #TODO: late binding of arguments
        #        value = islotdef['default']()
        #    else:
        #        value = islotdef['default']
        #    self[name] = value
        #for name, value in slots_init.iteritems():
        #    self[name] = value            
    def __del__(self):
        CLIPSobj.__del__(self)
    def __getitem__(self, name):
        'returns the slot by name'
        return self._slots[name]
    def __setitem__(self, name, value):
        'sets the slot by name'
        self._slots[name] = value
        if(self.clips_id != None):
            #notification to clips engine
            clips.SendCommand('(modify %s (%s %s) )' % (self.clips_id, name, value))
    def clips_init(self, modulename):
        'forwarding of definition to clips'
        namespace={'modulename':modulename}
        namespace.update(self.__dict__)
        #print namespace
        cheetah=clips_tmpl(namespaces=namespace)
        strdef=cheetah.Template()
        strdef+='; Rules from %s::%s\n\n' % (modulename, self.name)
        strdef+=CLIPSobj.clips_init(self, modulename)
        return strdef


class Engine(object):
    '''Stores Modules
    '''
    def __init__(self ):
        # should be one of
        #_engine = clips
        #_engine = clips.Environment()
        self._engine = clips
        self._modules = {}
    def add_module(self, module):
        self._modules[module.name] = module
    def new_module(self, name, props=None):
        mod=BaseModule(name)
        self._modules[name] = mod
        return mod
    def add_construct(self, construct, modulename='MAIN'):
        if(not isinstance(construct, CLIPSobj)):
            raise TypeError("construct must be a CLIPSobj not a %s" % type(construct))
        if(isinstance(construct, BaseModule)):
            self.add_module(construct)
        else:
            self._modules[modulename].add_construct(construct)
    def __get_item__(self, name):
        return self._modules[name]
    def remove_module(self, name):
        del self._modules[name]
    def clips_init(self):
        strdef=''
        #strdef+='(deffunction python-call (?name $?args) (printout t "python-call" ?name " " $?args crlf))\n\n'
        for name, mod in self._modules.iteritems():
            strdef+=mod.clips_init()
        return strdef
