#!/usr/bin/env python
#
# LiberMate
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

# Standard imports
import sys
import types


# Internal imports
import antlr
import MatlabParser

"""
block[ptoken] returns [sstr]
    self=write_node
    {
    sstr=""
    c=None
    self.ptoken=ptoken
    //print "in block", ptoken
    //self.tokenstack.append(_t)
    enter=_t
    if(_t and (_t.getType() not in [VAR,EXPR])):
        self.is_simple_rhs=False
    //if(_t):
    //    print "in block",_tokenNames[_t.getType()],_t.getText(),self.is_simple_rhs
    sys.stdout.flush()

    }
"""

class Mat2Py:
    'Translate MATLAB AST to Python AST'
    def __init__(self):
        mapfunc={}
        do_funcs=filter(lambda func: func.startswith('do_'), dir(self))
        for func in do_funcs:
            basefunc=func[3:]
            if(basefunc.isupper() and hasattr(MatlabParser, basefunc)):
                if(isinstance(getattr(MatlabParser, basefunc), types.IntType)):
                    mapfunc[getattr(MatlabParser, basefunc)]=getattr(self, func)
            elif hasattr(MatlabParser, 'LITERAL_'+basefunc):
                mapfunc[getattr(MatlabParser, 'LITERAL_'+basefunc)]=getattr(self, func)
        self.mapfunc=mapfunc
        self.returnval=""
        self.in_funcdef=False
        
    def script(self, node):
        self.translate(node)
        
    def  translate(self,nodes):
        self.returnval=""
        cc=[ self.write_node(child, "") for child in nodes]
        sstr="\n".join(cc)
        return sstr
        
    def write_node(self, node, ptoken=""):
        #print node.number, node.name
        func=self.mapfunc[node.number]
        return func(node, ptoken)
        
    def do_FUNCTION(self, node,  ptoken):
        'Handle FUNCTION node'
        self.incr()
        nodes=[ child.name for child in node.children ]
        cc=[ self.write_node(child, "") for child in node.children ]
        print node.children[1].name
        if('RETURN_VARS' in nodes ):
            index=nodes.index('RETURN_VARS')
            self.returnval=cc[index]
            del cc[index]
            del nodes[index]
        else:
            self.returnval=''
        if('FUNCTION_ARGS' in nodes):
            index=nodes.index('FUNCTION_ARGS')
            args=cc[index]
            del cc[index]
            del nodes[index]
        else:
            args=''
        if('NAME' in nodes):
            index=nodes.index('NAME')
            name=cc[index]
            del cc[index]
            del nodes[index]
        else:
            args=''
        k=self.nl+"# Local Variables: "+cc[0]+self.nl+self.nl.join(cc[1:])+self.nl+"return "+self.returnval
        self.decr()
        sstr=self.indent+"def "+name+args+":"+self.nl+k
        return sstr
        
    def do_FUNCTION_ARGS(self, node,  ptoken):
        'Handle FUNCTION_ARGS node'
        cc=[ self.write_node(child, "") for child in node.children ]
        sstr="("+", ".join(cc)+")"
        return sstr

    def do_RETURN_VARS(self, node, ptoken):
        'handle RETURN_VARS node'
        cc=[ self.write_node(child, "") for child in node.children ]
        sstr="["+", ".join(cc)+"]"
        return sstr

    def do_COMMENT(self, node, ptoken):
        'handle COMMENT node'
        sstr="#"+node.value
        return sstr

    def do_SCOPE(self, node, ptoken):
        'Handle SCOPE node'
        sstr=node.value
        return sstr
        
    def do_BLOCK(self, node, ptoken):
        cc=[ self.write_node(child, "") for child in node.children ]
        sstr=self.nl.join(cc)
        return sstr

    def do_if(self, node, ptoken):
        self.incr()
        a=self.write_node(node.children[0], "")
        b=self.write_node(node.children[1], "")
        self.decr()
        cc=[ self.write_node(child, "") for child in node.children[2:] ]
        sstr="if "+a+":"+self.nl+"    "+b+self.nl+self.nl.join(cc)+self.nl
        return sstr

    def do_elseif(self, node, ptoken):
        self.incr()
        a=self.write_node(node.children[0], "")
        cc=[ self.write_node(child, "") for child in node.children[1:] ]
        sstr="elif "+a+":"+self.nl+self.nl.join(cc)+self.nl
        self.decr()
        return sstr

    def do_else(self, node, ptoken):
        self.incr()
        #a=self.write_node(node.children[0], "")
        cc=[ self.write_node(child, "") for child in node.children ]
        sstr="else:"+self.nl+self.nl.join(cc)+self.nl
        self.decr()
        return sstr

    def do_for(self, node, ptoken):
        self.incr()
        a=self.write_node(node.children[0], "")
        b=self.write_node(node.children[1], "")
        c=self.write_node(node.children[2], "")
        #cc=[ self.write_node(child, "") for child in node.children[3:] ]
        sstr="for "+a+" in "+b+":"+self.nl+c+self.nl
        self.decr()
        return sstr

    def do_while(self, node, ptoken):
        self.incr()
        a=self.write_node(node.children[0], "")
        b=self.write_node(node.children[1], "")
        #cc=[ self.write_node(child, "") for child in node.children[2:] ]
        sstr="while "+a+":"+self.nl+b+self.nl
        self.decr()
        return sstr

    def do_try(self, node, ptoken):
        self.incr()
        a=self.write_node(node.children[0], "")
        b=self.write_node(node.children[1], "")
        #cc=[ self.write_node(child, "") for child in node.children[2:] ]
        sstr="try:"+self.nl+a
        self.decr()
        if(b):
            sstr+=self.nl+b
        sstr+=self.nl
        return sstr

    def do_catch(self, node, ptoken):
        self.incr()
        a=self.write_node(node.children[0], "")
        #cc=[ self.write_node(child, "") for child in node.children[1:] ]
        sstr="except :"+self.nl+a
        self.decr()
        return sstr

    def do_switch(self, node, ptoken):
        a=self.write_node(node.children[0], "")
        cc=[ self.write_node(child, "") for child in node.children[1:] ]
        sstr="_switch_val="+a+self.nl
        sstr+="if False: # switch "+self.nl+"    pass"+self.nl+ self.nl.join(cc)
        sstr+=self.nl
        return sstr

    def do_case(self, node, ptoken):
        self.incr()
        a=self.write_node(node.children[0], "")
        cc=[ self.write_node(child, "") for child in node.children[1:] ]
        sstr="elif _switch_val == "+a+":"+self.nl+self.nl.join(cc)
        self.decr()
        return sstr

    def do_otherwise(self, node, ptoken):
        self.incr()
        #a=self.write_node(node.children[0], "")
        cc=[ self.write_node(child, "") for child in node.children ]
        sstr="else:"+self.nl+self.nl.join(cc)
        self.decr()
        return sstr

    def do_ANDAND(self, node, ptoken):
        a=self.write_node(node.children[0], "and")
        b=self.write_node(node.children[1], "and")
        #cc=[ self.write_node(child, "") for child in node.children[2:] ]
        sstr=self.bop("and", a, b, ptoken, add_padding=True)
        return sstr

    def do_ASSIGN(self, node, ptoken):
        self.is_lhs=True
        a=self.write_node(node.children[0], "=")
        self.is_lhs=False
        self.is_simple_rhs=True
        if(len(node.children)>1):
            b=self.write_node(node.children[1], "=")
            sstr=self.bop("=", ptoken,  a, b, add_padding=True)
        else:
            sstr=a
        self.is_simple_rhs=False
        return sstr

    def do_LAMBDA(self, node, ptoken):
        a=self.write_node(node.children[0], "")
        b=self.write_node(node.children[1], "")
        sstr="lambda "+a+": "+b
        return sstr

    def do_ATPAREN(self, node, ptoken):
        #a=self.write_node(node.children[0], "")
        cc=[ self.write_node(child, ",") for child in node.children ]
        sstr=", ".join(cc)
        return sstr

    def do_BACKDIV(self, node, ptoken):
        a=self.write_node(node.children[0], ", ")
        b=self.write_node(node.children[1], ", ")
        sstr="linalg.solve("+a+", "+b+")"
        return sstr

    def do_COLON(self, node, ptoken):
        cc=[ self.write_node(child, "") for child in node.children ]
        sstr=self.colonop(ptoken, cc)
        return sstr

    def do_COMMA(self, node, ptoken):
        cc=[ self.write_node(child, ",") for child in node.children ]
        sstr=self.multiop(", ", ptoken,  cc)
        return sstr

    def do_DOT(self, node, ptoken):
        a=self.write_node(node.children[0], ".")
        b=self.write_node(node.children[1], ".")
        sstr=self.bop(".", ptoken,  a, b)
        return sstr

