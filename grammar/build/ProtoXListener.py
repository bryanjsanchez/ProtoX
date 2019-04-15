from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProtoXParser import ProtoXParser
else:
    from ProtoXParser import ProtoXParser

# This class defines a complete listener for a parse tree produced by ProtoXParser.
class ProtoXListener(ParseTreeListener):

    # Enter a parse tree produced by ProtoXParser#prog.
    def enterProg(self, ctx:ProtoXParser.ProgContext):
        pass

    # Exit a parse tree produced by ProtoXParser#prog.
    def exitProg(self, ctx:ProtoXParser.ProgContext):
        pass


    # Enter a parse tree produced by ProtoXParser#statements.
    def enterStatements(self, ctx:ProtoXParser.StatementsContext):
        pass

    # Exit a parse tree produced by ProtoXParser#statements.
    def exitStatements(self, ctx:ProtoXParser.StatementsContext):
        pass


    # Enter a parse tree produced by ProtoXParser#statement.
    def enterStatement(self, ctx:ProtoXParser.StatementContext):
        pass

    # Exit a parse tree produced by ProtoXParser#statement.
    def exitStatement(self, ctx:ProtoXParser.StatementContext):
        pass


    # Enter a parse tree produced by ProtoXParser#expr.
    def enterExpr(self, ctx:ProtoXParser.ExprContext):
        pass

    # Exit a parse tree produced by ProtoXParser#expr.
    def exitExpr(self, ctx:ProtoXParser.ExprContext):
        pass


