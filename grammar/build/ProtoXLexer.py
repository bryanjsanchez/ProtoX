# Generated from /Users/nemo/git/ProtoX/grammar/src/ProtoX.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\62\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\3\2\6\2\23\n\2\r\2\16\2\24\3\3\3\3\3\3\7\3")
        buf.write("\32\n\3\f\3\16\3\35\13\3\3\4\3\4\3\5\5\5\"\n\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\6\6)\n\6\r\6\16\6*\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r\2\17\2\3\2\5\4\2\13\13")
        buf.write("\"\"\3\2\62;\4\2C\\c|\2\64\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3\22\3\2\2\2\5\26\3")
        buf.write("\2\2\2\7\36\3\2\2\2\t!\3\2\2\2\13(\3\2\2\2\r.\3\2\2\2")
        buf.write("\17\60\3\2\2\2\21\23\5\r\7\2\22\21\3\2\2\2\23\24\3\2\2")
        buf.write("\2\24\22\3\2\2\2\24\25\3\2\2\2\25\4\3\2\2\2\26\33\5\17")
        buf.write("\b\2\27\32\5\17\b\2\30\32\5\r\7\2\31\27\3\2\2\2\31\30")
        buf.write("\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34")
        buf.write("\6\3\2\2\2\35\33\3\2\2\2\36\37\7-\2\2\37\b\3\2\2\2 \"")
        buf.write("\7\17\2\2! \3\2\2\2!\"\3\2\2\2\"#\3\2\2\2#$\7\f\2\2$%")
        buf.write("\3\2\2\2%&\b\5\2\2&\n\3\2\2\2\')\t\2\2\2(\'\3\2\2\2)*")
        buf.write("\3\2\2\2*(\3\2\2\2*+\3\2\2\2+,\3\2\2\2,-\b\6\2\2-\f\3")
        buf.write("\2\2\2./\t\3\2\2/\16\3\2\2\2\60\61\t\4\2\2\61\20\3\2\2")
        buf.write("\2\b\2\24\31\33!*\3\b\2\2")
        return buf.getvalue()


class ProtoXLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    ID = 2
    PLUS = 3
    NEWLINE = 4
    WHITESPACE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "PLUS", "NEWLINE", "WHITESPACE" ]

    ruleNames = [ "INT", "ID", "PLUS", "NEWLINE", "WHITESPACE", "DIGIT", 
                  "LETTER" ]

    grammarFileName = "ProtoX.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


