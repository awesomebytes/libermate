### $ANTLR 2.7.6 (20071205): "mat2py.g" -> "MatlabParser.py"$
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
### preamble action>>>

### preamble action <<<

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

class Parser(antlr.LLkParser):
    ### user action >>>
    ### user action <<<
    
    def __init__(self, *args, **kwargs):
        antlr.LLkParser.__init__(self, *args, **kwargs)
        self.tokenNames = _tokenNames
        self.buildTokenTypeASTClassMap()
        self.astFactory = antlr.ASTFactory(self.getTokenTypeToASTClassMap())
        self.astFactory.setASTNodeClass()
        ### __init__ header action >>> 
        # gets inserted in the __init__ method of each of the generated Python
        # classes
        #
        self.paren_count=0
        self.brack_count=0
        self.string_ok=True
        self.gobble_space=True
        ### __init__ header action <<< 
        
    def sp(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        sp_AST = None
        try:      ## for error handling
            pass
            self.match(SPACE)
            sp_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_0)
            else:
                raise ex
        
        self.returnAST = sp_AST
    
    def script(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        script_AST = None
        try:      ## for error handling
            if not True:
                raise antlr.SemanticException("True")
            pass
            while True:
                if (self.LA(1)==COMMENT or self.LA(1)==NEWLINE):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [COMMENT]:
                        pass
                        tmp63_AST = None
                        tmp63_AST = self.astFactory.create(self.LT(1))
                        self.addASTChild(currentAST, tmp63_AST)
                        self.match(COMMENT)
                    elif la1 and la1 in [NEWLINE]:
                        pass
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    self.match(NEWLINE)
                else:
                    break
                
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LITERAL_function]:
                pass
                _cnt8= 0
                while True:
                    if (self.LA(1)==LITERAL_function):
                        pass
                        self.function()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
                    _cnt8 += 1
                if _cnt8 < 1:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            elif la1 and la1 in [EOF,ARRAY_END,BREAK,CONT,RETURN,FLOAT,COMPLEX,ASSERT,GLOBAL,SPACE,LBRACK,NAME,LPAREN,LITERAL_if,LITERAL_while,LITERAL_for,LITERAL_try,LITERAL_switch,LBRACE,ATPAREN,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                pass
                self.block()
                self.addASTChild(currentAST, self.returnAST)
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            self.match(EOF_TYPE)
            script_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_1)
            else:
                raise ex
        
        self.returnAST = script_AST
    
    def function(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        function_AST = None
        try:      ## for error handling
            pass
            self.match(LITERAL_function)
            if not self.inputState.guessing:
                self.new_scope()
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [SPACE]:
                pass
                self.sp()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [LBRACK,NAME]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            if (self.LA(1)==LBRACK or self.LA(1)==NAME) and (_tokenSet_2.member(self.LA(2))):
                pass
                self.funcreturn()
                self.addASTChild(currentAST, self.returnAST)
            elif (self.LA(1)==NAME) and (_tokenSet_3.member(self.LA(2))):
                pass
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            
            self.noun()
            self.addASTChild(currentAST, self.returnAST)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LPAREN]:
                pass
                self.funcargs()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            _cnt14= 0
            while True:
                if (_tokenSet_4.member(self.LA(1))):
                    pass
                    self.ender()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
                _cnt14 += 1
            if _cnt14 < 1:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            self.block()
            self.addASTChild(currentAST, self.returnAST)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [END]:
                pass
                self.match(END)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                _cnt18= 0
                while True:
                    if (_tokenSet_4.member(self.LA(1))):
                        pass
                        self.ender()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
                    _cnt18 += 1
                if _cnt18 < 1:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            elif la1 and la1 in [EOF,LITERAL_function]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            if not self.inputState.guessing:
                function_AST = currentAST.root
                function_AST = antlr.make(self.astFactory.create(FUNCTION,"function"), self.get_scope(), function_AST);
                currentAST.root = function_AST
                if (function_AST != None) and (function_AST.getFirstChild() != None):
                    currentAST.child = function_AST.getFirstChild()
                else:
                    currentAST.child = function_AST
                currentAST.advanceChildToEnd()
            function_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_5)
            else:
                raise ex
        
        self.returnAST = function_AST
    
    def block(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        block_AST = None
        try:      ## for error handling
            pass
            while True:
                if (_tokenSet_6.member(self.LA(1))):
                    pass
                    self.command_or_statement()
                    self.addASTChild(currentAST, self.returnAST)
                    _cnt39= 0
                    while True:
                        if (_tokenSet_4.member(self.LA(1))):
                            pass
                            self.ender()
                            self.addASTChild(currentAST, self.returnAST)
                        else:
                            break
                        
                        _cnt39 += 1
                    if _cnt39 < 1:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                else:
                    break
                
            if not self.inputState.guessing:
                block_AST = currentAST.root
                block_AST = antlr.make(self.astFactory.create(BLOCK,"block"), block_AST);
                currentAST.root = block_AST
                if (block_AST != None) and (block_AST.getFirstChild() != None):
                    currentAST.child = block_AST.getFirstChild()
                else:
                    currentAST.child = block_AST
                currentAST.advanceChildToEnd()
            block_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_7)
            else:
                raise ex
        
        self.returnAST = block_AST
    
    def funcreturn(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        funcreturn_AST = None
        a = None
        a_AST = None
        b = None
        b_AST = None
        r = None
        r_AST = None
        c = None
        c_AST = None
        d = None
        d_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LBRACK]:
                pass
                self.match(LBRACK)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [NAME]:
                    pass
                    a = self.LT(1)
                    a_AST = self.astFactory.create(a)
                    self.addASTChild(currentAST, a_AST)
                    self.match(NAME)
                    if not self.inputState.guessing:
                        self.as_var(a_AST)
                    while True:
                        if (self.LA(1)==SPACE or self.LA(1)==COMMA):
                            pass
                            la1 = self.LA(1)
                            if False:
                                pass
                            elif la1 and la1 in [SPACE]:
                                pass
                                self.sp()
                                self.addASTChild(currentAST, self.returnAST)
                            elif la1 and la1 in [COMMA]:
                                pass
                                self.match(COMMA)
                                la1 = self.LA(1)
                                if False:
                                    pass
                                elif la1 and la1 in [SPACE]:
                                    pass
                                    self.sp()
                                    self.addASTChild(currentAST, self.returnAST)
                                elif la1 and la1 in [NAME]:
                                    pass
                                else:
                                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                                    
                            else:
                                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                                
                            b = self.LT(1)
                            b_AST = self.astFactory.create(b)
                            self.addASTChild(currentAST, b_AST)
                            self.match(NAME)
                            if not self.inputState.guessing:
                                self.as_var(b_AST)
                        else:
                            break
                        
                elif la1 and la1 in [RBRACK]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.match(RBRACK)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [ASSIGN]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                r = self.LT(1)
                r_AST = self.astFactory.create(r)
                self.makeASTRoot(currentAST, r_AST)
                self.match(ASSIGN)
                if not self.inputState.guessing:
                    r_AST.setType(RETURN_VARS)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [NAME]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                funcreturn_AST = currentAST.root
            elif la1 and la1 in [NAME]:
                pass
                c = self.LT(1)
                c_AST = self.astFactory.create(c)
                self.addASTChild(currentAST, c_AST)
                self.match(NAME)
                if not self.inputState.guessing:
                    self.as_var(c_AST)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [ASSIGN]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                d = self.LT(1)
                d_AST = self.astFactory.create(d)
                self.makeASTRoot(currentAST, d_AST)
                self.match(ASSIGN)
                if not self.inputState.guessing:
                    d_AST.setType(RETURN_VARS)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [NAME]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                funcreturn_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_8)
            else:
                raise ex
        
        self.returnAST = funcreturn_AST
    
    def noun(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        noun_AST = None
        a = None
        a_AST = None
        try:      ## for error handling
            pass
            a = self.LT(1)
            a_AST = self.astFactory.create(a)
            self.addASTChild(currentAST, a_AST)
            self.match(NAME)
            if not self.inputState.guessing:
                self.var_lookup(a_AST)
            noun_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_3)
            else:
                raise ex
        
        self.returnAST = noun_AST
    
    def funcargs(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        funcargs_AST = None
        p = None
        p_AST = None
        a = None
        a_AST = None
        b = None
        b_AST = None
        try:      ## for error handling
            pass
            p = self.LT(1)
            p_AST = self.astFactory.create(p)
            self.makeASTRoot(currentAST, p_AST)
            self.match(LPAREN)
            if not self.inputState.guessing:
                p_AST.setType(FUNCTION_ARGS)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [NAME]:
                pass
                a = self.LT(1)
                a_AST = self.astFactory.create(a)
                self.addASTChild(currentAST, a_AST)
                self.match(NAME)
                if not self.inputState.guessing:
                    self.as_var(a_AST)
                while True:
                    if (self.LA(1)==SPACE or self.LA(1)==COMMA):
                        pass
                        la1 = self.LA(1)
                        if False:
                            pass
                        elif la1 and la1 in [SPACE]:
                            pass
                            self.sp()
                            self.addASTChild(currentAST, self.returnAST)
                        elif la1 and la1 in [COMMA]:
                            pass
                        else:
                                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                            
                        self.match(COMMA)
                        la1 = self.LA(1)
                        if False:
                            pass
                        elif la1 and la1 in [SPACE]:
                            pass
                            self.sp()
                            self.addASTChild(currentAST, self.returnAST)
                        elif la1 and la1 in [NAME]:
                            pass
                        else:
                                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                            
                        b = self.LT(1)
                        b_AST = self.astFactory.create(b)
                        self.addASTChild(currentAST, b_AST)
                        self.match(NAME)
                        if not self.inputState.guessing:
                            self.as_var(b_AST)
                    else:
                        break
                    
            elif la1 and la1 in [RPAREN]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            self.match(RPAREN)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [SPACE]:
                pass
                self.sp()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            funcargs_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_4)
            else:
                raise ex
        
        self.returnAST = funcargs_AST
    
    def ender(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        ender_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [COMMENT,NEWLINE]:
                pass
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [COMMENT]:
                    pass
                    tmp73_AST = None
                    tmp73_AST = self.astFactory.create(self.LT(1))
                    self.addASTChild(currentAST, tmp73_AST)
                    self.match(COMMENT)
                elif la1 and la1 in [NEWLINE]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.match(NEWLINE)
                ender_AST = currentAST.root
            elif la1 and la1 in [SEMI]:
                pass
                self.match(SEMI)
                ender_AST = currentAST.root
            elif la1 and la1 in [COMMA]:
                pass
                self.match(COMMA)
                ender_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_9)
            else:
                raise ex
        
        self.returnAST = ender_AST
    
    def command_or_statement(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        command_or_statement_AST = None
        a = None
        a_AST = None
        t_AST = None
        tb_AST = None
        b = None
        b_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [GLOBAL]:
                pass
                tmp77_AST = None
                tmp77_AST = self.astFactory.create(self.LT(1))
                self.match(GLOBAL)
                _cnt43= 0
                while True:
                    if (self.LA(1)==NAME):
                        pass
                        a = self.LT(1)
                        a_AST = self.astFactory.create(a)
                        self.match(NAME)
                        if not self.inputState.guessing:
                            self.as_global(a_AST)
                    else:
                        break
                    
                    _cnt43 += 1
                if _cnt43 < 1:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            elif la1 and la1 in [LITERAL_if]:
                pass
                tmp78_AST = None
                tmp78_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp78_AST)
                self.match(LITERAL_if)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,ATPAREN,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.expr()
                t_AST = self.returnAST
                self.addASTChild(currentAST, self.returnAST)
                _cnt48= 0
                while True:
                    if (_tokenSet_4.member(self.LA(1))):
                        pass
                        self.ender()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
                    _cnt48 += 1
                if _cnt48 < 1:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                self.block()
                tb_AST = self.returnAST
                self.addASTChild(currentAST, self.returnAST)
                while True:
                    if (self.LA(1)==LITERAL_elseif):
                        pass
                        self.elseifblock()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [LITERAL_else]:
                    pass
                    self.elseblock()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [END]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.match(END)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                command_or_statement_AST = currentAST.root
            elif la1 and la1 in [LITERAL_while]:
                pass
                tmp80_AST = None
                tmp80_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp80_AST)
                self.match(LITERAL_while)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,ATPAREN,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.expr()
                self.addASTChild(currentAST, self.returnAST)
                _cnt55= 0
                while True:
                    if (_tokenSet_4.member(self.LA(1))):
                        pass
                        self.ender()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
                    _cnt55 += 1
                if _cnt55 < 1:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                self.block()
                self.addASTChild(currentAST, self.returnAST)
                self.match(END)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                command_or_statement_AST = currentAST.root
            elif la1 and la1 in [LITERAL_for]:
                pass
                tmp82_AST = None
                tmp82_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp82_AST)
                self.match(LITERAL_for)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [NAME]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                b = self.LT(1)
                b_AST = self.astFactory.create(b)
                self.addASTChild(currentAST, b_AST)
                self.match(NAME)
                if not self.inputState.guessing:
                    self.as_var(b_AST)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [ASSIGN]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.match(ASSIGN)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,ATPAREN,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.expr()
                self.addASTChild(currentAST, self.returnAST)
                _cnt61= 0
                while True:
                    if (_tokenSet_4.member(self.LA(1))):
                        pass
                        self.ender()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
                    _cnt61 += 1
                if _cnt61 < 1:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                self.block()
                self.addASTChild(currentAST, self.returnAST)
                self.match(END)
                command_or_statement_AST = currentAST.root
            elif la1 and la1 in [LITERAL_try]:
                pass
                tmp85_AST = None
                tmp85_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp85_AST)
                self.match(LITERAL_try)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.ender()
                self.addASTChild(currentAST, self.returnAST)
                self.block()
                self.addASTChild(currentAST, self.returnAST)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [LITERAL_catch]:
                    pass
                    self.catchblock()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [END]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.match(END)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                command_or_statement_AST = currentAST.root
            elif la1 and la1 in [LITERAL_switch]:
                pass
                tmp87_AST = None
                tmp87_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp87_AST)
                self.match(LITERAL_switch)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,ATPAREN,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.expr()
                self.addASTChild(currentAST, self.returnAST)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                _cnt68= 0
                while True:
                    if (_tokenSet_4.member(self.LA(1))):
                        pass
                        self.ender()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
                    _cnt68 += 1
                if _cnt68 < 1:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                _cnt70= 0
                while True:
                    if (self.LA(1)==LITERAL_case):
                        pass
                        self.caseblock()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
                    _cnt70 += 1
                if _cnt70 < 1:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [LITERAL_otherwise]:
                    pass
                    self.otherwiseblock()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [END]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.match(END)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                command_or_statement_AST = currentAST.root
            elif la1 and la1 in [SPACE]:
                pass
                self.match(SPACE)
                command_or_statement_AST = currentAST.root
            else:
                synPredMatched45 = False
                if (self.LA(1)==NAME) and (_tokenSet_10.member(self.LA(2))):
                    _m45 = self.mark()
                    synPredMatched45 = True
                    self.inputState.guessing += 1
                    try:
                        pass
                        self.match(NAME)
                        self.noun()
                    except antlr.RecognitionException, pe:
                        synPredMatched45 = False
                    self.rewind(_m45)
                    self.inputState.guessing -= 1
                if synPredMatched45:
                    pass
                    self.command()
                    self.addASTChild(currentAST, self.returnAST)
                    command_or_statement_AST = currentAST.root
                elif (_tokenSet_11.member(self.LA(1))) and (_tokenSet_12.member(self.LA(2))):
                    pass
                    self.substatement()
                    self.addASTChild(currentAST, self.returnAST)
                    command_or_statement_AST = currentAST.root
                else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_4)
            else:
                raise ex
        
        self.returnAST = command_or_statement_AST
    
    def command(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        command_AST = None
        a = None
        a_AST = None
        b = None
        b_AST = None
        try:      ## for error handling
            pass
            a = self.LT(1)
            a_AST = self.astFactory.create(a)
            self.makeASTRoot(currentAST, a_AST)
            self.match(NAME)
            if not self.inputState.guessing:
                a_AST.setType(COMMAND)
            while True:
                if (self.LA(1)==NAME):
                    pass
                    b = self.LT(1)
                    b_AST = self.astFactory.create(b)
                    self.addASTChild(currentAST, b_AST)
                    self.match(NAME)
                    if not self.inputState.guessing:
                        b_AST.setType(STRING)
                else:
                    break
                
            command_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_4)
            else:
                raise ex
        
        self.returnAST = command_AST
    
    def expr(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                pass
                self.expr_1()
                self.addASTChild(currentAST, self.returnAST)
                expr_AST = currentAST.root
            elif la1 and la1 in [ATPAREN]:
                pass
                self.expr_at()
                self.addASTChild(currentAST, self.returnAST)
                self.expr_1()
                self.addASTChild(currentAST, self.returnAST)
                if not self.inputState.guessing:
                    expr_AST = currentAST.root
                    expr_AST = antlr.make(self.astFactory.create(LAMBDA), expr_AST);
                    currentAST.root = expr_AST
                    if (expr_AST != None) and (expr_AST.getFirstChild() != None):
                        currentAST.child = expr_AST.getFirstChild()
                    else:
                        currentAST.child = expr_AST
                    currentAST.advanceChildToEnd()
                expr_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_13)
            else:
                raise ex
        
        self.returnAST = expr_AST
    
    def elseifblock(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        elseifblock_AST = None
        try:      ## for error handling
            pass
            tmp90_AST = None
            tmp90_AST = self.astFactory.create(self.LT(1))
            self.makeASTRoot(currentAST, tmp90_AST)
            self.match(LITERAL_elseif)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [SPACE]:
                pass
                self.sp()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,ATPAREN,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            self.expr()
            self.addASTChild(currentAST, self.returnAST)
            _cnt85= 0
            while True:
                if (_tokenSet_4.member(self.LA(1))):
                    pass
                    self.ender()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
                _cnt85 += 1
            if _cnt85 < 1:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            self.block()
            self.addASTChild(currentAST, self.returnAST)
            elseifblock_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_14)
            else:
                raise ex
        
        self.returnAST = elseifblock_AST
    
    def elseblock(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        elseblock_AST = None
        a = None
        a_AST = None
        try:      ## for error handling
            pass
            a = self.LT(1)
            a_AST = self.astFactory.create(a)
            self.makeASTRoot(currentAST, a_AST)
            self.match(LITERAL_else)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [SPACE]:
                pass
                self.sp()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [ARRAY_END,BREAK,CONT,RETURN,FLOAT,COMPLEX,ASSERT,COMMENT,NEWLINE,LBRACK,NAME,COMMA,LPAREN,SEMI,LBRACE,ATPAREN,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                pass
                _cnt94= 0
                while True:
                    if (_tokenSet_4.member(self.LA(1))):
                        pass
                        self.ender()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
                    _cnt94 += 1
                if _cnt94 < 1:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                self.block()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [ARRAY_END,BREAK,CONT,RETURN,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,ATPAREN,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                pass
                self.substatement()
                self.addASTChild(currentAST, self.returnAST)
                _cnt96= 0
                while True:
                    if (_tokenSet_4.member(self.LA(1))):
                        pass
                        self.ender()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
                    _cnt96 += 1
                if _cnt96 < 1:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            elseblock_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_15)
            else:
                raise ex
        
        self.returnAST = elseblock_AST
    
    def catchblock(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        catchblock_AST = None
        try:      ## for error handling
            pass
            tmp91_AST = None
            tmp91_AST = self.astFactory.create(self.LT(1))
            self.makeASTRoot(currentAST, tmp91_AST)
            self.match(LITERAL_catch)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [SPACE]:
                pass
                self.sp()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            _cnt76= 0
            while True:
                if (_tokenSet_4.member(self.LA(1))):
                    pass
                    self.ender()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
                _cnt76 += 1
            if _cnt76 < 1:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            self.block()
            self.addASTChild(currentAST, self.returnAST)
            catchblock_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_15)
            else:
                raise ex
        
        self.returnAST = catchblock_AST
    
    def caseblock(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        caseblock_AST = None
        try:      ## for error handling
            pass
            tmp92_AST = None
            tmp92_AST = self.astFactory.create(self.LT(1))
            self.makeASTRoot(currentAST, tmp92_AST)
            self.match(LITERAL_case)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [SPACE]:
                pass
                self.sp()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,ATPAREN,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            self.expr()
            self.addASTChild(currentAST, self.returnAST)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [SPACE]:
                pass
                self.sp()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            _cnt81= 0
            while True:
                if (_tokenSet_4.member(self.LA(1))):
                    pass
                    self.ender()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
                _cnt81 += 1
            if _cnt81 < 1:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            self.block()
            self.addASTChild(currentAST, self.returnAST)
            caseblock_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_16)
            else:
                raise ex
        
        self.returnAST = caseblock_AST
    
    def otherwiseblock(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        otherwiseblock_AST = None
        try:      ## for error handling
            pass
            tmp93_AST = None
            tmp93_AST = self.astFactory.create(self.LT(1))
            self.makeASTRoot(currentAST, tmp93_AST)
            self.match(LITERAL_otherwise)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [SPACE]:
                pass
                self.sp()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            _cnt89= 0
            while True:
                if (_tokenSet_4.member(self.LA(1))):
                    pass
                    self.ender()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
                _cnt89 += 1
            if _cnt89 < 1:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            self.block()
            self.addASTChild(currentAST, self.returnAST)
            otherwiseblock_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_15)
            else:
                raise ex
        
        self.returnAST = otherwiseblock_AST
    
    def substatement(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        substatement_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [BREAK]:
                pass
                tmp94_AST = None
                tmp94_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp94_AST)
                self.match(BREAK)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                substatement_AST = currentAST.root
            elif la1 and la1 in [CONT]:
                pass
                tmp95_AST = None
                tmp95_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp95_AST)
                self.match(CONT)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                substatement_AST = currentAST.root
            elif la1 and la1 in [RETURN]:
                pass
                tmp96_AST = None
                tmp96_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp96_AST)
                self.match(RETURN)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SPACE]:
                    pass
                    self.sp()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [COMMENT,NEWLINE,COMMA,SEMI]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                substatement_AST = currentAST.root
            else:
                synPredMatched103 = False
                if (self.LA(1)==LBRACK or self.LA(1)==NAME) and (_tokenSet_17.member(self.LA(2))):
                    _m103 = self.mark()
                    synPredMatched103 = True
                    self.inputState.guessing += 1
                    try:
                        pass
                        self.lhs()
                        la1 = self.LA(1)
                        if False:
                            pass
                        elif la1 and la1 in [SPACE]:
                            pass
                            self.match(SPACE)
                        elif la1 and la1 in [ASSIGN]:
                            pass
                        else:
                                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                            
                        self.match(ASSIGN)
                    except antlr.RecognitionException, pe:
                        synPredMatched103 = False
                    self.rewind(_m103)
                    self.inputState.guessing -= 1
                if synPredMatched103:
                    pass
                    self.lhs()
                    self.addASTChild(currentAST, self.returnAST)
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [SPACE]:
                        pass
                        self.sp()
                        self.addASTChild(currentAST, self.returnAST)
                    elif la1 and la1 in [ASSIGN]:
                        pass
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    tmp97_AST = None
                    tmp97_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp97_AST)
                    self.match(ASSIGN)
                    self.expr()
                    self.addASTChild(currentAST, self.returnAST)
                    substatement_AST = currentAST.root
                elif (_tokenSet_18.member(self.LA(1))) and (_tokenSet_19.member(self.LA(2))):
                    pass
                    self.expr()
                    self.addASTChild(currentAST, self.returnAST)
                    substatement_AST = currentAST.root
                else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_4)
            else:
                raise ex
        
        self.returnAST = substatement_AST
    
    def lhs(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        lhs_AST = None
        a = None
        a_AST = None
        b = None
        b_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LBRACK]:
                pass
                tmp98_AST = None
                tmp98_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp98_AST)
                self.match(LBRACK)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [NAME]:
                    pass
                    a = self.LT(1)
                    a_AST = self.astFactory.create(a)
                    self.addASTChild(currentAST, a_AST)
                    self.match(NAME)
                    if not self.inputState.guessing:
                        self.as_var(a_AST)
                    while True:
                        if (self.LA(1)==SPACE or self.LA(1)==COMMA):
                            pass
                            la1 = self.LA(1)
                            if False:
                                pass
                            elif la1 and la1 in [SPACE]:
                                pass
                                self.sp()
                                self.addASTChild(currentAST, self.returnAST)
                            elif la1 and la1 in [COMMA]:
                                pass
                                self.match(COMMA)
                                la1 = self.LA(1)
                                if False:
                                    pass
                                elif la1 and la1 in [SPACE]:
                                    pass
                                    self.sp()
                                    self.addASTChild(currentAST, self.returnAST)
                                elif la1 and la1 in [NAME]:
                                    pass
                                else:
                                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                                    
                            else:
                                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                                
                            b = self.LT(1)
                            b_AST = self.astFactory.create(b)
                            self.addASTChild(currentAST, b_AST)
                            self.match(NAME)
                            if not self.inputState.guessing:
                                self.as_var(b_AST)
                        else:
                            break
                        
                elif la1 and la1 in [RBRACK]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.match(RBRACK)
                lhs_AST = currentAST.root
            elif la1 and la1 in [NAME]:
                pass
                self.reference_lhs()
                self.addASTChild(currentAST, self.returnAST)
                while True:
                    if (self.LA(1)==DOT):
                        pass
                        tmp101_AST = None
                        tmp101_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp101_AST)
                        self.match(DOT)
                        if not self.inputState.guessing:
                            self.is_dot=True
                        self.reference_lhs()
                        self.addASTChild(currentAST, self.returnAST)
                        if not self.inputState.guessing:
                            self.is_dot=False
                    else:
                        break
                    
                lhs_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_20)
            else:
                raise ex
        
        self.returnAST = lhs_AST
    
    def reference_lhs(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        reference_lhs_AST = None
        c = None
        c_AST = None
        try:      ## for error handling
            pass
            c = self.LT(1)
            c_AST = self.astFactory.create(c)
            self.addASTChild(currentAST, c_AST)
            self.match(NAME)
            if not self.inputState.guessing:
                self.as_var(c_AST)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LBRACE]:
                pass
                self.brace_arglist()
                self.addASTChild(currentAST, self.returnAST)
                if not self.inputState.guessing:
                    reference_lhs_AST = currentAST.root
                    reference_lhs_AST = antlr.make(self.astFactory.create(BRACE_ARGS), reference_lhs_AST);
                    currentAST.root = reference_lhs_AST
                    if (reference_lhs_AST != None) and (reference_lhs_AST.getFirstChild() != None):
                        currentAST.child = reference_lhs_AST.getFirstChild()
                    else:
                        currentAST.child = reference_lhs_AST
                    currentAST.advanceChildToEnd()
            elif la1 and la1 in [DOT,SPACE,ASSIGN,LPAREN]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LPAREN]:
                pass
                self.paren_arglist()
                self.addASTChild(currentAST, self.returnAST)
                if not self.inputState.guessing:
                    reference_lhs_AST = currentAST.root
                    reference_lhs_AST = antlr.make(self.astFactory.create(PAREN_ARGS), reference_lhs_AST);
                    currentAST.root = reference_lhs_AST
                    if (reference_lhs_AST != None) and (reference_lhs_AST.getFirstChild() != None):
                        currentAST.child = reference_lhs_AST.getFirstChild()
                    else:
                        currentAST.child = reference_lhs_AST
                    currentAST.advanceChildToEnd()
            elif la1 and la1 in [DOT,SPACE,ASSIGN]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            reference_lhs_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_21)
            else:
                raise ex
        
        self.returnAST = reference_lhs_AST
    
    def brace_arglist(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        brace_arglist_AST = None
        try:      ## for error handling
            pass
            self.match(LBRACE)
            if not self.inputState.guessing:
                self.inside_args=True
                pgobble_space=self.gobble_space
                self.gobble_space=True
            self.arg_list()
            self.addASTChild(currentAST, self.returnAST)
            self.match(RBRACE)
            if not self.inputState.guessing:
                self.inside_args=False
                self.gobble_space=pgobble_space
            brace_arglist_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_22)
            else:
                raise ex
        
        self.returnAST = brace_arglist_AST
    
    def paren_arglist(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        paren_arglist_AST = None
        a = None
        a_AST = None
        try:      ## for error handling
            pass
            a = self.LT(1)
            a_AST = self.astFactory.create(a)
            self.match(LPAREN)
            if not self.inputState.guessing:
                self.inside_args=True
                pgobble_space=self.gobble_space
                self.gobble_space=True
            self.arg_list()
            self.addASTChild(currentAST, self.returnAST)
            self.match(RPAREN)
            if not self.inputState.guessing:
                self.inside_args=False
                self.gobble_space=pgobble_space
            paren_arglist_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_23)
            else:
                raise ex
        
        self.returnAST = paren_arglist_AST
    
    def arg_list(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        arg_list_AST = None
        a = None
        a_AST = None
        b = None
        b_AST = None
        try:      ## for error handling
            pass
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,ATPAREN,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                pass
                self.expr()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [COLON]:
                pass
                a = self.LT(1)
                a_AST = self.astFactory.create(a)
                self.addASTChild(currentAST, a_AST)
                self.match(COLON)
                if not self.inputState.guessing:
                    a_AST.setType(ALLELEMENTS)
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            while True:
                if (self.LA(1)==COMMA):
                    pass
                    self.match(COMMA)
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,ATPAREN,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                        pass
                        self.expr()
                        self.addASTChild(currentAST, self.returnAST)
                    elif la1 and la1 in [COLON]:
                        pass
                        b = self.LT(1)
                        b_AST = self.astFactory.create(b)
                        self.addASTChild(currentAST, b_AST)
                        self.match(COLON)
                        if not self.inputState.guessing:
                            b_AST.setType(ALLELEMENTS)
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                else:
                    break
                
            arg_list_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_24)
            else:
                raise ex
        
        self.returnAST = arg_list_AST
    
    def expr_1(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_1_AST = None
        try:      ## for error handling
            pass
            self.expr_2()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==OROR):
                    pass
                    tmp106_AST = None
                    tmp106_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp106_AST)
                    self.match(OROR)
                    self.expr_2()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            expr_1_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_25)
            else:
                raise ex
        
        self.returnAST = expr_1_AST
    
    def expr_at(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_at_AST = None
        a = None
        a_AST = None
        b = None
        b_AST = None
        try:      ## for error handling
            pass
            tmp107_AST = None
            tmp107_AST = self.astFactory.create(self.LT(1))
            self.makeASTRoot(currentAST, tmp107_AST)
            self.match(ATPAREN)
            a = self.LT(1)
            a_AST = self.astFactory.create(a)
            self.addASTChild(currentAST, a_AST)
            self.match(NAME)
            if not self.inputState.guessing:
                self.as_var(a_AST)
            while True:
                if (self.LA(1)==COMMA):
                    pass
                    self.match(COMMA)
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [SPACE]:
                        pass
                        self.sp()
                        self.addASTChild(currentAST, self.returnAST)
                    elif la1 and la1 in [NAME]:
                        pass
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    b = self.LT(1)
                    b_AST = self.astFactory.create(b)
                    self.addASTChild(currentAST, b_AST)
                    self.match(NAME)
                    if not self.inputState.guessing:
                        self.as_var(b_AST)
                else:
                    break
                
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [SPACE]:
                pass
                self.sp()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [RPAREN]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            self.match(RPAREN)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [SPACE]:
                pass
                self.sp()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            expr_at_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_26)
            else:
                raise ex
        
        self.returnAST = expr_at_AST
    
    def expr_2(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_2_AST = None
        try:      ## for error handling
            pass
            self.expr_3()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==ANDAND):
                    pass
                    tmp110_AST = None
                    tmp110_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp110_AST)
                    self.match(ANDAND)
                    self.expr_3()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            expr_2_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_27)
            else:
                raise ex
        
        self.returnAST = expr_2_AST
    
    def expr_3(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_3_AST = None
        try:      ## for error handling
            pass
            self.expr_4()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==OR):
                    pass
                    tmp111_AST = None
                    tmp111_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp111_AST)
                    self.match(OR)
                    self.expr_4()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            expr_3_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_28)
            else:
                raise ex
        
        self.returnAST = expr_3_AST
    
    def expr_4(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_4_AST = None
        try:      ## for error handling
            pass
            self.expr_5()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==AND):
                    pass
                    tmp112_AST = None
                    tmp112_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp112_AST)
                    self.match(AND)
                    self.expr_5()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            expr_4_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_29)
            else:
                raise ex
        
        self.returnAST = expr_4_AST
    
    def expr_5(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_5_AST = None
        try:      ## for error handling
            pass
            self.expr_6()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if ((self.LA(1) >= EQUAL and self.LA(1) <= GREATER_OR_EQUAL)):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [EQUAL]:
                        pass
                        tmp113_AST = None
                        tmp113_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp113_AST)
                        self.match(EQUAL)
                    elif la1 and la1 in [NOT_EQUAL]:
                        pass
                        tmp114_AST = None
                        tmp114_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp114_AST)
                        self.match(NOT_EQUAL)
                    elif la1 and la1 in [LESS_THAN]:
                        pass
                        tmp115_AST = None
                        tmp115_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp115_AST)
                        self.match(LESS_THAN)
                    elif la1 and la1 in [LESS_OR_EQUAL]:
                        pass
                        tmp116_AST = None
                        tmp116_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp116_AST)
                        self.match(LESS_OR_EQUAL)
                    elif la1 and la1 in [GREATER_THAN]:
                        pass
                        tmp117_AST = None
                        tmp117_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp117_AST)
                        self.match(GREATER_THAN)
                    elif la1 and la1 in [GREATER_OR_EQUAL]:
                        pass
                        tmp118_AST = None
                        tmp118_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp118_AST)
                        self.match(GREATER_OR_EQUAL)
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    self.expr_6()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            expr_5_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_30)
            else:
                raise ex
        
        self.returnAST = expr_5_AST
    
    def expr_6(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_6_AST = None
        try:      ## for error handling
            pass
            self.expr_7()
            self.addASTChild(currentAST, self.returnAST)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [COLON]:
                pass
                tmp119_AST = None
                tmp119_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp119_AST)
                self.match(COLON)
                self.expr_7()
                self.addASTChild(currentAST, self.returnAST)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [COLON]:
                    pass
                    self.match(COLON)
                    self.expr_7()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [SPACE,COMMENT,NEWLINE,COMMA,RBRACK,RPAREN,SEMI,RBRACE,OROR,ANDAND,OR,AND,EQUAL,NOT_EQUAL,LESS_THAN,LESS_OR_EQUAL,GREATER_THAN,GREATER_OR_EQUAL]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
            elif la1 and la1 in [SPACE,COMMENT,NEWLINE,COMMA,RBRACK,RPAREN,SEMI,RBRACE,OROR,ANDAND,OR,AND,EQUAL,NOT_EQUAL,LESS_THAN,LESS_OR_EQUAL,GREATER_THAN,GREATER_OR_EQUAL]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            expr_6_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_31)
            else:
                raise ex
        
        self.returnAST = expr_6_AST
    
    def expr_7(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_7_AST = None
        try:      ## for error handling
            pass
            self.expr_8()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==PLUS or self.LA(1)==MINUS):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [PLUS]:
                        pass
                        tmp121_AST = None
                        tmp121_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp121_AST)
                        self.match(PLUS)
                    elif la1 and la1 in [MINUS]:
                        pass
                        tmp122_AST = None
                        tmp122_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp122_AST)
                        self.match(MINUS)
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    self.expr_8()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            expr_7_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_32)
            else:
                raise ex
        
        self.returnAST = expr_7_AST
    
    def expr_8(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_8_AST = None
        try:      ## for error handling
            pass
            self.expr_9()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if ((self.LA(1) >= STAR and self.LA(1) <= DOTBACKDIV)):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [STAR]:
                        pass
                        tmp123_AST = None
                        tmp123_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp123_AST)
                        self.match(STAR)
                    elif la1 and la1 in [DIV]:
                        pass
                        tmp124_AST = None
                        tmp124_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp124_AST)
                        self.match(DIV)
                    elif la1 and la1 in [BACKDIV]:
                        pass
                        tmp125_AST = None
                        tmp125_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp125_AST)
                        self.match(BACKDIV)
                    elif la1 and la1 in [DOTSTAR]:
                        pass
                        tmp126_AST = None
                        tmp126_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp126_AST)
                        self.match(DOTSTAR)
                    elif la1 and la1 in [DOTDIV]:
                        pass
                        tmp127_AST = None
                        tmp127_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp127_AST)
                        self.match(DOTDIV)
                    elif la1 and la1 in [DOTBACKDIV]:
                        pass
                        tmp128_AST = None
                        tmp128_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp128_AST)
                        self.match(DOTBACKDIV)
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    self.expr_9()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            expr_8_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_33)
            else:
                raise ex
        
        self.returnAST = expr_8_AST
    
    def expr_9(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_9_AST = None
        p = None
        p_AST = None
        m = None
        m_AST = None
        try:      ## for error handling
            pass
            while True:
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [NOT]:
                    pass
                    tmp129_AST = None
                    tmp129_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp129_AST)
                    self.match(NOT)
                elif la1 and la1 in [PLUS]:
                    pass
                    p = self.LT(1)
                    p_AST = self.astFactory.create(p)
                    self.makeASTRoot(currentAST, p_AST)
                    self.match(PLUS)
                    if not self.inputState.guessing:
                        p_AST.setType(SIGN_PLUS)
                elif la1 and la1 in [MINUS]:
                    pass
                    m = self.LT(1)
                    m_AST = self.astFactory.create(m)
                    self.makeASTRoot(currentAST, m_AST)
                    self.match(MINUS)
                    if not self.inputState.guessing:
                        m_AST.setType(SIGN_MINUS)
                else:
                        break
                    
            self.expr_10()
            self.addASTChild(currentAST, self.returnAST)
            expr_9_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_34)
            else:
                raise ex
        
        self.returnAST = expr_9_AST
    
    def expr_10(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_10_AST = None
        try:      ## for error handling
            pass
            self.expr_11()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==EXP or self.LA(1)==DOTEXP):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [EXP]:
                        pass
                        tmp130_AST = None
                        tmp130_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp130_AST)
                        self.match(EXP)
                    elif la1 and la1 in [DOTEXP]:
                        pass
                        tmp131_AST = None
                        tmp131_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp131_AST)
                        self.match(DOTEXP)
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    self.expr_11()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            expr_10_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_34)
            else:
                raise ex
        
        self.returnAST = expr_10_AST
    
    def expr_11(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_11_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [AT]:
                pass
                tmp132_AST = None
                tmp132_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp132_AST)
                self.match(AT)
                tmp133_AST = None
                tmp133_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp133_AST)
                self.match(NAME)
                expr_11_AST = currentAST.root
            elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,NUMBER,INT,MATCHVAR,STRING]:
                pass
                self.expr_11a()
                self.addASTChild(currentAST, self.returnAST)
                expr_11_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_35)
            else:
                raise ex
        
        self.returnAST = expr_11_AST
    
    def expr_11a(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_11a_AST = None
        try:      ## for error handling
            pass
            self.expr_12()
            self.addASTChild(currentAST, self.returnAST)
            if ((self.LA(1)==SPACE) and (_tokenSet_36.member(self.LA(2))) and (self.gobble_space)):
                pass
                self.match(SPACE)
            elif (_tokenSet_36.member(self.LA(1))) and (_tokenSet_37.member(self.LA(2))):
                pass
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [TRANS]:
                pass
                tmp135_AST = None
                tmp135_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp135_AST)
                self.match(TRANS)
            elif la1 and la1 in [DOTTRANS]:
                pass
                tmp136_AST = None
                tmp136_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp136_AST)
                self.match(DOTTRANS)
            elif la1 and la1 in [SPACE,COMMENT,NEWLINE,COMMA,RBRACK,RPAREN,SEMI,RBRACE,COLON,OROR,ANDAND,OR,AND,EQUAL,NOT_EQUAL,LESS_THAN,LESS_OR_EQUAL,GREATER_THAN,GREATER_OR_EQUAL,PLUS,MINUS,STAR,DIV,BACKDIV,DOTSTAR,DOTDIV,DOTBACKDIV,EXP,DOTEXP]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            expr_11a_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_35)
            else:
                raise ex
        
        self.returnAST = expr_11a_AST
    
    def expr_12(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_12_AST = None
        b = None
        b_AST = None
        c = None
        c_AST = None
        d = None
        d_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [NUMBER]:
                pass
                tmp137_AST = None
                tmp137_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp137_AST)
                self.match(NUMBER)
                expr_12_AST = currentAST.root
            elif la1 and la1 in [INT]:
                pass
                tmp138_AST = None
                tmp138_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp138_AST)
                self.match(INT)
                expr_12_AST = currentAST.root
            elif la1 and la1 in [FLOAT]:
                pass
                tmp139_AST = None
                tmp139_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp139_AST)
                self.match(FLOAT)
                expr_12_AST = currentAST.root
            elif la1 and la1 in [COMPLEX]:
                pass
                tmp140_AST = None
                tmp140_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp140_AST)
                self.match(COMPLEX)
                expr_12_AST = currentAST.root
            elif la1 and la1 in [NAME]:
                pass
                self.reference()
                self.addASTChild(currentAST, self.returnAST)
                while True:
                    if (self.LA(1)==DOT):
                        pass
                        tmp141_AST = None
                        tmp141_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp141_AST)
                        self.match(DOT)
                        if not self.inputState.guessing:
                            self.is_dot=True
                        self.reference()
                        self.addASTChild(currentAST, self.returnAST)
                        if not self.inputState.guessing:
                            self.is_dot=False
                    else:
                        break
                    
                expr_12_AST = currentAST.root
            elif la1 and la1 in [MATCHVAR]:
                pass
                tmp142_AST = None
                tmp142_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp142_AST)
                self.match(MATCHVAR)
                expr_12_AST = currentAST.root
            elif la1 and la1 in [ASSERT]:
                pass
                tmp143_AST = None
                tmp143_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp143_AST)
                self.match(ASSERT)
                self.match(LPAREN)
                if not self.inputState.guessing:
                    pgobble_space=self.gobble_space
                    self.gobble_space=True # disable automatic space skipping
                self.expr()
                self.addASTChild(currentAST, self.returnAST)
                self.match(COMMA)
                self.expr()
                self.addASTChild(currentAST, self.returnAST)
                self.match(RPAREN)
                if not self.inputState.guessing:
                    self.gobble_space=pgobble_space
                expr_12_AST = currentAST.root
            elif la1 and la1 in [STRING]:
                pass
                b = self.LT(1)
                b_AST = self.astFactory.create(b)
                self.addASTChild(currentAST, b_AST)
                self.match(STRING)
                expr_12_AST = currentAST.root
            elif la1 and la1 in [LPAREN]:
                pass
                self.match(LPAREN)
                if not self.inputState.guessing:
                    pgobble_space=self.gobble_space
                    self.gobble_space=True # disable automatic space skipping
                self.expr()
                self.addASTChild(currentAST, self.returnAST)
                self.match(RPAREN)
                if not self.inputState.guessing:
                    self.gobble_space=pgobble_space
                expr_12_AST = currentAST.root
            elif la1 and la1 in [LBRACK]:
                pass
                c = self.LT(1)
                c_AST = self.astFactory.create(c)
                self.makeASTRoot(currentAST, c_AST)
                self.match(LBRACK)
                if not self.inputState.guessing:
                    c_AST.setType(MATRIX)
                    pgobble_space=self.gobble_space 
                    self.gobble_space=False # disable automatic space skipping
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                    pass
                    self.semiblock()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [RBRACK]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.match(RBRACK)
                if not self.inputState.guessing:
                    self.gobble_space=pgobble_space
                expr_12_AST = currentAST.root
            elif la1 and la1 in [ARRAY_END]:
                pass
                tmp150_AST = None
                tmp150_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp150_AST)
                self.match(ARRAY_END)
                expr_12_AST = currentAST.root
            elif la1 and la1 in [LBRACE]:
                pass
                d = self.LT(1)
                d_AST = self.astFactory.create(d)
                self.makeASTRoot(currentAST, d_AST)
                self.match(LBRACE)
                if not self.inputState.guessing:
                    d_AST.setType(CELL)
                    pgobble_space=self.gobble_space # disable automatic space skipping
                    self.gobble_space=False
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                    pass
                    self.semiblock()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [RBRACE]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.match(RBRACE)
                if not self.inputState.guessing:
                    self.gobble_space=pgobble_space
                expr_12_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_36)
            else:
                raise ex
        
        self.returnAST = expr_12_AST
    
    def reference(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        reference_AST = None
        a = None
        a_AST = None
        try:      ## for error handling
            pass
            a = self.LT(1)
            a_AST = self.astFactory.create(a)
            self.addASTChild(currentAST, a_AST)
            self.match(NAME)
            if not self.inputState.guessing:
                self.var_lookup(a_AST)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LBRACE]:
                pass
                self.brace_arglist()
                self.addASTChild(currentAST, self.returnAST)
                if not self.inputState.guessing:
                    reference_AST = currentAST.root
                    reference_AST = antlr.make(self.astFactory.create(BRACE_ARGS), reference_AST);
                    currentAST.root = reference_AST
                    if (reference_AST != None) and (reference_AST.getFirstChild() != None):
                        currentAST.child = reference_AST.getFirstChild()
                    else:
                        currentAST.child = reference_AST
                    currentAST.advanceChildToEnd()
            elif la1 and la1 in [DOT,TRANS,SPACE,COMMENT,NEWLINE,COMMA,RBRACK,LPAREN,RPAREN,SEMI,RBRACE,COLON,OROR,ANDAND,OR,AND,EQUAL,NOT_EQUAL,LESS_THAN,LESS_OR_EQUAL,GREATER_THAN,GREATER_OR_EQUAL,PLUS,MINUS,STAR,DIV,BACKDIV,DOTSTAR,DOTDIV,DOTBACKDIV,EXP,DOTEXP,DOTTRANS]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LPAREN]:
                pass
                self.paren_arglist()
                self.addASTChild(currentAST, self.returnAST)
                if not self.inputState.guessing:
                    reference_AST = currentAST.root
                    reference_AST = antlr.make(self.astFactory.create(PAREN_ARGS), reference_AST);
                    currentAST.root = reference_AST
                    if (reference_AST != None) and (reference_AST.getFirstChild() != None):
                        currentAST.child = reference_AST.getFirstChild()
                    else:
                        currentAST.child = reference_AST
                    currentAST.advanceChildToEnd()
            elif la1 and la1 in [DOT,TRANS,SPACE,COMMENT,NEWLINE,COMMA,RBRACK,RPAREN,SEMI,RBRACE,COLON,OROR,ANDAND,OR,AND,EQUAL,NOT_EQUAL,LESS_THAN,LESS_OR_EQUAL,GREATER_THAN,GREATER_OR_EQUAL,PLUS,MINUS,STAR,DIV,BACKDIV,DOTSTAR,DOTDIV,DOTBACKDIV,EXP,DOTEXP,DOTTRANS]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            reference_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_38)
            else:
                raise ex
        
        self.returnAST = reference_AST
    
    def semiblock(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        semiblock_AST = None
        try:      ## for error handling
            pass
            if not self.inputState.guessing:
                g=False
            self.commablock()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==NEWLINE or self.LA(1)==SEMI):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [NEWLINE]:
                        pass
                        _cnt185= 0
                        while True:
                            if (self.LA(1)==NEWLINE):
                                pass
                                self.match(NEWLINE)
                            else:
                                break
                            
                            _cnt185 += 1
                        if _cnt185 < 1:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    elif la1 and la1 in [SEMI]:
                        pass
                        self.match(SEMI)
                        while True:
                            if (self.LA(1)==NEWLINE):
                                pass
                                self.match(NEWLINE)
                            else:
                                break
                            
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    self.commablock()
                    self.addASTChild(currentAST, self.returnAST)
                    if not self.inputState.guessing:
                        g=True
                else:
                    break
                
            if not self.inputState.guessing:
                semiblock_AST = currentAST.root
                if g: semiblock_AST = antlr.make(self.astFactory.create(ROWJOIN), semiblock_AST);
                currentAST.root = semiblock_AST
                if (semiblock_AST != None) and (semiblock_AST.getFirstChild() != None):
                    currentAST.child = semiblock_AST.getFirstChild()
                else:
                    currentAST.child = semiblock_AST
                currentAST.advanceChildToEnd()
            semiblock_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_39)
            else:
                raise ex
        
        self.returnAST = semiblock_AST
    
    def commablock(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        commablock_AST = None
        try:      ## for error handling
            pass
            self.expr_1()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==SPACE or self.LA(1)==COMMA):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [SPACE]:
                        pass
                        pass
                        self.match(SPACE)
                    elif la1 and la1 in [COMMA]:
                        pass
                        self.match(COMMA)
                        la1 = self.LA(1)
                        if False:
                            pass
                        elif la1 and la1 in [SPACE]:
                            pass
                            self.sp()
                            self.addASTChild(currentAST, self.returnAST)
                        elif la1 and la1 in [ARRAY_END,FLOAT,COMPLEX,ASSERT,LBRACK,NAME,LPAREN,LBRACE,PLUS,MINUS,NOT,AT,NUMBER,INT,MATCHVAR,STRING]:
                            pass
                        else:
                                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                            
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    self.expr_1()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            if not self.inputState.guessing:
                commablock_AST = currentAST.root
                commablock_AST = antlr.make(self.astFactory.create(COLUMNJOIN), commablock_AST);
                currentAST.root = commablock_AST
                if (commablock_AST != None) and (commablock_AST.getFirstChild() != None):
                    currentAST.child = commablock_AST.getFirstChild()
                else:
                    currentAST.child = commablock_AST
                currentAST.advanceChildToEnd()
            commablock_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_40)
            else:
                raise ex
        
        self.returnAST = commablock_AST
    
    
    def buildTokenTypeASTClassMap(self):
        self.tokenTypeToASTClassMap = None

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
    data = [ -7493464748105924608L, 128191488L, 0L, 0L]
    return data
