#!/usr/bin/env python
#
# LiberMate - BaseRules
#
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

__author__ = "Eric C. Schug (schugschug@gmail.com)"
__copyright__ = "Copyright (c) 2009 Eric C. Schug"
__license__ = "GNU General Public License"
__revision__ = "$Id$"

import sys
import traceback

# External imports
import clips

#import RuleEngine
import MatlabParser

class Match:
    pass
class Any(Match):
    pass
class All(Match):
    pass
class OnePlus(Match):
    pass
class ZeroPlus(Match):
    pass

class BaseAST:
    def __init__():
        pass
    def append(self, tag):
        pass
    def match(self, name=None, text=None, attrs={}, children=Any):
        pass

astcount=0
def gensym_ast():
    global astcount
    astcount+=1
    return 'ast%d' % astcount

'''
class ASTTemplate(RuleEngine.BaseTemplate):
    'Defines the CLIPS Template for ASTNode'
    exportslots = {
        'is_matrix':(types.BoolType, False), 
        'is_scalar':(types.BoolType, False), 
        'is_lhs':(types.BoolType, False), 
        'is_rhs': (types.BoolType, False), 
        'id':  (types.ListType, ), 
        'name':  (types.ListType, ), 
        'value':  (types.StringType, ), 
        'children':  (types.ListType, ), 
        }
'''
_fact_lookup={}

class ASTNode(object):
    misc_flags=['is_matrix', 'is_scalar', 'is_lhs', 'is_rhs']
    def __init__(self, number, value, children=[], id=None):
        self._id=id or gensym_ast()
        _fact_lookup[self._id]=self
        self._fact=None
        self.flags=dict([(flag, False) for flag in self.misc_flags])
        self.number=number
        self.value=value
        self.children=children
    def __del__(self):
        #self.retract()
        pass
    def to_list(self):
        return [self.name,  self.value,  [child.to_list() for child in self.children]]
    def set_flag(self, flag, value):
        self.flags[flag]=value
        if(self._fact):
            sstr='(bind ?*ans* (modify %d (%s %s)) )' % (self._fact, flag, value)
            clips.SendCommand(sstr)
            self._fact=clips.Eval('?*ans*').Index
    def get_flag(self, flag, value):
        return self.flags[flag]
    def assert_all(self):
        for child in self.children:
            child.assert_all()
        self.assert_this()
    def assert_this(self):
        #TODO: Convert value to CLIPS string
        value='"'+self.value+'"'
        other_props=[  "(%s %s)" % (flag, str(value).upper()) for flag, value in self.flags.iteritems() ]
        if(self.children):
            child_ids=[str(child._id) for child in self.children]
            fstr='(ASTTemplate (id %s) (name %s) (value %s) %s (children %s) )' % (
                                                                        self._id, 
                                                                        self.name, 
                                                                        value, 
                                                                        " ".join(other_props), 
                                                                        " ".join(child_ids))
        else:
            fstr='(ASTTemplate (id %s) (name %s) (value %s) %s)' % (
                                                                        self._id, 
                                                                        self.name, 
                                                                        value, 
                                                                        " ".join(other_props), 
                                                                        )
        #print fstr
        self._fact=clips.Assert(fstr).Index
        _fact_lookup[self._fact]=self
    def modify(self, **kwargs):
        for kw, value in kwargs.iteritems():
            if(kw=='name'):
                self.name=value
            elif(kw=='value'):
                self.value=value
            elif(kw=='children'):
                self.children=value
            elif(kw in self.flags):
                self.set_flag(kw, value)
    def retract_all(self):
        self.retract()
        for child in self.children:
            child.retract()
    def retract(self):
        if(self._fact):
            clips.Call('retract', self._fact)
            del _fact_lookup[self._fact]
        self._fact=None
    def get_name(self):
        return MatlabParser._tokenNames[self._number]
    def set_name(self, name):
        number=MatlabParser._tokenNames.index(name)
        self.number=number
    name = property(get_name, set_name)
    
    def get_number(self):
        return self._number
    def set_number(self, number):
        self._number=number
        if(number in [MatlabParser.INT,  MatlabParser.FLOAT,  MatlabParser.NUMBER]):
            self.set_flag('is_scalar', True)
        if(self._fact):
            sstr='(bind ?*ans* (modify %d (name %s)) )' % (self._fact, self.name)
            clips.SendCommand(sstr)
            self._fact=clips.Eval('?*ans*').Index
    number = property(get_number, set_number)
    
    def get_value(self):
        return self._value
    def set_value(self, value):
        self._value=value        
        if(self._fact):
            sstr='(bind ?*ans* (modify %d (name %s)) )' % (self._fact, self.value)
            clips.SendCommand(sstr)
            self._fact=clips.Eval('?*ans*').Index
    value = property(get_value, set_value)

    def get_children(self):
        return self._children
    def set_children(self, children):
        self._children=children
        if(self._fact):
            child_ids=[str(child._id) for child in self.children]
            sstr='(bind ?*ans* (modify %d (children %s)) )' % (self._fact, ' '.join(self.child_ids))
            clips.SendCommand(sstr)
            self._fact=clips.Eval('?*ans*').Index
    children = property(get_children, set_children)