#    def do_LOGICAL_NOT(self, node, ptoken):
#        a=self.write_node(node.children[0], "")
#        cc=[ self.write_node(child, "") for child in node.children[1:] ]
#        return sstr
#    a=block["not"]) {sstr=self.preop("not ", a)}
#        a=self.write_node(node.children[0], "")
#        cc=[ self.write_node(child, "") for child in node.children[1:] ]
#        return sstr

    def do_NOT(self, node, ptoken):
        a=self.write_node(node.children[0], "not")
        sstr=self.preop("not", ptoken,  a, add_padding=True)
        return sstr

    def do_SIGN_PLUS(self, node, ptoken):
        a=self.write_node(node.children[0], " +")
        sstr=self.preop(" +", ptoken,  a)
        return sstr

    def do_SIGN_MINUS(self, node, ptoken):
        a=self.write_node(node.children[0], " -")
        sstr=self.preop(" -", ptoken,  a)
        return sstr

    def do_DOTDIV(self, node, ptoken):
        a=self.write_node(node.children[0], "/")
        b=self.write_node(node.children[1], "/")
        sstr=self.bop("/", ptoken,  a, b)
        return sstr

    def do_DOTEXP(self, node, ptoken):
        a=self.write_node(node.children[0], "**")
        b=self.write_node(node.children[1], "**")
        sstr=self.bop("**", ptoken,  a, b)
        return sstr

    def do_DOTSTAR(self, node, ptoken):
        a=self.write_node(node.children[0], "*")
        b=self.write_node(node.children[1], "*")
        sstr=self.bop("*", ptoken,  a, b)
        return sstr

    def do_MINUS(self, node, ptoken):
        a=self.write_node(node.children[0], "-")
        b=self.write_node(node.children[1], "-")
        sstr=self.bop("-", ptoken,  a, b)
        return sstr

    def do_PLUS(self, node, ptoken):
        a=self.write_node(node.children[0], "+")
        b=self.write_node(node.children[1], "+")
        sstr=self.bop("+", ptoken,  a, b)
        return sstr

    def do_EQUAL(self, node, ptoken):
        a=self.write_node(node.children[0], "==")
        b=self.write_node(node.children[1], "==")
        sstr=self.bop("==", ptoken,  a, b, add_padding=True)
        return sstr

    def do_NOT_EQUAL(self, node, ptoken):
        a=self.write_node(node.children[0], "!=")
        b=self.write_node(node.children[1], "!=")
        sstr=self.bop("!=", ptoken,  a, b, add_padding=True)
        return sstr

    def do_GREATER_THAN(self, node, ptoken):
        a=self.write_node(node.children[0], ">")
        b=self.write_node(node.children[1], ">")
        sstr=self.bop(">", ptoken,  a, b, add_padding=True)
        return sstr

    def do_GREATER_OR_EQUAL(self, node, ptoken):
        a=self.write_node(node.children[0], ">=")
        b=self.write_node(node.children[1], ">=")
        sstr=self.bop(">=", ptoken,  a, b, add_padding=True)
        return sstr

    def do_LESS_OR_EQUAL(self, node, ptoken):
        a=self.write_node(node.children[0], "<=")
        b=self.write_node(node.children[1], "<=")
        sstr=self.bop("<=", ptoken,  a, b)
        return sstr

    def do_LESS_THAN(self, node, ptoken):
        a=self.write_node(node.children[0], "<")
        b=self.write_node(node.children[1], "<")
        sstr=self.bop("<", ptoken,  a, b)
        return sstr

    def do_OROR(self, node, ptoken):
        a=self.write_node(node.children[0], "or")
        b=self.write_node(node.children[1], "or")
        sstr=self.bop("or", ptoken,  a, b, add_padding=True)
        return sstr

    def do_LPAREN(self, node, ptoken):
        cc=[ self.write_node(child, "") for child in node.children ]
        sstr="("+", ".join(cc)+")"
        return sstr

    def do_BRACE_ARGS(self, node, ptoken):
        pin_var=self.in_var
        if(node.children[0].name=='VAR'):
            self.in_var=True
        else:
            self.in_var=False
        a=self.write_node(node.children[0], "x(")
        cc=[ self.write_node(child, "x(") for child in node.children[1:] ]
        sstr=a+self.join_args(cc,True, ptoken=ptoken)
        self.in_var=pin_var
        return sstr

    def do_PAREN_ARGS(self, node, ptoken):
        pin_var=self.in_var
        if(node.children[0].name=='VAR'):
            self.in_var=True
        else:
            self.in_var=False
        a=self.write_node(node.children[0], "x(")
            
        cc=[ self.write_node(child, "x(") for child in node.children[1:] ]
        sstr=a+self.join_args(cc, ptoken=ptoken)
        self.in_var=pin_var
        return sstr

    def do_LBRACE(self, node, ptoken):
        'LHS Assign'
        cc=[ self.write_node(child, ",") for child in node.children ]
        sstr=self.join_args(cc, True)
        return sstr

    def do_MATRIX(self, node, ptoken):
        'Construct Matrix Node'
        cc=[ self.write_node(child, ",") for child in node.children ]
        if(cc):
            sstr="np.array("+", ".join(cc)+")" 
        else:
            sstr="np.array([])"
        return sstr

    def do_CELL(self, node, ptoken):
        'Construct Cell Array Node'
        cc=[ self.write_node(child, ",") for child in node.children]
        if(cc):
            sstr="cellarray("+", ".join(cc)+")" 
        else:
            sstr="cellarray([])"
        return sstr

    def do_EXPR(self, node, ptoken):
        cc=[ self.write_node(child, ",") for child in node.children ]
        sstr=", ".join(cc)
        return sstr

    def do_ROWJOIN(self, node, ptoken):
        'Join Rows of matrix / cell array'
        cc=[ self.write_node(child, ",") for child in node.children ]
        # alternative form
        #sstr="r_["+", ".join(cc)+"]"
        sstr="np.vstack(("+", ".join(cc)+"))"
        return sstr

    def do_COLUMNJOIN(self, node, ptoken):
        'Join Columns of matrix / cell array'
        cc=[ self.write_node(child, ",") for child in node.children ]
        # alternative form
        #sstr="c_["+", ".join(cc)+"]"
        sstr="np.hstack(("+", ".join(cc)+"))"
        return sstr

    def do_AND(self, node, ptoken):
        'Logical And'
        a=self.write_node(node.children[0], ",")
        b=self.write_node(node.children[1], ",")
        sstr="np.logical_and("+a+", "+b+")"
        return sstr

    def do_OR(self, node, ptoken):
        'Logical Or'
        a=self.write_node(node.children[0], ",")
        b=self.write_node(node.children[1], ",")
        sstr="np.logical_or("+a+", "+b+")"
        return sstr

    def do_STAR(self, node, ptoken):
        'Matrix Mult'
        a=self.write_node(node.children[0], ",")
        b=self.write_node(node.children[1], ",")
        sstr="np.dot("+a+", "+b+")"
        return sstr

    def do_DIV(self, node, ptoken):
        'Matrix Division'
        a=self.write_node(node.children[0], ",")
        b=self.write_node(node.children[1], ",")
        sstr="matdiv("+a+", "+b+")"
        return sstr

    def do_DOTBACKDIV(self, node, ptoken):
        'Element wise back division'
        a=self.write_node(node.children[0], ",")
        b=self.write_node(node.children[1], ",")
        sstr="matbackdiv("+a+", "+b+")"
        return sstr

    def do_EXP(self, node, ptoken):
        'Matrix Power'
        a=self.write_node(node.children[0], ",")
        b=self.write_node(node.children[1], ",")
        sstr="matixpower("+a+", "+b+")"
        return sstr

    def do_AT(self, node, ptoken):
        a=self.write_node(node.children[0], "")
        sstr=a
        return sstr

    def do_BREAK(self, node, ptoken):
        sstr="break"
        return sstr

    def do_CONT(self, node, ptoken):
        sstr="continue"
        return sstr

    def do_RETURN(self, node, ptoken):
        sstr="return ["+self.returnval+"]"
        return sstr

    def do_ARRAY_END(self, node, ptoken):
        'Last Element of Array'
        sstr="xend"
        #sstr="0"
        return sstr

    def do_ALLELEMENTS(self, node, ptoken):
        sstr=":"
        return sstr

    def do_TRANS(self, node, ptoken):
        'Conj Transpose'
        a=self.write_node(node.children[0], ".")
        sstr=a+".conj().T"
        return sstr

    def do_DOTTRANS(self, node, ptoken):
        'Simple Transpose'
        a=self.write_node(node.children[0], ".")
        sstr=a+".T"
        return sstr

    def do_COMMAND(self, node, ptoken):
        cc=[ self.write_node(child, "NAME") for child in node.children ]
        sstr=self.Lookup(node.value)+"("+"".join(cc)+")"
        return sstr

    def do_NAME(self, node, ptoken):
        'Non variable label'
        self.nargin=0
        cc=[ self.write_node(child, "NAME") for child in node.children ]
        if(cc):
            sstr=self.Lookup(node.value)+"".join(cc)
        else:
            sstr=self.Lookup(node.value)
        return sstr

    def do_NEWLINE(self, node, ptoken):
        sstr=node.value
        return sstr


    def do_NUMBER(self, node, ptoken):
        sstr=node.value
        return sstr

    def do_INT(self, node, ptoken):
        # In Matlab everything is a matrix 
        sstr=node.value #+"."
        return sstr

    def do_FLOAT(self, node, ptoken):
        sstr=node.value
        return sstr

    def do_COMPLEX(self, node, ptoken):
        sstr=node.value
        return sstr

    def do_RBRACK(self, node, ptoken):
        sstr=""
        return sstr

    def do_LBRACK(self, node, ptoken):
        cc=[ self.write_node(child, "") for child in node.children ]
        sstr="["+", ".join(cc)+"]"
        return sstr

    def do_RPAREN(self, node, ptoken):
        sstr=""
        return sstr

    def do_STRING(self, node, ptoken):
        #convert to python string
        sstr=node.value.replace("''",r"\'")
        return sstr

    def do_VAR(self, node, ptoken):
        'Variable label'
        pin_var=self.in_var
        self.in_var=True
        cc=[ self.write_node(child, "VAR") for child in node.children ]
        if(cc):
            sstr=(node.value)+"".join(cc)
        else:
            sstr=(node.value)
            #if(self.is_simple_rhs):
            #    sstr+="copy("+sstr+")"
        self.in_var=pin_var
        return sstr
#    ;
'''
funcargs returns [sstr]
    {
     sstr=""
     cc=[]
    //print "in funcargs"
    }
    : #(LPAREN (a:VAR {cc.append(a.getText())})* ) {sstr="("+", ".join(cc)+")" }
    // | b:COMMENT {sstr="#"+b.getText()+"\n"} complains
    ;
'''