_tokenSet_0 = antlr.BitSet(mk_tokenSet_0())

### generate bit set
def mk_tokenSet_1(): 
    ### var1
    data = [ 2L, 0L]
    return data
_tokenSet_1 = antlr.BitSet(mk_tokenSet_1())

### generate bit set
def mk_tokenSet_2(): 
    ### var1
    data = [ 114624087195648L, 0L]
    return data
_tokenSet_2 = antlr.BitSet(mk_tokenSet_2())

### generate bit set
def mk_tokenSet_3(): 
    ### var1
    data = [ 576620731245264896L, 0L]
    return data
_tokenSet_3 = antlr.BitSet(mk_tokenSet_3())

### generate bit set
def mk_tokenSet_4(): 
    ### var1
    data = [ 576479993756909568L, 0L]
    return data
_tokenSet_4 = antlr.BitSet(mk_tokenSet_4())

### generate bit set
def mk_tokenSet_5(): 
    ### var1
    data = [ 2199023255554L, 0L]
    return data
_tokenSet_5 = antlr.BitSet(mk_tokenSet_5())

### generate bit set
def mk_tokenSet_6(): 
    ### var1
    data = [ -8052844844969885696L, 128191488L, 0L, 0L]
    return data
_tokenSet_6 = antlr.BitSet(mk_tokenSet_6())

