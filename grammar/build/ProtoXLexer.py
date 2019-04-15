from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("\u0080\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\7\r")
        buf.write("h\n\r\f\r\16\rk\13\r\3\16\3\16\3\17\5\17p\n\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\6\20w\n\20\r\20\16\20x\3\20\3\20\3")
        buf.write("\21\3\21\3\22\3\22\2\2\23\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\2#\2")
        buf.write("\3\2\5\4\2\13\13\"\"\3\2\62;\6\2//C\\aac|\2\u0081\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\3%\3\2\2\2\5)\3\2\2\2\7\60")
        buf.write("\3\2\2\2\t\65\3\2\2\2\13?\3\2\2\2\rJ\3\2\2\2\17T\3\2\2")
        buf.write("\2\21V\3\2\2\2\23X\3\2\2\2\25]\3\2\2\2\27b\3\2\2\2\31")
        buf.write("d\3\2\2\2\33l\3\2\2\2\35o\3\2\2\2\37v\3\2\2\2!|\3\2\2")
        buf.write("\2#~\3\2\2\2%&\7c\2\2&\'\7f\2\2\'(\7f\2\2(\4\3\2\2\2)")
        buf.write("*\7f\2\2*+\7g\2\2+,\7n\2\2,-\7g\2\2-.\7v\2\2./\7g\2\2")
        buf.write("/\6\3\2\2\2\60\61\7g\2\2\61\62\7f\2\2\62\63\7k\2\2\63")
        buf.write("\64\7v\2\2\64\b\3\2\2\2\65\66\7j\2\2\66\67\7q\2\2\678")
        buf.write("\7u\2\289\7r\2\29:\7k\2\2:;\7v\2\2;<\7c\2\2<=\7n\2\2=")
        buf.write(">\7u\2\2>\n\3\2\2\2?@\7r\2\2@A\7t\2\2AB\7q\2\2BC\7e\2")
        buf.write("\2CD\7g\2\2DE\7f\2\2EF\7w\2\2FG\7t\2\2GH\7g\2\2HI\7u\2")
        buf.write("\2I\f\3\2\2\2JK\7r\2\2KL\7t\2\2LM\7q\2\2MN\7v\2\2NO\7")
        buf.write("q\2\2OP\7e\2\2PQ\7q\2\2QR\7n\2\2RS\7u\2\2S\16\3\2\2\2")
        buf.write("TU\7*\2\2U\20\3\2\2\2VW\7+\2\2W\22\3\2\2\2XY\7u\2\2YZ")
        buf.write("\7j\2\2Z[\7q\2\2[\\\7y\2\2\\\24\3\2\2\2]^\7n\2\2^_\7k")
        buf.write("\2\2_`\7u\2\2`a\7v\2\2a\26\3\2\2\2bc\7$\2\2c\30\3\2\2")
        buf.write("\2di\5#\22\2eh\5#\22\2fh\5!\21\2ge\3\2\2\2gf\3\2\2\2h")
        buf.write("k\3\2\2\2ig\3\2\2\2ij\3\2\2\2j\32\3\2\2\2ki\3\2\2\2lm")
        buf.write("\7.\2\2m\34\3\2\2\2np\7\17\2\2on\3\2\2\2op\3\2\2\2pq\3")
        buf.write("\2\2\2qr\7\f\2\2rs\3\2\2\2st\b\17\2\2t\36\3\2\2\2uw\t")
        buf.write("\2\2\2vu\3\2\2\2wx\3\2\2\2xv\3\2\2\2xy\3\2\2\2yz\3\2\2")
        buf.write("\2z{\b\20\2\2{ \3\2\2\2|}\t\3\2\2}\"\3\2\2\2~\177\t\4")
        buf.write("\2\2\177$\3\2\2\2\7\2giox\3\b\2\2")
        return buf.getvalue()


class ProtoXLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ADD = 1
    DELETE = 2
    EDIT = 3
    HOSP = 4
    PROC = 5
    PROTO = 6
    LP = 7
    RP = 8
    SHOW = 9
    LIST = 10
    QUOTATION = 11
    ID = 12
    COMMA = 13
    NEWLINE = 14
    WHITESPACE = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'add'", "'delete'", "'edit'", "'hospitals'", "'procedures'",
            "'protocols'", "'('", "')'", "'show'", "'list'", "'\"'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "DELETE", "EDIT", "HOSP", "PROC", "PROTO", "LP", "RP",
            "SHOW", "LIST", "QUOTATION", "ID", "COMMA", "NEWLINE", "WHITESPACE" ]

    ruleNames = [ "ADD", "DELETE", "EDIT", "HOSP", "PROC", "PROTO", "LP",
                  "RP", "SHOW", "LIST", "QUOTATION", "ID", "COMMA", "NEWLINE",
                  "WHITESPACE", "DIGIT", "LETTER" ]

    grammarFileName = "ProtoX.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