def passs():
            #Simple conversions
            s=re.sub(r'pi\(\)','pi',s)
            s=re.sub(r'Inf\(\)','inf',s)
            s=re.sub(r'nan\(\)','nan',s)
            s=re.sub(r'int\(([\d]+)\.\)',r'\1',s)
            def sub_eval(m):
                return str(eval(m.group(1)))
            s=re.sub(r"random.rand\('state', ", "random.set_state(",s)
            #s=re.sub(r"random.rand\(\), ", "random.set_state(",s)
            s=re.sub(r'([\d]+\.?-1)',sub_eval,s)
            s=re.sub(r'matdiv\((.+?),\ (\d+.)\)',r'(\1)/\2',s)
            s=re.sub(r'matdiv\((\d+.),\ ',r'\1/(',s)
            s=re.sub(r'dot\((.+?),\ (\d+.)\)',r'(\1)*\2',s)
            s=re.sub(r'dot\((\d+.),\ ',r'\1*(',s)
            s=re.sub(r'shape\.Error\(([\w\.]+),\ ([\w\.]+)\)',r'\1.shape[\2-1]',s)
            s=re.sub(r'shape\.Error\((\w+)\)',r'\1.shape',s)
            s=re.sub(r'\.flatten\(1\)\.conj\(\)\.T',r'.flatten(0).conj()',s)
            s=re.sub(r'\.flatten\(1\)\.T',r'.flatten(0)',s)
            s=re.sub(r'\.flatten\(1\)\.T',r'.flatten(0)',s)


_rules_dict={}
def rule_callback(id, *matchargs):
    global _rules_dict
    #print 'executing rule_callback', id,  matchargs
    try:
        id=str(id)
        func=_rules_dict[id]
        def to_native(arg):
            if(isinstance(arg, clips.Fact)):
                #arg.PPrint()
                fact=arg.Slots['id']
                arg=_fact_lookup[fact]
            return arg
        new_args=[to_native(arg) for arg in matchargs]
                
        func(*new_args)
    except:
        #traceback.print_last()
        print "Exception in user code:"
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60
        pass
    #print rule
print rule_callback
clips.RegisterPythonFunction(rule_callback, 'rule_callback')

def connect_rules(inst):
    global _rules_dict
    rule_funcs=filter(lambda attr: attr.startswith('rule_'), dir(inst))
    class_name=inst.__class__.__name__
    maprule=dict([(class_name+'-'+func[5:],  getattr(inst, func)) for func in rule_funcs])
    _rules_dict.update(maprule)