### generate bit set
def mk_tokenSet_7(): 
    ### var1
    data = [ 558448552817328130L, 0L]
    return data
_tokenSet_7 = antlr.BitSet(mk_tokenSet_7())

### generate bit set
def mk_tokenSet_8(): 
    ### var1
    data = [ 8796093022208L, 0L]
    return data
_tokenSet_8 = antlr.BitSet(mk_tokenSet_8())

### generate bit set
def mk_tokenSet_9(): 
    ### var1
    data = [ -6917916298395647998L, 128191488L, 0L, 0L]
    return data
_tokenSet_9 = antlr.BitSet(mk_tokenSet_9())

### generate bit set
def mk_tokenSet_10(): 
    ### var1
    data = [ 576488789849931776L, 0L]
    return data
_tokenSet_10 = antlr.BitSet(mk_tokenSet_10())

### generate bit set
def mk_tokenSet_11(): 
    ### var1
    data = [ -8070296585583722496L, 128191488L, 0L, 0L]
    return data
_tokenSet_11 = antlr.BitSet(mk_tokenSet_11())

### generate bit set
def mk_tokenSet_12(): 
    ### var1
    data = [ -576181736128102400L, 134217727L, 0L, 0L]
    return data
_tokenSet_12 = antlr.BitSet(mk_tokenSet_12())

