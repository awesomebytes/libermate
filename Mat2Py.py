### $ANTLR 2.7.6 (20071205): "mat2py.g" -> "Mat2Py.py"$
### import antlr and other modules ..
import sys
import antlr

version = sys.version.split()[0]
if version < '2.2.1':
    False = 0
if version < '2.3':
    True = not False
### header action >>> 
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
# along with this program.  If not, see <http:#www.gnu.org/licenses/>.
#

__author__ = "Eric C. Schug (schugschug@gmail.com)"
__copyright__ = "Copyright (c) 2009 Eric C. Schug"
__license__ = "GNU General Public License"
__revision__ = "$Id$"
   
import traceback
### header action <<< 

### import antlr.Token 
from antlr import Token
### >>>The Known Token Types <<<
SKIP                = antlr.SKIP
INVALID_TYPE        = antlr.INVALID_TYPE
EOF_TYPE            = antlr.EOF_TYPE
EOF                 = antlr.EOF
NULL_TREE_LOOKAHEAD = antlr.NULL_TREE_LOOKAHEAD
MIN_USER_TYPE       = antlr.MIN_USER_TYPE
EXPR = 4
DECL = 5
FUNCTION = 6
IFBLOCK = 7
BLOCK = 8
BCOLON = 9
SIGN_PLUS = 10
SIGN_MINUS = 11
VAR = 12
SCOPE = 13
DOT = 14
ARGUMENTS = 15
CONTINUATION = 16
END = 17
ARRAY_END = 18
BREAK = 19
CONT = 20
RETURN = 21
RETURN_VARS = 22
COMMAND = 23
LAMBDA = 24
ALLELEMENTS = 25
TRANS = 26
CELL = 27
MATRIX = 28
COLUMN_JOIN = 29
ROW_JOIN = 30
FLOAT = 31
COMPLEX = 32
ASSERT = 33
GLOBAL = 34
FUNCTION_ARGS = 35
BRACE_ARGS = 36
PAREN_ARGS = 37
SPACE = 38
COMMENT = 39
NEWLINE = 40
LITERAL_function = 41
LBRACK = 42
NAME = 43
COMMA = 44
RBRACK = 45
ASSIGN = 46
LPAREN = 47
RPAREN = 48
LITERAL_if = 49
LITERAL_while = 50
LITERAL_for = 51
LITERAL_try = 52
LITERAL_switch = 53
LITERAL_catch = 54
LITERAL_case = 55
LITERAL_elseif = 56
LITERAL_otherwise = 57
LITERAL_else = 58
SEMI = 59
LBRACE = 60
RBRACE = 61
COLON = 62
ATPAREN = 63
OROR = 64
ANDAND = 65
OR = 66
AND = 67
EQUAL = 68
NOT_EQUAL = 69
LESS_THAN = 70
LESS_OR_EQUAL = 71
GREATER_THAN = 72
GREATER_OR_EQUAL = 73
PLUS = 74
MINUS = 75
STAR = 76
DIV = 77
BACKDIV = 78
DOTSTAR = 79
DOTDIV = 80
DOTBACKDIV = 81
NOT = 82
EXP = 83
DOTEXP = 84
AT = 85
DOTTRANS = 86
NUMBER = 87
INT = 88
MATCHVAR = 89
STRING = 90
Exponent = 91
MATCH = 92
DIGIT = 93
ROWJOIN = 94
COLUMNJOIN = 95

### user code>>>

### user code<<<

