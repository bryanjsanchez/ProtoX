# Generated from /Users/nemo/git/ProtoX/grammar/src/ProtoX.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProtoXParser import ProtoXParser
else:
    from ProtoXParser import ProtoXParser

# This class defines a complete generic visitor for a parse tree produced by ProtoXParser.

class ProtoXVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ProtoXParser#prog.
    def visitProg(self, ctx:ProtoXParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProtoXParser#statements.
    def visitStatements(self, ctx:ProtoXParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProtoXParser#statement.
    def visitStatement(self, ctx:ProtoXParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProtoXParser#expr.
    def visitExpr(self, ctx:ProtoXParser.ExprContext):
        return self.visitChildren(ctx)



del ProtoXParser