### generate bit set
def mk_tokenSet_13(): 
    ### var1
    data = [ 2882604752825221120L, 0L]
    return data
_tokenSet_13 = antlr.BitSet(mk_tokenSet_13())

### generate bit set
def mk_tokenSet_14(): 
    ### var1
    data = [ 360287970189770752L, 0L]
    return data
_tokenSet_14 = antlr.BitSet(mk_tokenSet_14())

### generate bit set
def mk_tokenSet_15(): 
    ### var1
    data = [ 131072L, 0L]
    return data
_tokenSet_15 = antlr.BitSet(mk_tokenSet_15())

### generate bit set
def mk_tokenSet_16(): 
    ### var1
    data = [ 180143985094950912L, 0L]
    return data
_tokenSet_16 = antlr.BitSet(mk_tokenSet_16())

### generate bit set
def mk_tokenSet_17(): 
    ### var1
    data = [ 1153176866182414336L, 0L]
    return data
_tokenSet_17 = antlr.BitSet(mk_tokenSet_17())

### generate bit set
def mk_tokenSet_18(): 
    ### var1
    data = [ -8070296585587392512L, 128191488L, 0L, 0L]
    return data
_tokenSet_18 = antlr.BitSet(mk_tokenSet_18())

### generate bit set
def mk_tokenSet_19(): 
    ### var1
    data = [ -576252104872280064L, 134217727L, 0L, 0L]
    return data