class Walker(antlr.TreeParser):
    
    # ctor ..
    def __init__(self, *args, **kwargs):
        antlr.TreeParser.__init__(self, *args, **kwargs)
        self.tokenNames = _tokenNames
        ### __init__ header action >>> 
        # gets inserted in the __init__ method of each of the generated Python
        # classes
        #
        self.paren_count=0
        self.brack_count=0
        self.string_ok=True
        self.gobble_space=True
        ### __init__ header action <<< 
    
    ### user action >>>
    ### user action <<<
    def script(self, _t):    
        sstr = None
        
        script_AST_in = None
        if _t != antlr.ASTNULL:
            script_AST_in = _t
        sstr=""
        #print "in script"
        cc=[]
        xx=""
        ax=""
        try:      ## for error handling
            if not _t:
                _t = antlr.ASTNULL
            if (_t.getType()==FUNCTION):
                pass
                _cnt309= 0
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_t.getType()==FUNCTION):
                        pass
                        g=self.function(_t)
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                    _cnt309 += 1
                if _cnt309 < 1:
                    raise antlr.NoViableAltException(_t)
                sstr+="\n\n".join(cc)
            elif (_t.getType()==COMMENT):
                pass
                ax=self.comment(_t)
                _t = self._retTree
                b=self.script(_t)
                _t = self._retTree
                sstr=ax+b
            elif (_tokenSet_0.member(_t.getType())):
                pass
                h=self.block(_t, "")
                _t = self._retTree
                sstr+=h
            else:
                raise antlr.NoViableAltException(_t)
            
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return sstr
    
    def function(self, _t):    
        sstr = None
        
        function_AST_in = None
        if _t != antlr.ASTNULL:
            function_AST_in = _t
        e = None
        b = None
        sstr=""
        #print "in function"
        cc=[]
        xx=""
        ax=""
        self.returnval=""
        try:      ## for error handling
            pass
            _t311 = _t
            tmp1_AST_in = _t
            self.match(_t,FUNCTION)
            _t = _t.getFirstChild()
            self.incr()
            e = _t
            self.match(_t,SCOPE)
            _t = _t.getNextSibling()
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [RETURN_VARS]:
                pass
                a=self.funcreturn(_t)
                _t = self._retTree
                self.returnval=a
            elif la1 and la1 in [NAME]:
                pass
            else:
                    raise antlr.NoViableAltException(_t)
                
            b = _t
            self.match(_t,NAME)
            _t = _t.getNextSibling()
            c=self.funcargs(_t)
            _t = self._retTree
            d=self.block(_t, "")
            _t = self._retTree
            _t = _t311
            _t = _t.getNextSibling()
            k=self.nl+"# Local Variables: "+e.getText()+self.nl+d+self.nl+"return ["+self.returnval+"]"
            self.decr()
            sstr=self.indent+"def "+b.getText()+c+":"+self.nl+k
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return sstr
    
    def comment(self, _t):    
        sstr = None
        
        comment_AST_in = None
        if _t != antlr.ASTNULL:
            comment_AST_in = _t
        a = None
        sstr=""
        #print "in comment"
        cc=[]
        try:      ## for error handling
            pass
            _cnt315= 0
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==COMMENT):
                    pass
                    a = _t
                    self.match(_t,COMMENT)
                    _t = _t.getNextSibling()
                    cc.append("#"+a.getText())
                else:
                    break
                
                _cnt315 += 1
            if _cnt315 < 1:
                raise antlr.NoViableAltException(_t)
            sstr=self.nl.join(cc)+self.nl
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return sstr
    
    def block(self, _t,
        ptoken
    ):    
        sstr = None
        
        block_AST_in = None
        if _t != antlr.ASTNULL:
            block_AST_in = _t
        q = None
        i = None
        j = None
        k = None
        u = None
        v = None
        w = None
        m = None
        p = None
        r = None
        sstr=""
        cc=[]
        c=None
        self.ptoken=ptoken
        #print "in block", ptoken
        #self.tokenstack.append(_t)
        enter=_t
        if(_t and (_t.getType() not in [VAR,EXPR])):
           self.is_simple_rhs=False
        #if(_t):
        #    print "in block",_tokenNames[_t.getType()],_t.getText(),self.is_simple_rhs
        sys.stdout.flush()
        try:      ## for error handling
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [BLOCK]:
                pass
                _t321 = _t
                tmp2_AST_in = _t
                self.match(_t,BLOCK)
                _t = _t.getFirstChild()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, ptoken)
                        _t = self._retTree
                        if(g): cc.append(g)
                    else:
                        break
                    
                _t = _t321
                _t = _t.getNextSibling()
                #print "block join ~"+self.indent+"~block",len(self.nl), len(cc)
                sstr=self.nl.join(cc) 
                #print sstr
            elif la1 and la1 in [LITERAL_if]:
                pass
                _t324 = _t
                tmp3_AST_in = _t
                self.match(_t,LITERAL_if)
                _t = _t.getFirstChild()
                self.incr()
                a=self.block(_t, "")
                _t = self._retTree
                b=self.block(_t, "")
                _t = self._retTree
                self.decr()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, "")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t324
                _t = _t.getNextSibling()
                #print "if"
                sstr="if "+a+":"+self.nl+"    "+b+self.nl+self.nl.join(cc)+self.nl
            elif la1 and la1 in [LITERAL_elseif]:
                pass
                _t327 = _t
                tmp4_AST_in = _t
                self.match(_t,LITERAL_elseif)
                _t = _t.getFirstChild()
                self.incr()
                aexpr=self.block(_t, "")
                _t = self._retTree
                if not _t:
                    _t = antlr.ASTNULL
                la1 = _t.getType()
                if False:
                    pass
                elif la1 and la1 in [EXPR,BLOCK,SIGN_PLUS,SIGN_MINUS,VAR,DOT,ARGUMENTS,ARRAY_END,BREAK,CONT,RETURN,COMMAND,LAMBDA,ALLELEMENTS,TRANS,CELL,MATRIX,FLOAT,COMPLEX,COMMENT,NEWLINE,LBRACK,NAME,COMMA,RBRACK,ASSIGN,LPAREN,RPAREN,LITERAL_if,LITERAL_while,LITERAL_for,LITERAL_try,LITERAL_switch,LITERAL_catch,LITERAL_case,LITERAL_elseif,LITERAL_otherwise,LITERAL_else,LBRACE,COLON,ATPAREN,OROR,ANDAND,OR,AND,EQUAL,NOT_EQUAL,LESS_THAN,LESS_OR_EQUAL,GREATER_THAN,GREATER_OR_EQUAL,PLUS,MINUS,STAR,DIV,BACKDIV,DOTSTAR,DOTDIV,DOTBACKDIV,NOT,EXP,DOTEXP,AT,DOTTRANS,NUMBER,INT,STRING,ROWJOIN,COLUMNJOIN]:
                    pass
                    g=self.block(_t, "")
                    _t = self._retTree
                    cc.append(g)
                elif la1 and la1 in [3]:
                    pass
                else:
                        raise antlr.NoViableAltException(_t)
                    
                _t = _t327
                _t = _t.getNextSibling()
                sstr="elif "+aexpr+":"+self.nl+self.nl.join(cc)+self.nl
                self.decr()
            elif la1 and la1 in [LITERAL_else]:
                pass
                _t329 = _t
                tmp5_AST_in = _t
                self.match(_t,LITERAL_else)
                _t = _t.getFirstChild()
                self.incr()
                if not _t:
                    _t = antlr.ASTNULL
                la1 = _t.getType()
                if False:
                    pass
                elif la1 and la1 in [EXPR,BLOCK,SIGN_PLUS,SIGN_MINUS,VAR,DOT,ARGUMENTS,ARRAY_END,BREAK,CONT,RETURN,COMMAND,LAMBDA,ALLELEMENTS,TRANS,CELL,MATRIX,FLOAT,COMPLEX,COMMENT,NEWLINE,LBRACK,NAME,COMMA,RBRACK,ASSIGN,LPAREN,RPAREN,LITERAL_if,LITERAL_while,LITERAL_for,LITERAL_try,LITERAL_switch,LITERAL_catch,LITERAL_case,LITERAL_elseif,LITERAL_otherwise,LITERAL_else,LBRACE,COLON,ATPAREN,OROR,ANDAND,OR,AND,EQUAL,NOT_EQUAL,LESS_THAN,LESS_OR_EQUAL,GREATER_THAN,GREATER_OR_EQUAL,PLUS,MINUS,STAR,DIV,BACKDIV,DOTSTAR,DOTDIV,DOTBACKDIV,NOT,EXP,DOTEXP,AT,DOTTRANS,NUMBER,INT,STRING,ROWJOIN,COLUMNJOIN]:
                    pass
                    g=self.block(_t, "")
                    _t = self._retTree
                    cc.append(g)
                elif la1 and la1 in [3]:
                    pass
                else:
                        raise antlr.NoViableAltException(_t)
                    
                _t = _t329
                _t = _t.getNextSibling()
                #print "else"
                sstr="else:"+self.nl+self.nl.join(cc)+self.nl
                self.decr()
            elif la1 and la1 in [LITERAL_for]:
                pass
                _t331 = _t
                tmp6_AST_in = _t
                self.match(_t,LITERAL_for)
                _t = _t.getFirstChild()
                self.incr()
                anoun=self.block(_t, "")
                _t = self._retTree
                bexpr=self.block(_t, "")
                _t = self._retTree
                cblock=self.block(_t, "")
                _t = self._retTree
                _t = _t331
                _t = _t.getNextSibling()
                sstr="for "+anoun+" in "+bexpr+":"+self.nl+cblock+self.nl
                self.decr()
            elif la1 and la1 in [LITERAL_while]:
                pass
                _t332 = _t
                tmp7_AST_in = _t
                self.match(_t,LITERAL_while)
                _t = _t.getFirstChild()
                self.incr()
                aexpr=self.block(_t, "")
                _t = self._retTree
                bblock=self.block(_t, "")
                _t = self._retTree
                _t = _t332
                _t = _t.getNextSibling()
                sstr="while "+aexpr+":"+self.nl+bblock+self.nl
                self.decr()
            elif la1 and la1 in [LITERAL_try]:
                pass
                _t333 = _t
                tmp8_AST_in = _t
                self.match(_t,LITERAL_try)
                _t = _t.getFirstChild()
                self.incr()
                ablock=self.block(_t, "")
                _t = self._retTree
                pass
                bblock=self.block(_t, "")
                _t = self._retTree
                _t = _t333
                _t = _t.getNextSibling()
                sstr="try:"+self.nl+ablock
                self.decr()
                if(bblock):
                   sstr+=self.nl+bblock
                sstr+=self.nl
            elif la1 and la1 in [LITERAL_catch]:
                pass
                _t335 = _t
                tmp9_AST_in = _t
                self.match(_t,LITERAL_catch)
                _t = _t.getFirstChild()
                self.incr()
                bblock=self.block(_t, "")
                _t = self._retTree
                _t = _t335
                _t = _t.getNextSibling()
                sstr="except :"+self.nl+bblock
                self.decr()
            elif la1 and la1 in [LITERAL_switch]:
                pass
                _t336 = _t
                tmp10_AST_in = _t
                self.match(_t,LITERAL_switch)
                _t = _t.getFirstChild()
                aexpr=self.block(_t, "")
                _t = self._retTree
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, "")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t336
                _t = _t.getNextSibling()
                sstr="_switch_val="+aexpr+self.nl
                sstr+="if False: # switch "+cc[0]+self.nl+"    pass"+self.nl+ self.nl.join(cc)
                sstr+=self.nl
            elif la1 and la1 in [LITERAL_case]:
                pass
                _t339 = _t
                tmp11_AST_in = _t
                self.match(_t,LITERAL_case)
                _t = _t.getFirstChild()
                self.incr()
                aexpr=self.block(_t, "")
                _t = self._retTree
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, "")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t339
                _t = _t.getNextSibling()
                sstr="elif _switch_val == "+aexpr+":"+self.nl+self.nl.join(cc)
                #print "CASE"+sstr+"CASE"
                self.decr()
            elif la1 and la1 in [LITERAL_otherwise]:
                pass
                _t342 = _t
                tmp12_AST_in = _t
                self.match(_t,LITERAL_otherwise)
                _t = _t.getFirstChild()
                self.incr()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, "")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t342
                _t = _t.getNextSibling()
                sstr="else:"+self.nl+self.nl.join(cc)
                self.decr()
            elif la1 and la1 in [ANDAND]:
                pass
                _t345 = _t
                tmp13_AST_in = _t
                self.match(_t,ANDAND)
                _t = _t.getFirstChild()
                a=self.block(_t, "and")
                _t = self._retTree
                b=self.block(_t, "and")
                _t = self._retTree
                _t = _t345
                _t = _t.getNextSibling()
                sstr=self.bop(" and ",a,b)
            elif la1 and la1 in [ASSIGN]:
                pass
                _t346 = _t
                tmp14_AST_in = _t
                self.match(_t,ASSIGN)
                _t = _t.getFirstChild()
                self.is_lhs=True
                a=self.block(_t, "=")
                _t = self._retTree
                self.is_lhs=False
                self.is_simple_rhs=True
                #print "Simple RHS"
                b=self.block(_t, "=")
                _t = self._retTree
                self.is_simple_rhs=False
                _t = _t346
                _t = _t.getNextSibling()
                sstr=self.bop(" = ",a,b)
            elif la1 and la1 in [LAMBDA]:
                pass
                _t347 = _t
                tmp15_AST_in = _t
                self.match(_t,LAMBDA)
                _t = _t.getFirstChild()
                a=self.block(_t, "")
                _t = self._retTree
                b=self.block(_t, "")
                _t = self._retTree
                _t = _t347
                _t = _t.getNextSibling()
                sstr="lambda "+a+": "+b
            elif la1 and la1 in [ATPAREN]:
                pass
                _t348 = _t
                tmp16_AST_in = _t
                self.match(_t,ATPAREN)
                _t = _t.getFirstChild()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, ",")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t348
                _t = _t.getNextSibling()
                sstr=", ".join(cc)
            elif la1 and la1 in [BACKDIV]:
                pass
                _t351 = _t
                tmp17_AST_in = _t
                self.match(_t,BACKDIV)
                _t = _t.getFirstChild()
                a=self.block(_t, ",")
                _t = self._retTree
                b=self.block(_t, ",")
                _t = self._retTree
                _t = _t351
                _t = _t.getNextSibling()
                sstr="linalg.solve("+a+", "+b+")"
            elif la1 and la1 in [COLON]:
                pass
                _t352 = _t
                tmp18_AST_in = _t
                self.match(_t,COLON)
                _t = _t.getFirstChild()
                a=self.block(_t, ":")
                _t = self._retTree
                b=self.block(_t, ":")
                _t = self._retTree
                if not _t:
                    _t = antlr.ASTNULL
                la1 = _t.getType()
                if False:
                    pass
                elif la1 and la1 in [EXPR,BLOCK,SIGN_PLUS,SIGN_MINUS,VAR,DOT,ARGUMENTS,ARRAY_END,BREAK,CONT,RETURN,COMMAND,LAMBDA,ALLELEMENTS,TRANS,CELL,MATRIX,FLOAT,COMPLEX,COMMENT,NEWLINE,LBRACK,NAME,COMMA,RBRACK,ASSIGN,LPAREN,RPAREN,LITERAL_if,LITERAL_while,LITERAL_for,LITERAL_try,LITERAL_switch,LITERAL_catch,LITERAL_case,LITERAL_elseif,LITERAL_otherwise,LITERAL_else,LBRACE,COLON,ATPAREN,OROR,ANDAND,OR,AND,EQUAL,NOT_EQUAL,LESS_THAN,LESS_OR_EQUAL,GREATER_THAN,GREATER_OR_EQUAL,PLUS,MINUS,STAR,DIV,BACKDIV,DOTSTAR,DOTDIV,DOTBACKDIV,NOT,EXP,DOTEXP,AT,DOTTRANS,NUMBER,INT,STRING,ROWJOIN,COLUMNJOIN]:
                    pass
                    c=self.block(_t, ":")
                    _t = self._retTree
                elif la1 and la1 in [3]:
                    pass
                else:
                        raise antlr.NoViableAltException(_t)
                    
                _t = _t352
                _t = _t.getNextSibling()
                sstr=self.colonop(a,b,c)
            elif la1 and la1 in [COMMA]:
                pass
                _t354 = _t
                tmp19_AST_in = _t
                self.match(_t,COMMA)
                _t = _t.getFirstChild()
                _cnt356= 0
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        a=self.block(_t, ',')
                        _t = self._retTree
                        cc.append(a)
                    else:
                        break
                    
                    _cnt356 += 1
                if _cnt356 < 1:
                    raise antlr.NoViableAltException(_t)
                _t = _t354
                _t = _t.getNextSibling()
                sstr=self.multiop(", ",cc)
            elif la1 and la1 in [DOT]:
                pass
                _t357 = _t
                tmp20_AST_in = _t
                self.match(_t,DOT)
                _t = _t.getFirstChild()
                a=self.block(_t, '.')
                _t = self._retTree
                _t = _t357
                _t = _t.getNextSibling()
                sstr=self.preop(".",a)
            elif la1 and la1 in [NOT]:
                pass
                _t358 = _t
                tmp21_AST_in = _t
                self.match(_t,NOT)
                _t = _t.getFirstChild()
                a=self.block(_t, "not")
                _t = self._retTree
                _t = _t358
                _t = _t.getNextSibling()
                sstr=self.preop("not ",a)
            elif la1 and la1 in [SIGN_PLUS]:
                pass
                _t359 = _t
                tmp22_AST_in = _t
                self.match(_t,SIGN_PLUS)
                _t = _t.getFirstChild()
                a=self.block(_t, " +")
                _t = self._retTree
                _t = _t359
                _t = _t.getNextSibling()
                sstr=self.preop("+",a)
            elif la1 and la1 in [SIGN_MINUS]:
                pass
                _t360 = _t
                tmp23_AST_in = _t
                self.match(_t,SIGN_MINUS)
                _t = _t.getFirstChild()
                a=self.block(_t, " -")
                _t = self._retTree
                _t = _t360
                _t = _t.getNextSibling()
                sstr=self.preop("-",a)
            elif la1 and la1 in [DOTDIV]:
                pass
                _t361 = _t
                tmp24_AST_in = _t
                self.match(_t,DOTDIV)
                _t = _t.getFirstChild()
                a=self.block(_t, "/")
                _t = self._retTree
                b=self.block(_t, "/")
                _t = self._retTree
                _t = _t361
                _t = _t.getNextSibling()
                sstr=self.bop("/",a,b)
            elif la1 and la1 in [DOTEXP]:
                pass
                _t362 = _t
                tmp25_AST_in = _t
                self.match(_t,DOTEXP)
                _t = _t.getFirstChild()
                a=self.block(_t, "**")
                _t = self._retTree
                b=self.block(_t, "**")
                _t = self._retTree
                _t = _t362
                _t = _t.getNextSibling()
                sstr=self.bop("**",a,b)
            elif la1 and la1 in [DOTSTAR]:
                pass
                _t363 = _t
                tmp26_AST_in = _t
                self.match(_t,DOTSTAR)
                _t = _t.getFirstChild()
                a=self.block(_t, "*")
                _t = self._retTree
                b=self.block(_t, "*")
                _t = self._retTree
                _t = _t363
                _t = _t.getNextSibling()
                sstr=self.bop("*",a,b)
            elif la1 and la1 in [MINUS]:
                pass
                _t364 = _t
                tmp27_AST_in = _t
                self.match(_t,MINUS)
                _t = _t.getFirstChild()
                a=self.block(_t, "-")
                _t = self._retTree
                b=self.block(_t, "-")
                _t = self._retTree
                _t = _t364
                _t = _t.getNextSibling()
                sstr=self.bop("-",a,b)
            elif la1 and la1 in [PLUS]:
                pass
                _t365 = _t
                tmp28_AST_in = _t
                self.match(_t,PLUS)
                _t = _t.getFirstChild()
                a=self.block(_t, "+")
                _t = self._retTree
                b=self.block(_t, "+")
                _t = self._retTree
                _t = _t365
                _t = _t.getNextSibling()
                sstr=self.bop("+",a,b)
            elif la1 and la1 in [EQUAL]:
                pass
                _t366 = _t
                tmp29_AST_in = _t
                self.match(_t,EQUAL)
                _t = _t.getFirstChild()
                a=self.block(_t, "==")
                _t = self._retTree
                b=self.block(_t, "==")
                _t = self._retTree
                _t = _t366
                _t = _t.getNextSibling()
                sstr=self.bop(" == ",a,b)
            elif la1 and la1 in [NOT_EQUAL]:
                pass
                _t367 = _t
                tmp30_AST_in = _t
                self.match(_t,NOT_EQUAL)
                _t = _t.getFirstChild()
                a=self.block(_t, "!=")
                _t = self._retTree
                b=self.block(_t, "!=")
                _t = self._retTree
                _t = _t367
                _t = _t.getNextSibling()
                sstr=self.bop(" != ",a,b)
            elif la1 and la1 in [GREATER_THAN]:
                pass
                _t368 = _t
                tmp31_AST_in = _t
                self.match(_t,GREATER_THAN)
                _t = _t.getFirstChild()
                a=self.block(_t, ">")
                _t = self._retTree
                b=self.block(_t, ">")
                _t = self._retTree
                _t = _t368
                _t = _t.getNextSibling()
                sstr=self.bop(" > ",a,b)
            elif la1 and la1 in [GREATER_OR_EQUAL]:
                pass
                _t369 = _t
                tmp32_AST_in = _t
                self.match(_t,GREATER_OR_EQUAL)
                _t = _t.getFirstChild()
                a=self.block(_t, ">=")
                _t = self._retTree
                b=self.block(_t, ">=")
                _t = self._retTree
                _t = _t369
                _t = _t.getNextSibling()
                sstr=self.bop(" >= ",a,b)
            elif la1 and la1 in [LESS_OR_EQUAL]:
                pass
                _t370 = _t
                tmp33_AST_in = _t
                self.match(_t,LESS_OR_EQUAL)
                _t = _t.getFirstChild()
                a=self.block(_t, "<=")
                _t = self._retTree
                b=self.block(_t, "<=")
                _t = self._retTree
                _t = _t370
                _t = _t.getNextSibling()
                sstr=self.bop("<=",a,b)
            elif la1 and la1 in [LESS_THAN]:
                pass
                _t371 = _t
                tmp34_AST_in = _t
                self.match(_t,LESS_THAN)
                _t = _t.getFirstChild()
                a=self.block(_t, "<")
                _t = self._retTree
                b=self.block(_t, "<")
                _t = self._retTree
                _t = _t371
                _t = _t.getNextSibling()
                sstr=self.bop("<",a,b)
            elif la1 and la1 in [OROR]:
                pass
                _t372 = _t
                tmp35_AST_in = _t
                self.match(_t,OROR)
                _t = _t.getFirstChild()
                a=self.block(_t, "or")
                _t = self._retTree
                b=self.block(_t, "or")
                _t = self._retTree
                _t = _t372
                _t = _t.getNextSibling()
                sstr=self.bop(" or ",a,b)
            elif la1 and la1 in [LPAREN]:
                pass
                _t373 = _t
                tmp36_AST_in = _t
                self.match(_t,LPAREN)
                _t = _t.getFirstChild()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, "")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t373
                _t = _t.getNextSibling()
                sstr="("+", ".join(cc)+")"
            elif la1 and la1 in [ARGUMENTS]:
                pass
                _t376 = _t
                tmp37_AST_in = _t
                self.match(_t,ARGUMENTS)
                _t = _t.getFirstChild()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, ",")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t376
                _t = _t.getNextSibling()
                sstr=self.join_args(cc,ptoken=ptoken)
            elif la1 and la1 in [LBRACE]:
                pass
                _t379 = _t
                tmp38_AST_in = _t
                self.match(_t,LBRACE)
                _t = _t.getFirstChild()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, ",")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t379
                _t = _t.getNextSibling()
                sstr=self.join_args(cc,True)
            elif la1 and la1 in [MATRIX]:
                pass
                _t382 = _t
                tmp39_AST_in = _t
                self.match(_t,MATRIX)
                _t = _t.getFirstChild()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, ",")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t382
                _t = _t.getNextSibling()
                if(cc):
                   sstr="array("+", ".join(cc)+")" 
                else:
                   sstr="array([])"
            elif la1 and la1 in [CELL]:
                pass
                _t385 = _t
                tmp40_AST_in = _t
                self.match(_t,CELL)
                _t = _t.getFirstChild()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, ",")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t385
                _t = _t.getNextSibling()
                if(cc):
                   sstr="cellarray("+", ".join(cc)+")" 
                else:
                   sstr="cellarray([])"
            elif la1 and la1 in [EXPR]:
                pass
                _t388 = _t
                tmp41_AST_in = _t
                self.match(_t,EXPR)
                _t = _t.getFirstChild()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, ",")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t388
                _t = _t.getNextSibling()
                sstr=", ".join(cc)
            elif la1 and la1 in [ROWJOIN]:
                pass
                _t391 = _t
                tmp42_AST_in = _t
                self.match(_t,ROWJOIN)
                _t = _t.getFirstChild()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        a=self.block(_t, ",")
                        _t = self._retTree
                        cc.append(a)
                    else:
                        break
                    
                _t = _t391
                _t = _t.getNextSibling()
                sstr="r_["+", ".join(cc)+"]"
            elif la1 and la1 in [COLUMNJOIN]:
                pass
                _t394 = _t
                tmp43_AST_in = _t
                self.match(_t,COLUMNJOIN)
                _t = _t.getFirstChild()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        a=self.block(_t, ",")
                        _t = self._retTree
                        cc.append(a)
                    else:
                        break
                    
                _t = _t394
                _t = _t.getNextSibling()
                sstr="c_["+", ".join(cc)+"]"
            elif la1 and la1 in [AND]:
                pass
                _t397 = _t
                tmp44_AST_in = _t
                self.match(_t,AND)
                _t = _t.getFirstChild()
                a=self.block(_t, ',')
                _t = self._retTree
                b=self.block(_t, ',')
                _t = self._retTree
                _t = _t397
                _t = _t.getNextSibling()
                sstr="logical_and("+a+", "+b+")"
            elif la1 and la1 in [OR]:
                pass
                _t398 = _t
                tmp45_AST_in = _t
                self.match(_t,OR)
                _t = _t.getFirstChild()
                a=self.block(_t, ",")
                _t = self._retTree
                b=self.block(_t, ",")
                _t = self._retTree
                _t = _t398
                _t = _t.getNextSibling()
                sstr="logical_or("+a+", "+b+")"
            elif la1 and la1 in [STAR]:
                pass
                _t399 = _t
                tmp46_AST_in = _t
                self.match(_t,STAR)
                _t = _t.getFirstChild()
                a=self.block(_t, ",")
                _t = self._retTree
                b=self.block(_t, ",")
                _t = self._retTree
                _t = _t399
                _t = _t.getNextSibling()
                sstr="dot("+a+", "+b+")"
            elif la1 and la1 in [DIV]:
                pass
                _t400 = _t
                tmp47_AST_in = _t
                self.match(_t,DIV)
                _t = _t.getFirstChild()
                a=self.block(_t, ',')
                _t = self._retTree
                b=self.block(_t, ',')
                _t = self._retTree
                _t = _t400
                _t = _t.getNextSibling()
                sstr="matdiv("+a+", "+b+")"
            elif la1 and la1 in [DOTBACKDIV]:
                pass
                _t401 = _t
                tmp48_AST_in = _t
                self.match(_t,DOTBACKDIV)
                _t = _t.getFirstChild()
                a=self.block(_t, ',')
                _t = self._retTree
                b=self.block(_t, ',')
                _t = self._retTree
                _t = _t401
                _t = _t.getNextSibling()
                sstr="matbackdiv("+a+", "+b+")"
            elif la1 and la1 in [EXP]:
                pass
                _t402 = _t
                tmp49_AST_in = _t
                self.match(_t,EXP)
                _t = _t.getFirstChild()
                a=self.block(_t, ",")
                _t = self._retTree
                b=self.block(_t, ",")
                _t = self._retTree
                _t = _t402
                _t = _t.getNextSibling()
                sstr="matixpower("+a+", "+b+")"
            elif la1 and la1 in [AT]:
                pass
                _t403 = _t
                tmp50_AST_in = _t
                self.match(_t,AT)
                _t = _t.getFirstChild()
                a=self.block(_t, ptoken)
                _t = self._retTree
                _t = _t403
                _t = _t.getNextSibling()
                sstr=a
            elif la1 and la1 in [BREAK]:
                pass
                tmp51_AST_in = _t
                self.match(_t,BREAK)
                _t = _t.getNextSibling()
                sstr="break"
            elif la1 and la1 in [CONT]:
                pass
                tmp52_AST_in = _t
                self.match(_t,CONT)
                _t = _t.getNextSibling()
                sstr="continue"
            elif la1 and la1 in [RETURN]:
                pass
                tmp53_AST_in = _t
                self.match(_t,RETURN)
                _t = _t.getNextSibling()
                sstr="return ["+self.returnval+"]"
            elif la1 and la1 in [ARRAY_END]:
                pass
                tmp54_AST_in = _t
                self.match(_t,ARRAY_END)
                _t = _t.getNextSibling()
                sstr="xend"
            elif la1 and la1 in [ALLELEMENTS]:
                pass
                tmp55_AST_in = _t
                self.match(_t,ALLELEMENTS)
                _t = _t.getNextSibling()
                sstr=":"
            elif la1 and la1 in [TRANS]:
                pass
                _t404 = _t
                tmp56_AST_in = _t
                self.match(_t,TRANS)
                _t = _t.getFirstChild()
                a=self.block(_t, ".")
                _t = self._retTree
                _t = _t404
                _t = _t.getNextSibling()
                sstr=a+".conj().T"
            elif la1 and la1 in [DOTTRANS]:
                pass
                _t405 = _t
                tmp57_AST_in = _t
                self.match(_t,DOTTRANS)
                _t = _t.getFirstChild()
                a=self.block(_t, ".")
                _t = self._retTree
                _t = _t405
                _t = _t.getNextSibling()
                sstr=a+".T"
            elif la1 and la1 in [COMMAND]:
                pass
                _t406 = _t
                q = antlr.ifelse(_t == antlr.ASTNULL, None, _t)
                self.match(_t,COMMAND)
                _t = _t.getFirstChild()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        a=self.block(_t, "NAME")
                        _t = self._retTree
                        cc.append("'"+a+"'")
                    else:
                        break
                    
                _t = _t406
                _t = _t.getNextSibling()
                sstr=self.Lookup(q.getText())+"("+"".join(cc)+")"
            elif la1 and la1 in [NAME]:
                pass
                _t409 = _t
                i = antlr.ifelse(_t == antlr.ASTNULL, None, _t)
                self.match(_t,NAME)
                _t = _t.getFirstChild()
                self.nargin=0
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, "NAME")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t409
                _t = _t.getNextSibling()
                if(cc):
                   sstr=self.Lookup(i.getText())+"".join(cc)
                else:
                   
                   sstr=self.Lookup(i.getText())+"()"
            elif la1 and la1 in [NEWLINE]:
                pass
                j = _t
                self.match(_t,NEWLINE)
                _t = _t.getNextSibling()
                sstr=j.getText()
            elif la1 and la1 in [NUMBER]:
                pass
                k = _t
                self.match(_t,NUMBER)
                _t = _t.getNextSibling()
                sstr=k.getText()
            elif la1 and la1 in [INT]:
                pass
                u = _t
                self.match(_t,INT)
                _t = _t.getNextSibling()
                sstr=u.getText()+"."
            elif la1 and la1 in [FLOAT]:
                pass
                v = _t
                self.match(_t,FLOAT)
                _t = _t.getNextSibling()
                sstr=v.getText()
            elif la1 and la1 in [COMPLEX]:
                pass
                w = _t
                self.match(_t,COMPLEX)
                _t = _t.getNextSibling()
                sstr=w.getText()
            elif la1 and la1 in [RBRACK]:
                pass
                tmp58_AST_in = _t
                self.match(_t,RBRACK)
                _t = _t.getNextSibling()
                sstr=""
            elif la1 and la1 in [LBRACK]:
                pass
                _t412 = _t
                tmp59_AST_in = _t
                self.match(_t,LBRACK)
                _t = _t.getFirstChild()
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, "")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t412
                _t = _t.getNextSibling()
                sstr="["+", ".join(cc)+"]"
            elif la1 and la1 in [RPAREN]:
                pass
                m = _t
                self.match(_t,RPAREN)
                _t = _t.getNextSibling()
                sstr=""
            elif la1 and la1 in [STRING]:
                pass
                p = _t
                self.match(_t,STRING)
                _t = _t.getNextSibling()
                sstr=p.getText().replace("''",r"\'")
            elif la1 and la1 in [VAR]:
                pass
                _t415 = _t
                r = antlr.ifelse(_t == antlr.ASTNULL, None, _t)
                self.match(_t,VAR)
                _t = _t.getFirstChild()
                self.in_var=True
                while True:
                    if not _t:
                        _t = antlr.ASTNULL
                    if (_tokenSet_0.member(_t.getType())):
                        pass
                        g=self.block(_t, "VAR")
                        _t = self._retTree
                        cc.append(g)
                    else:
                        break
                    
                _t = _t415
                _t = _t.getNextSibling()
                if(cc):
                   sstr=(r.getText())+"".join(cc)
                else:
                   sstr=(r.getText())
                   if(self.is_simple_rhs):
                       sstr+=".copy()"
                self.in_var=False
            elif la1 and la1 in [COMMENT]:
                pass
                t=self.comment(_t)
                _t = self._retTree
                sstr=t
                if not _t:
                    _t = antlr.ASTNULL
                if (_tokenSet_0.member(_t.getType())):
                    pass
                    g=self.block(_t, ptoken)
                    _t = self._retTree
                    sstr+=g
                elif (_tokenSet_1.member(_t.getType())):
                    pass
                else:
                    raise antlr.NoViableAltException(_t)
                
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return sstr
    
    def funcreturn(self, _t):    
        sstr = None
        
        funcreturn_AST_in = None
        if _t != antlr.ASTNULL:
            funcreturn_AST_in = _t
        a = None
        sstr=""
        cc=[]
        #print "in funcreturn"
        try:      ## for error handling
            pass
            _t317 = _t
            tmp60_AST_in = _t
            self.match(_t,RETURN_VARS)
            _t = _t.getFirstChild()
            _cnt319= 0
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==VAR):
                    pass
                    a = _t
                    self.match(_t,VAR)
                    _t = _t.getNextSibling()
                    cc.append(a.getText())
                else:
                    break
                
                _cnt319 += 1
            if _cnt319 < 1:
                raise antlr.NoViableAltException(_t)
            _t = _t317
            _t = _t.getNextSibling()
            sstr=", ".join(cc)
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return sstr
    
    def funcargs(self, _t):    
        sstr = None
        
        funcargs_AST_in = None
        if _t != antlr.ASTNULL:
            funcargs_AST_in = _t
        a = None
        sstr=""
        cc=[]
        #print "in funcargs"
        try:      ## for error handling
            pass
            _t420 = _t
            tmp61_AST_in = _t
            self.match(_t,FUNCTION_ARGS)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==VAR):
                    pass
                    a = _t
                    self.match(_t,VAR)
                    _t = _t.getNextSibling()
                    cc.append(a.getText())
                else:
                    break
                
            _t = _t420
            _t = _t.getNextSibling()
            sstr="("+", ".join(cc)+")"
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return sstr
    
    def default(self, _t):    
        sstr = None
        
        default_AST_in = None
        if _t != antlr.ASTNULL:
            default_AST_in = _t
        b = None
        c = None
        a = None
        sstr=""
        try:      ## for error handling
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [NAME]:
                pass
                _t424 = _t
                b = antlr.ifelse(_t == antlr.ASTNULL, None, _t)
                self.match(_t,NAME)
                _t = _t.getFirstChild()
                if not _t:
                    _t = antlr.ASTNULL
                la1 = _t.getType()
                if False:
                    pass
                elif la1 and la1 in [NAME]:
                    pass
                    c = _t
                    self.match(_t,NAME)
                    _t = _t.getNextSibling()
                elif la1 and la1 in [3]:
                    pass
                else:
                        raise antlr.NoViableAltException(_t)
                    
                _t = _t424
                _t = _t.getNextSibling()
                sstr=_t.getText()
                #print "sdsdsd "+_t.toString()
            elif la1 and la1 in [COMMENT]:
                pass
                a = _t
                self.match(_t,COMMENT)
                _t = _t.getNextSibling()
                sstr="#"+a.getText()+"\n"
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return sstr
    

