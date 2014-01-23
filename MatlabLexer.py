### $ANTLR 2.7.6 (20071205): "mat2py.g" -> "MatlabLexer.py"$
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
### preamble action >>> 

### preamble action <<< 
### >>>The Literals<<<
literals = {}
literals[u"switch"] = 53
literals[u"case"] = 55
literals[u"for"] = 51
literals[u"try"] = 52
literals[u"global"] = 34
literals[u"continue"] = 20
literals[u"function"] = 41
literals[u"elseif"] = 56
literals[u"while"] = 50
literals[u"break"] = 19
literals[u"return"] = 21
literals[u"assert"] = 33
literals[u"if"] = 49
literals[u"otherwise"] = 57
literals[u"else"] = 58
literals[u"catch"] = 54


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

class Lexer(antlr.CharScanner) :
    ### user action >>>
    ### user action <<<
    def __init__(self, *argv, **kwargs) :
        antlr.CharScanner.__init__(self, *argv, **kwargs)
        self.caseSensitiveLiterals = True
        self.setCaseSensitive(True)
        self.literals = literals
        ### __init__ header action >>> 
        # gets inserted in the __init__ method of each of the generated Python
        # classes
        #
        self.paren_count=0
        self.brack_count=0
        self.string_ok=True
        self.gobble_space=True
        ### __init__ header action <<< 
    
    def nextToken(self):
        while True:
            try: ### try again ..
                while True:
                    _token = None
                    _ttype = INVALID_TYPE
                    self.resetText()
                    try: ## for char stream error handling
                        try: ##for lexical error handling
                            la1 = self.LA(1)
                            if False:
                                pass
                            elif la1 and la1 in u'\'':
                                pass
                                self.mSTRING(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'%':
                                pass
                                self.mCOMMENT(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'\t ':
                                pass
                                self.mSPACE(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'\n\r':
                                pass
                                self.mNEWLINE(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz':
                                pass
                                self.mNAME(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'?':
                                pass
                                self.mMATCH(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'\\':
                                pass
                                self.mBACKDIV(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u':':
                                pass
                                self.mCOLON(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u',':
                                pass
                                self.mCOMMA(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'/':
                                pass
                                self.mDIV(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'^':
                                pass
                                self.mEXP(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'[':
                                pass
                                self.mLBRACK(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'{':
                                pass
                                self.mLBRACE(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'(':
                                pass
                                self.mLPAREN(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'-':
                                pass
                                self.mMINUS(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'+':
                                pass
                                self.mPLUS(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u']':
                                pass
                                self.mRBRACK(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'}':
                                pass
                                self.mRBRACE(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u')':
                                pass
                                self.mRPAREN(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u';':
                                pass
                                self.mSEMI(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'*':
                                pass
                                self.mSTAR(True)
                                theRetToken = self._returnToken
                            else:
                                if (self.LA(1)==u'@') and (self.LA(2)==u'('):
                                    pass
                                    self.mATPAREN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'&') and (self.LA(2)==u'&'):
                                    pass
                                    self.mANDAND(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'.') and (self.LA(2)==u'\''):
                                    pass
                                    self.mDOTTRANS(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'.') and (self.LA(2)==u'\\'):
                                    pass
                                    self.mDOTBACKDIV(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'.') and (self.LA(2)==u'/'):
                                    pass
                                    self.mDOTDIV(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'.') and (self.LA(2)==u'^'):
                                    pass
                                    self.mDOTEXP(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'.') and (self.LA(2)==u'*'):
                                    pass
                                    self.mDOTSTAR(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'=') and (self.LA(2)==u'='):
                                    pass
                                    self.mEQUAL(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'>') and (self.LA(2)==u'='):
                                    pass
                                    self.mGREATER_OR_EQUAL(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'<') and (self.LA(2)==u'='):
                                    pass
                                    self.mLESS_OR_EQUAL(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'|') and (self.LA(2)==u'|'):
                                    pass
                                    self.mOROR(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'~') and (self.LA(2)==u'='):
                                    pass
                                    self.mNOT_EQUAL(True)
                                    theRetToken = self._returnToken
                                elif (_tokenSet_0.member(self.LA(1))) and (True):
                                    pass
                                    self.mNUMBER(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'&') and (True):
                                    pass
                                    self.mAND(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'=') and (True):
                                    pass
                                    self.mASSIGN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'@') and (True):
                                    pass
                                    self.mAT(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'>') and (True):
                                    pass
                                    self.mGREATER_THAN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'<') and (True):
                                    pass
                                    self.mLESS_THAN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'~') and (True):
                                    pass
                                    self.mNOT(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'|') and (True):
                                    pass
                                    self.mOR(True)
                                    theRetToken = self._returnToken
                                else:
                                    self.default(self.LA(1))
                                
                            if not self._returnToken:
                                raise antlr.TryAgain ### found SKIP token
                            ### option { testLiterals=true } 
                            self.testForLiteral(self._returnToken)
                            ### return token to caller
                            return self._returnToken
                        ### handle lexical errors ....
                        except antlr.RecognitionException, e:
                            raise antlr.TokenStreamRecognitionException(e)
                    ### handle char stream errors ...
                    except antlr.CharStreamException,cse:
                        if isinstance(cse, antlr.CharStreamIOException):
                            raise antlr.TokenStreamIOException(cse.io)
                        else:
                            raise antlr.TokenStreamException(str(cse))
            except antlr.TryAgain:
                pass
        
    def mSTRING(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = STRING
        _saveIndex = 0
        if ((self.LA(1)==u'\'') and (_tokenSet_1.member(self.LA(2))) and (self.string_ok)):
            pass
            self.match('\'')
            while True:
                if (self.LA(1)==u'\'') and (self.LA(2)==u'\''):
                    pass
                    self.match('\'')
                    self.match('\'')
                elif (_tokenSet_2.member(self.LA(1))):
                    pass
                    self.match(_tokenSet_2)
                else:
                    break
                
            self.match('\'')
            if not self.inputState.guessing:
                self.string_ok=False
        elif (self.LA(1)==u'\'') and (True):
            pass
            self.match('\'')
            if not self.inputState.guessing:
                _ttype = TRANS;
            if not self.inputState.guessing:
                _ttype = TRANS;
        else:
            self.raise_NoViableAlt(self.LA(1))
        
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mCOMMENT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = COMMENT
        _saveIndex = 0
        pass
        self.match('%')
        while True:
            if (_tokenSet_3.member(self.LA(1))):
                pass
                self.match(_tokenSet_3)
            else:
                break
            
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mSPACE(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = SPACE
        _saveIndex = 0
        pass
        _cnt206= 0
        while True:
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in u' ':
                pass
                self.match(' ')
            elif la1 and la1 in u'\t':
                pass
                self.match('\t')
            else:
                    break
                
            _cnt206 += 1
        if _cnt206 < 1:
            self.raise_NoViableAlt(self.LA(1))
        if not self.inputState.guessing:
            if self.brack_count<=0: _ttype = Token.SKIP;
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mNUMBER(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = NUMBER
        _saveIndex = 0
        synPredMatched218 = False
        if (self.LA(1)==u'.') and ((self.LA(2) >= u'0' and self.LA(2) <= u'9')):
            _m218 = self.mark()
            synPredMatched218 = True
            self.inputState.guessing += 1
            try:
                pass
                self.match('.')
                self.mDIGIT(False)
            except antlr.RecognitionException, pe:
                synPredMatched218 = False
            self.rewind(_m218)
            self.inputState.guessing -= 1
        if synPredMatched218:
            pass
            self.match('.')
            _cnt220= 0
            while True:
                if ((self.LA(1) >= u'0' and self.LA(1) <= u'9')):
                    pass
                    self.mDIGIT(False)
                else:
                    break
                
                _cnt220 += 1
            if _cnt220 < 1:
                self.raise_NoViableAlt(self.LA(1))
            if (self.LA(1)==u'E' or self.LA(1)==u'e'):
                pass
                self.mExponent(False)
            else: ## <m4>
                    pass
                
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in u'i':
                pass
                self.match('i')
            elif la1 and la1 in u'I':
                pass
                self.match('I')
            elif la1 and la1 in u'j':
                pass
                self.match('j')
            elif la1 and la1 in u'J':
                pass
                self.match('J')
            else:
                ##<m3> <closing
                    pass
                
            if not self.inputState.guessing:
                self.string_ok=False
        else:
            synPredMatched224 = False
            if (self.LA(1)==u'.') and (self.LA(2)==u'.'):
                _m224 = self.mark()
                synPredMatched224 = True
                self.inputState.guessing += 1
                try:
                    pass
                    self.match('.')
                    self.match('.')
                except antlr.RecognitionException, pe:
                    synPredMatched224 = False
                self.rewind(_m224)
                self.inputState.guessing -= 1
            if synPredMatched224:
                pass
                self.match("...")
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in u'\t ':
                    pass
                    self.mSPACE(False)
                elif la1 and la1 in u'\n\r%':
                    pass
                else:
                        self.raise_NoViableAlt(self.LA(1))
                    
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in u'%':
                    pass
                    self.mCOMMENT(False)
                elif la1 and la1 in u'\n\r':
                    pass
                else:
                        self.raise_NoViableAlt(self.LA(1))
                    
                self.mNEWLINE(False)
                if not self.inputState.guessing:
                    _ttype = Token.SKIP;
            elif ((self.LA(1) >= u'0' and self.LA(1) <= u'9')):
                pass
                _cnt209= 0
                while True:
                    if ((self.LA(1) >= u'0' and self.LA(1) <= u'9')):
                        pass
                        self.mDIGIT(False)
                    else:
                        break
                    
                    _cnt209 += 1
                if _cnt209 < 1:
                    self.raise_NoViableAlt(self.LA(1))
                if not self.inputState.guessing:
                    _ttype = INT
                if (self.LA(1)==u'.') and (self.LA(2)==u'E' or self.LA(2)==u'e'):
                    pass
                    self.match('.')
                    self.mExponent(False)
                elif (self.LA(1)==u'.' or self.LA(1)==u'E' or self.LA(1)==u'e') and (True):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in u'.':
                        pass
                        self.match('.')
                        if ((self.LA(1) >= u'0' and self.LA(1) <= u'9')):
                            pass
                            _cnt214= 0
                            while True:
                                if ((self.LA(1) >= u'0' and self.LA(1) <= u'9')):
                                    pass
                                    self.mDIGIT(False)
                                else:
                                    break
                                
                                _cnt214 += 1
                            if _cnt214 < 1:
                                self.raise_NoViableAlt(self.LA(1))
                            if (self.LA(1)==u'E' or self.LA(1)==u'e'):
                                pass
                                self.mExponent(False)
                            else: ## <m4>
                                    pass
                                
                        else: ## <m4>
                                pass
                            
                    elif la1 and la1 in u'Ee':
                        pass
                        self.mExponent(False)
                    else:
                            self.raise_NoViableAlt(self.LA(1))
                        
                    if not self.inputState.guessing:
                        _ttype = FLOAT
                else: ## <m4>
                        pass
                    
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in u'i':
                    pass
                    self.match('i')
                elif la1 and la1 in u'I':
                    pass
                    self.match('I')
                elif la1 and la1 in u'j':
                    pass
                    self.match('j')
                elif la1 and la1 in u'J':
                    pass
                    self.match('J')
                    if not self.inputState.guessing:
                        _ttype = COMPLEX
                else:
                    ##<m3> <closing
                        pass
                    
                if not self.inputState.guessing:
                    self.string_ok=False
            elif (self.LA(1)==u'.') and (True):
                pass
                self.match('.')
                if not self.inputState.guessing:
                    _ttype = DOT;
                if not self.inputState.guessing:
                    self.string_ok=False
            else:
                self.raise_NoViableAlt(self.LA(1))
            
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mDIGIT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = DIGIT
        _saveIndex = 0
        pass
        self.matchRange(u'0', u'9')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mExponent(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = Exponent
        _saveIndex = 0
        pass
        la1 = self.LA(1)
        if False:
            pass
        elif la1 and la1 in u'e':
            pass
            self.match('e')
        elif la1 and la1 in u'E':
            pass
            self.match('E')
        else:
                self.raise_NoViableAlt(self.LA(1))
            
        la1 = self.LA(1)
        if False:
            pass
        elif la1 and la1 in u'+':
            pass
            self.match('+')
        elif la1 and la1 in u'-':
            pass
            self.match('-')
        elif la1 and la1 in u'0123456789':
            pass
        else:
                self.raise_NoViableAlt(self.LA(1))
            
        _cnt231= 0
        while True:
            if ((self.LA(1) >= u'0' and self.LA(1) <= u'9')):
                pass
                self.mDIGIT(False)
            else:
                break
            
            _cnt231 += 1
        if _cnt231 < 1:
            self.raise_NoViableAlt(self.LA(1))
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mNEWLINE(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = NEWLINE
        _saveIndex = 0
        pass
        _cnt304= 0
        while True:
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in u'\n':
                pass
                self.match('\n')
                if not self.inputState.guessing:
                    self.newline()
            elif la1 and la1 in u'\r':
                pass
                self.match('\r')
            else:
                    break
                
            _cnt304 += 1
        if _cnt304 < 1:
            self.raise_NoViableAlt(self.LA(1))
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mNAME(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = NAME
        _saveIndex = 0
        pass
        la1 = self.LA(1)
        if False:
            pass
        elif la1 and la1 in u'abcdefghijklmnopqrstuvwxyz':
            pass
            self.matchRange(u'a', u'z')
        elif la1 and la1 in u'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            pass
            self.matchRange(u'A', u'Z')
        elif la1 and la1 in u'_':
            pass
            self.match('_')
        else:
                self.raise_NoViableAlt(self.LA(1))
            
        while True:
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in u'abcdefghijklmnopqrstuvwxyz':
                pass
                self.matchRange(u'a', u'z')
            elif la1 and la1 in u'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                pass
                self.matchRange(u'A', u'Z')
            elif la1 and la1 in u'_':
                pass
                self.match('_')
            elif la1 and la1 in u'0123456789':
                pass
                self.mDIGIT(False)
            else:
                    break
                
        if not self.inputState.guessing:
            if self.text.getString(_begin) == "end":
               if self.paren_count: 
                   _ttype = ARRAY_END;
               else:
                   _ttype = END;
            if self.text.getString(_begin) in ["if","case","while","else","elseif","try","otherwise","catch"]:
               self.string_ok=True
            else:
               self.string_ok=False
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mMATCH(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = MATCH
        _saveIndex = 0
        pass
        self.match('?')
        la1 = self.LA(1)
        if False:
            pass
        elif la1 and la1 in u'abcdefghijklmnopqrstuvwxyz':
            pass
            self.matchRange(u'a', u'z')
        elif la1 and la1 in u'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            pass
            self.matchRange(u'A', u'Z')
        elif la1 and la1 in u'_':
            pass
            self.match('_')
        else:
                self.raise_NoViableAlt(self.LA(1))
            
        while True:
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in u'abcdefghijklmnopqrstuvwxyz':
                pass
                self.matchRange(u'a', u'z')
            elif la1 and la1 in u'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                pass
                self.matchRange(u'A', u'Z')
            elif la1 and la1 in u'_':
                pass
                self.match('_')
            elif la1 and la1 in u'0123456789':
                pass
                self.mDIGIT(False)
            else:
                    break
                
        if not self.inputState.guessing:
            if self.text.getString(_begin) == "end":
               if self.paren_count: 
                   _ttype = ARRAY_END;
               else:
                   _ttype = END;
            if self.text.getString(_begin) in ["if","case","while","else","elseif","try","otherwise","catch"]:
               self.string_ok=True
            else:
               self.string_ok=False
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mATPAREN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = ATPAREN
        _saveIndex = 0
        pass
        self.match('@')
        self.match('(')
        if not self.inputState.guessing:
            self.paren_count+=1
        if not self.inputState.guessing:
            self.string_ok=False
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mAND(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = AND
        _saveIndex = 0
        pass
        self.match('&')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mANDAND(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = ANDAND
        _saveIndex = 0
        pass
        self.match("&&")
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mASSIGN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = ASSIGN
        _saveIndex = 0
        pass
        self.match('=')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mAT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = AT
        _saveIndex = 0
        pass
        self.match('@')
        if not self.inputState.guessing:
            self.string_ok=False
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mBACKDIV(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = BACKDIV
        _saveIndex = 0
        pass
        self.match("\\")
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mCOLON(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = COLON
        _saveIndex = 0
        pass
        self.match(':')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mCOMMA(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = COMMA
        _saveIndex = 0
        pass
        self.match(',')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mDIV(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = DIV
        _saveIndex = 0
        pass
        self.match('/')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mDOTTRANS(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = DOTTRANS
        _saveIndex = 0
        pass
        self.match(".'")
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mDOTBACKDIV(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = DOTBACKDIV
        _saveIndex = 0
        pass
        self.match(".\\")
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mDOTDIV(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = DOTDIV
        _saveIndex = 0
        pass
        self.match("./")
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mDOTEXP(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = DOTEXP
        _saveIndex = 0
        pass
        self.match(".^")
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mDOTSTAR(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = DOTSTAR
        _saveIndex = 0
        pass
        self.match(".*")
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mEQUAL(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = EQUAL
        _saveIndex = 0
        pass
        self.match("==")
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mEXP(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = EXP
        _saveIndex = 0
        pass
        self.match('^')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mGREATER_OR_EQUAL(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = GREATER_OR_EQUAL
        _saveIndex = 0
        pass
        self.match(">=")
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mGREATER_THAN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = GREATER_THAN
        _saveIndex = 0
        pass
        self.match('>')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mLBRACK(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LBRACK
        _saveIndex = 0
        pass
        self.match('[')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        if not self.inputState.guessing:
            self.brack_count+=1
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mLBRACE(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LBRACE
        _saveIndex = 0
        pass
        self.match('{')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.paren_count+=1
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mLESS_OR_EQUAL(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LESS_OR_EQUAL
        _saveIndex = 0
        pass
        self.match("<=")
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mLESS_THAN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LESS_THAN
        _saveIndex = 0
        pass
        self.match('<')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mOROR(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = OROR
        _saveIndex = 0
        pass
        self.match("||")
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mLPAREN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LPAREN
        _saveIndex = 0
        pass
        self.match('(')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.paren_count+=1
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mMINUS(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = MINUS
        _saveIndex = 0
        pass
        self.match('-')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mNOT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = NOT
        _saveIndex = 0
        pass
        self.match('~')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mNOT_EQUAL(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = NOT_EQUAL
        _saveIndex = 0
        pass
        self.match("~=")
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mOR(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = OR
        _saveIndex = 0
        pass
        self.match('|')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mPLUS(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = PLUS
        _saveIndex = 0
        pass
        self.match('+')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mRBRACK(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = RBRACK
        _saveIndex = 0
        pass
        self.match(']')
        if not self.inputState.guessing:
            self.string_ok=False
        if not self.inputState.guessing:
            self.brack_count-=1
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mRBRACE(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = RBRACE
        _saveIndex = 0
        pass
        self.match('}')
        if not self.inputState.guessing:
            self.paren_count-=1
        if not self.inputState.guessing:
            self.string_ok=False
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mRPAREN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = RPAREN
        _saveIndex = 0
        pass
        self.match(')')
        if not self.inputState.guessing:
            self.paren_count-=1
        if not self.inputState.guessing:
            self.string_ok=False
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mSEMI(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = SEMI
        _saveIndex = 0
        pass
        self.match(';')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mSTAR(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = STAR
        _saveIndex = 0
        pass
        self.match('*')
        if (self.LA(1)==u'\t' or self.LA(1)==u' '):
            pass
            self.mSPACE(False)
        else: ## <m4>
                pass
            
        if not self.inputState.guessing:
            self.string_ok=True
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    

### generate bit set
def mk_tokenSet_0(): 
    ### var1
    data = [ 288019269919178752L, 0L, 0L]
    return data
_tokenSet_0 = antlr.BitSet(mk_tokenSet_0())

### generate bit set
def mk_tokenSet_1(): 
    ### var1
    data = [ -1025L, -1L, 0L, 0L]
    return data
_tokenSet_1 = antlr.BitSet(mk_tokenSet_1())

### generate bit set
def mk_tokenSet_2(): 
    ### var1
    data = [ -549755814913L, -1L, 0L, 0L]
    return data
_tokenSet_2 = antlr.BitSet(mk_tokenSet_2())

### generate bit set
def mk_tokenSet_3(): 
    ### var1
    data = [ -9217L, -1L, 0L, 0L]
    return data
_tokenSet_3 = antlr.BitSet(mk_tokenSet_3())
    
### __main__ header action >>> 
if __name__ == '__main__' :
    import sys
    import antlr
    import MatlabLexer
    
    ### create lexer - shall read from stdin
    try:
        for token in MatlabLexer.Lexer():
            print token
            
    except antlr.TokenStreamException, e:
        print "error: exception caught while lexing: ", e
### __main__ header action <<< 