_tokenSet_19 = antlr.BitSet(mk_tokenSet_19())

### generate bit set
def mk_tokenSet_20(): 
    ### var1
    data = [ 70643622084608L, 0L]
    return data
_tokenSet_20 = antlr.BitSet(mk_tokenSet_20())

### generate bit set
def mk_tokenSet_21(): 
    ### var1
    data = [ 70643622100992L, 0L]
    return data
_tokenSet_21 = antlr.BitSet(mk_tokenSet_21())

### generate bit set
def mk_tokenSet_22(): 
    ### var1
    data = [ 7494537061924356096L, 6029311L, 0L, 0L]
    return data
_tokenSet_22 = antlr.BitSet(mk_tokenSet_22())

### generate bit set
def mk_tokenSet_23(): 
    ### var1
    data = [ 7494396324436000768L, 6029311L, 0L, 0L]
    return data
_tokenSet_23 = antlr.BitSet(mk_tokenSet_23())

### generate bit set
def mk_tokenSet_24(): 
    ### var1
    data = [ 2306124484190404608L, 0L]
    return data
_tokenSet_24 = antlr.BitSet(mk_tokenSet_24())

### generate bit set
def mk_tokenSet_25(): 
    ### var1
    data = [ 2882639937197309952L, 0L]
    return data