_tokenNames = [
    "<0>", 
    "EOF", 
    "<2>", 
    "NULL_TREE_LOOKAHEAD", 
    "EXPR", 
    "DECL", 
    "FUNCTION", 
    "IFBLOCK", 
    "BLOCK", 
    "BCOLON", 
    "SIGN_PLUS", 
    "SIGN_MINUS", 
    "VAR", 
    "SCOPE", 
    "DOT", 
    "ARGUMENTS", 
    "CONTINUATION", 
    "END", 
    "ARRAY_END", 
    "\"break\"", 
    "\"continue\"", 
    "\"return\"", 
    "RETURN_VARS", 
    "COMMAND", 
    "LAMBDA", 
    "ALLELEMENTS", 
    "TRANS", 
    "CELL", 
    "MATRIX", 
    "COLUMN_JOIN", 
    "ROW_JOIN", 
    "FLOAT", 
    "COMPLEX", 
    "\"assert\"", 
    "\"global\"", 
    "FUNCTION_ARGS", 
    "BRACE_ARGS", 
    "PAREN_ARGS", 
    "SPACE", 
    "COMMENT", 
    "NEWLINE", 
    "\"function\"", 
    "LBRACK", 
    "NAME", 
    "COMMA", 
    "RBRACK", 
    "ASSIGN", 
    "LPAREN", 
    "RPAREN", 
    "\"if\"", 
    "\"while\"", 
    "\"for\"", 
    "\"try\"", 
    "\"switch\"", 
    "\"catch\"", 
    "\"case\"", 
    "\"elseif\"", 
    "\"otherwise\"", 
    "\"else\"", 
    "SEMI", 
    "LBRACE", 
    "RBRACE", 
    "COLON", 
    "ATPAREN", 
    "OROR", 
    "ANDAND", 
    "OR", 
    "AND", 
    "EQUAL", 
    "NOT_EQUAL", 
    "LESS_THAN", 
    "LESS_OR_EQUAL", 
    "GREATER_THAN", 
    "GREATER_OR_EQUAL", 
    "PLUS", 
    "MINUS", 
    "STAR", 
    "DIV", 
    "BACKDIV", 
    "DOTSTAR", 
    "DOTDIV", 
    "DOTBACKDIV", 
    "NOT", 
    "EXP", 
    "DOTEXP", 
    "AT", 
    "DOTTRANS", 
    "NUMBER", 
    "INT", 
    "MATCHVAR", 
    "STRING", 
    "Exponent", 
    "MATCH", 
    "DIGIT", 
    "ROWJOIN", 
    "COLUMNJOIN"
]
    

### generate bit set
def mk_tokenSet_0(): 
    ### var1
    data = [ -2882306503321264880L, 3321888767L, 0L, 0L]
    return data
_tokenSet_0 = antlr.BitSet(mk_tokenSet_0())

### generate bit set
def mk_tokenSet_1(): 
    ### var1
    data = [ -2882306503321264872L, 3321888767L, 0L, 0L]
    return data
_tokenSet_1 = antlr.BitSet(mk_tokenSet_1())
