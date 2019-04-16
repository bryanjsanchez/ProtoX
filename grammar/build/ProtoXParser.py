# Generated from /Users/nemo/git/ProtoX/grammar/src/ProtoX.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\7\3")
        buf.write("\17\n\3\f\3\16\3\22\13\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5?\n\5\3\5\2\2\6")
        buf.write("\2\4\6\b\2\2\2I\2\n\3\2\2\2\4\20\3\2\2\2\6\23\3\2\2\2")
        buf.write("\b>\3\2\2\2\n\13\5\4\3\2\13\f\7\2\2\3\f\3\3\2\2\2\r\17")
        buf.write("\5\6\4\2\16\r\3\2\2\2\17\22\3\2\2\2\20\16\3\2\2\2\20\21")
        buf.write("\3\2\2\2\21\5\3\2\2\2\22\20\3\2\2\2\23\24\5\b\5\2\24\7")
        buf.write("\3\2\2\2\25\26\7\n\2\2\26?\7\6\2\2\27\30\7\3\2\2\30\31")
        buf.write("\7\7\2\2\31\32\7\f\2\2\32\33\7\t\2\2\33\34\7\6\2\2\34")
        buf.write("?\7\f\2\2\35\36\7\13\2\2\36\37\7\7\2\2\37?\7\f\2\2 !\7")
        buf.write("\13\2\2!\"\7\6\2\2\"#\7\7\2\2#?\7\f\2\2$%\7\13\2\2%&\7")
        buf.write("\6\2\2&\'\7\b\2\2\'?\7\f\2\2()\7\n\2\2)?\7\6\2\2*+\7\n")
        buf.write("\2\2+?\7\7\2\2,-\7\n\2\2-.\7\b\2\2.?\7\f\2\2/\60\7\n\2")
        buf.write("\2\60?\7\b\2\2\61\62\7\5\2\2\62\63\7\b\2\2\63?\7\f\2\2")
        buf.write("\64\65\7\3\2\2\65\66\7\6\2\2\66?\7\f\2\2\678\7\3\2\28")
        buf.write("9\7\7\2\29?\7\f\2\2:;\7\3\2\2;<\7\b\2\2<=\7\f\2\2=?\7")
        buf.write("\f\2\2>\25\3\2\2\2>\27\3\2\2\2>\35\3\2\2\2> \3\2\2\2>")
        buf.write("$\3\2\2\2>(\3\2\2\2>*\3\2\2\2>,\3\2\2\2>/\3\2\2\2>\61")
        buf.write("\3\2\2\2>\64\3\2\2\2>\67\3\2\2\2>:\3\2\2\2?\t\3\2\2\2")
        buf.write("\4\20>")
        return buf.getvalue()


class ProtoXParser ( Parser ):

    grammarFileName = "ProtoX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'add'", "'delete'", "'edit'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'to'", "'show'", "'list'" ]

    symbolicNames = [ "<INVALID>", "ADD", "DELETE", "EDIT", "HOSP", "PROC", 
                      "PROTO", "TO", "SHOW", "LIST", "TEXT", "NEWLINE", 
                      "WHITESPACE" ]

    RULE_prog = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_expr = 3

    ruleNames =  [ "prog", "statements", "statement", "expr" ]

    EOF = Token.EOF
    ADD=1
    DELETE=2
    EDIT=3
    HOSP=4
    PROC=5
    PROTO=6
    TO=7
    SHOW=8
    LIST=9
    TEXT=10
    NEWLINE=11
    WHITESPACE=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(ProtoXParser.StatementsContext,0)


        def EOF(self):
            return self.getToken(ProtoXParser.EOF, 0)

        def getRuleIndex(self):
            return ProtoXParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ProtoXParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.statements()
            self.state = 9
            self.match(ProtoXParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProtoXParser.StatementContext)
            else:
                return self.getTypedRuleContext(ProtoXParser.StatementContext,i)


        def getRuleIndex(self):
            return ProtoXParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = ProtoXParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ProtoXParser.ADD) | (1 << ProtoXParser.EDIT) | (1 << ProtoXParser.SHOW) | (1 << ProtoXParser.LIST))) != 0):
                self.state = 11
                self.statement()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ProtoXParser.ExprContext,0)


        def getRuleIndex(self):
            return ProtoXParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ProtoXParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHOW(self):
            return self.getToken(ProtoXParser.SHOW, 0)

        def HOSP(self):
            return self.getToken(ProtoXParser.HOSP, 0)

        def ADD(self):
            return self.getToken(ProtoXParser.ADD, 0)

        def PROC(self):
            return self.getToken(ProtoXParser.PROC, 0)

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ProtoXParser.TEXT)
            else:
                return self.getToken(ProtoXParser.TEXT, i)

        def TO(self):
            return self.getToken(ProtoXParser.TO, 0)

        def LIST(self):
            return self.getToken(ProtoXParser.LIST, 0)

        def PROTO(self):
            return self.getToken(ProtoXParser.PROTO, 0)

        def EDIT(self):
            return self.getToken(ProtoXParser.EDIT, 0)

        def getRuleIndex(self):
            return ProtoXParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ProtoXParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(ProtoXParser.SHOW)
                self.state = 20
                self.match(ProtoXParser.HOSP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(ProtoXParser.ADD)
                self.state = 22
                self.match(ProtoXParser.PROC)
                self.state = 23
                self.match(ProtoXParser.TEXT)
                self.state = 24
                self.match(ProtoXParser.TO)
                self.state = 25
                self.match(ProtoXParser.HOSP)
                self.state = 26
                self.match(ProtoXParser.TEXT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(ProtoXParser.LIST)
                self.state = 28
                self.match(ProtoXParser.PROC)
                self.state = 29
                self.match(ProtoXParser.TEXT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.match(ProtoXParser.LIST)
                self.state = 31
                self.match(ProtoXParser.HOSP)
                self.state = 32
                self.match(ProtoXParser.PROC)
                self.state = 33
                self.match(ProtoXParser.TEXT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.match(ProtoXParser.LIST)
                self.state = 35
                self.match(ProtoXParser.HOSP)
                self.state = 36
                self.match(ProtoXParser.PROTO)
                self.state = 37
                self.match(ProtoXParser.TEXT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 38
                self.match(ProtoXParser.SHOW)
                self.state = 39
                self.match(ProtoXParser.HOSP)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 40
                self.match(ProtoXParser.SHOW)
                self.state = 41
                self.match(ProtoXParser.PROC)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 42
                self.match(ProtoXParser.SHOW)
                self.state = 43
                self.match(ProtoXParser.PROTO)
                self.state = 44
                self.match(ProtoXParser.TEXT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 45
                self.match(ProtoXParser.SHOW)
                self.state = 46
                self.match(ProtoXParser.PROTO)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 47
                self.match(ProtoXParser.EDIT)
                self.state = 48
                self.match(ProtoXParser.PROTO)
                self.state = 49
                self.match(ProtoXParser.TEXT)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 50
                self.match(ProtoXParser.ADD)
                self.state = 51
                self.match(ProtoXParser.HOSP)
                self.state = 52
                self.match(ProtoXParser.TEXT)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 53
                self.match(ProtoXParser.ADD)
                self.state = 54
                self.match(ProtoXParser.PROC)
                self.state = 55
                self.match(ProtoXParser.TEXT)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 56
                self.match(ProtoXParser.ADD)
                self.state = 57
                self.match(ProtoXParser.PROTO)
                self.state = 58
                self.match(ProtoXParser.TEXT)
                self.state = 59
                self.match(ProtoXParser.TEXT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