_tokenSet_25 = antlr.BitSet(mk_tokenSet_25())

### generate bit set
def mk_tokenSet_26(): 
    ### var1
    data = [ 1153075451267383296L, 128191488L, 0L, 0L]
    return data
_tokenSet_26 = antlr.BitSet(mk_tokenSet_26())

### generate bit set
def mk_tokenSet_27(): 
    ### var1
    data = [ 2882639937197309952L, 1L, 0L, 0L]
    return data
_tokenSet_27 = antlr.BitSet(mk_tokenSet_27())

### generate bit set
def mk_tokenSet_28(): 
    ### var1
    data = [ 2882639937197309952L, 3L, 0L, 0L]
    return data
_tokenSet_28 = antlr.BitSet(mk_tokenSet_28())

### generate bit set
def mk_tokenSet_29(): 
    ### var1
    data = [ 2882639937197309952L, 7L, 0L, 0L]
    return data
_tokenSet_29 = antlr.BitSet(mk_tokenSet_29())

### generate bit set
def mk_tokenSet_30(): 
    ### var1
    data = [ 2882639937197309952L, 15L, 0L, 0L]
    return data
_tokenSet_30 = antlr.BitSet(mk_tokenSet_30())

### generate bit set
def mk_tokenSet_31(): 
    ### var1
    data = [ 2882639937197309952L, 1023L, 0L, 0L]
    return data
