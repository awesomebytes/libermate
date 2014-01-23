#
# CommandLine.py
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
__version__ = "0.1"
__copyright__ = "Copyright (c) 2009 Eric C. Schug"
__license__ = "GNU General Public License"
__revision__ = "$Id$"

import sys
import getopt

def descandarg(opt):
    'get description and arg name from a single opt'
    if(type(opt[3])==list):
        arg='TYPE'
    elif(opt[3]=='bool'):
        arg=''
    else:
        arg=opt[3].upper()
    desc = opt[2].replace('ARG',arg)
    return desc, arg

class App:
    usage_str='[options]'
    about_str=''
    def __init__(self, **kwargs):
         
        # Specify configuration options build an array of options defined as
        # [Name, shortkey, description, type, default]
        #type can be 'str','dir','file','bool','num', or a list of strings (enumeration)
        self.config_options=[
            ['help','h','display help and quit','bool',False],
            ['output','o','log output to file ARG','file','workit.log'],
            ['quite','','run silently hush all but prompts','bool',False],
        ]
        self.set_options(**kwargs)
    def ui(self):
        'Interactive user interface - future'
        raise NotImplementedError, 'ui is not yet available'


    def usage(self,config_options):
        'display command line usage extracted from config_options'
        usage_help='''usage: %s %s
%s

Allowable options are:''' % (sys.argv[0],self.usage_str,self.about_str)
        for opt in config_options:
            hline=' '
            desc, arg=descandarg(opt)
            if(opt[1]):
                hline += '-'+opt[1]+' '+arg+', '
            else:
                hline += ' '*5
            if(arg):
                hline += '--'+opt[0]+'='+arg
            else:
                hline += '--'+opt[0]
            if(arg):
                hline += ' \t\t(default='+str(opt[4])+')'
            else:
                hline += ' \t\t(default=off)'
            hline += '\n\t\t\t: '+desc
            if(type(opt[3])==list):
                hline=hline+', where TYPE can be one of ['+','.join(opt[3])+']'
            usage_help=usage_help+'\n'+hline
        print usage_help

    def command_line(self):
        'Handle command line parsing then call real main'
        # Parse config_options and create short and long options for getopt
        # and create argtable simplify argument checking
        shortopt=''
        longopt=[]
        argtable={}
        for opt in self.config_options:
            desc, arg=descandarg(opt)
            if(opt[1]):
                shortopt=shortopt+opt[1]
                argtable['-'+opt[1]]=opt
                if(arg):
                    shortopt=shortopt+':'
            argtable['--'+opt[0]]=opt
            if(arg):
                longopt.append(opt[0]+'=')
            else:
                longopt.append(opt[0])

        # Let getopt do its magic on the argv list
        try:
            opts, otherargs = getopt.getopt(sys.argv[1:], shortopt, longopt)
        except getopt.GetoptError, val:
            # print help information and exit:
            print "Error: improper command line usage"
            print val
            self.usage(self.config_options)
            sys.exit(2)

        #set option defaults
        cloptions={}
        for opt in self.config_options:
            cloptions[opt[0]]=opt[4]
        # interpret options from command line arguments
        for o, a in opts:
            if o in argtable:
                opt=argtable[o]
                if(opt[3]=='bool'):
                    arg=True
                elif(opt[3]=='num'):
                    arg=float(a)
                else:
                    arg=a
                cloptions[opt[0]]=arg
        # Check for help flag
        if(cloptions['help']):
            #print 'options specified :'
            #print cloptions
            self.usage(self.config_options)
            sys.exit()
        #check for interactive mode
        #if(interactive):
        #    ui()
        #run simulation main using options
        #main(cloptions)
        self.set_options(**cloptions)
        return otherargs

    def set_options(self, **kwargs):
        for name,value in kwargs.iteritems():
            setattr(self, name, value)