class BaseRules:
    'Base Rules for '
    def __init__(self):
        connect_rules(self)
        #mod=self.new_module('MAIN')
        #print (eng.clips_init())
        
        
        clips.Clear()
        clips.Load('astrules.clp')
        clips.Reset()
    def run(self):
        clips.Run()
    #rules
    def rule_simple_scalar(self, node):
        '?node <- (ASTTemplate (name INT|FLOAT|NUMBER) (is_scalar FALSE) )'
        node.modify(is_scalar=True)
    # 
    def rule_assign_lhs_rhs(self, node):
        '?node <- (ASTTemplate (name ASSIGN) )'
        node.children[0].modify(is_lhs=True, recursive=True)
        node.children[1].modify(is_rhs=True, recursive=True)
    
    def rule_map_rand_state(self, node, child):
        """
        ?node <- (ASTTemplate (id ?x) (name NAME) (value "rand") )
        ?child <- (ASTTemplate  (children ?x ?y $?) (name PAREN_ARGS))
        (ASTTemplate (id ?y) (value "'state'"))
        """
        # set function to random.set_state and delete state argument
        node.value="random.set_state"
        del child.children[0]

    def rule_int_as_float(self, node):
        ''''
        ?node <- (ASTTemplate (name INT) )
        '''
        
        node.modify(name='FLOAT', value=node.value+'.')
    
    def rule_length_to_shape(self, node,  a):
        '''
        length(?a) -> ?a.shape[-1]
        
        (ASTTemplate (id ?x) (name NAME) (value "'length'") )
        ?node <- (ASTTemplate (name PAREN_ARGS) (children ?x ?y) )
        ?a <- (ASTTemplate (id ?y) )
        '''
        node.modify(name='FLOAT', value=node.value+'.')
        mone=ASTNode(MatlabParser.INT, "-1")
        shape=ASTNode(MatlabParser.NAME, "'shape'")
        brack=ASTNode(MatlabParser.PAREN_ARGS, "'shape'", [shape, mone])
        brack.assert_all()
        node.name='DOT'
        node.value='.'
        node.childrent=[a, brack]

    def xrule_zeros_ones(self, node, a):
        '''
        zeros(?a,?b) -> np.zeros((?a,?b))
        
        ?node <- (ASTTemplate (name NAME) (value "length"|"ones")  (children ?x) )
        (ASTTemplate (id ?x) (name LPAREN) (children ?y ?z))
        ?a <- (ASTTemplate (id ?y) )
        ?b <- (ASTTemplate (id ?z) )
        '''
        #node.modify(name='FLOAT', value=node.value+'.')
    def rule_scalar_mult_div_exp(self, node, a,  b):
        '''
        ?a*?b -> ?a.*?b :  ?a.is_scalar or ?b.is_scalar

        ?node <- (ASTTemplate (name STAR|EXP|DIV) (children ?x ?y) )
        ?a <- (ASTTemplate (id ?x) )
        ?b <- (ASTTemplate (id ?y) )
        '''
        if(a.name=='INT' or b.name=='INT'):
            if(node.name=='STAR'):
                node.name='DOTSTAR'
            elif(node.name=='DIV'):
                node.name='DOTDIV'
            elif(node.name=='EXP'):
                node.name='DOTEXP'

'''
length(?a) -> ?a.shape[-1]

zeros(?a,?b) -> np.zeros((?a,?b))
ones(?a,?b) -> np.ones((?a,?b))
?a/?b -> matdiv(?a,?b)
?a*?b -> np.dot(?a,?b) :  not ?a.is_scalar and not ?b.is_scalar
size(?a,?b) -> ?a.shape[?b-1] :
ndims(?a) -> ?a.ndim 
eps -> finfo(float).eps
i -> 1j
find(?a) -> np.nonzero(?a)+1
rand -> np.random.rand
meshgrid(?a,?b) -> meshgrid[?a,?b]
repmat(?a,?m,?n) -> tile(?a,(?m,?n))
max(max(?a)) -> ?a.max()
max(?a) -> ?a.max(0)
max(?a,[],2) -> ?a.max(1)
max(?a,?b)  -> np.maximum(?a,?b)
min(max(?a)) -> ?a.min()
min(?a) -> ?a.min(0)
min(?a,[],2) -> a.min(1)
min(?a,?b)  -> minimum(?a,?b)

error -> matcompat.error 
warning -> matcompat.warning 
norm -> np.linalg.norm
bitand(?a,?b) -> ?a & ?b
bitor(?a,?b) -> ?a | ?b
inv -> np.linalg.inv
pinv -> np.linalg.pinv
chol -> np.linalg.cholesky
eig -> np.linalg.eig
qr -> scipy.linalg.qr
lu -> scipy.linalg.lu
conjgrad -> scipy.linalg.cg
regress(?a,?b) -> np.linalg.lstsq(?b, ?a)
decimate -> matcompat.decimate

'''