_tokenSet_31 = antlr.BitSet(mk_tokenSet_31())

### generate bit set
def mk_tokenSet_32(): 
    ### var1
    data = [ 7494325955624697856L, 1023L, 0L, 0L]
    return data
_tokenSet_32 = antlr.BitSet(mk_tokenSet_32())

### generate bit set
def mk_tokenSet_33(): 
    ### var1
    data = [ 7494325955624697856L, 4095L, 0L, 0L]
    return data
_tokenSet_33 = antlr.BitSet(mk_tokenSet_33())

### generate bit set
def mk_tokenSet_34(): 
    ### var1
    data = [ 7494325955624697856L, 262143L, 0L, 0L]
    return data
_tokenSet_34 = antlr.BitSet(mk_tokenSet_34())

### generate bit set
def mk_tokenSet_35(): 
    ### var1
    data = [ 7494325955624697856L, 1835007L, 0L, 0L]
    return data
_tokenSet_35 = antlr.BitSet(mk_tokenSet_35())

### generate bit set
def mk_tokenSet_36(): 
    ### var1
    data = [ 7494325955691806720L, 6029311L, 0L, 0L]
    return data
_tokenSet_36 = antlr.BitSet(mk_tokenSet_36())

### generate bit set
def mk_tokenSet_37(): 
    ### var1
    data = [ -242594463742L, 134217727L, 0L, 0L]
    return data
_tokenSet_37 = antlr.BitSet(mk_tokenSet_37())

### generate bit set
def mk_tokenSet_38(): 
    ### var1
    data = [ 7494325955691823104L, 6029311L, 0L, 0L]
    return data
_tokenSet_38 = antlr.BitSet(mk_tokenSet_38())

### generate bit set
def mk_tokenSet_39(): 
    ### var1
    data = [ 2305878193585782784L, 0L]
    return data
_tokenSet_39 = antlr.BitSet(mk_tokenSet_39())

### generate bit set
def mk_tokenSet_40(): 
    ### var1
    data = [ 2882340045400834048L, 0L]
    return data
_tokenSet_40 = antlr.BitSet(mk_tokenSet_40())
    
