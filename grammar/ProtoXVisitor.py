from grammar.build.ProtoXParser import ProtoXParser
from grammar.build.ProtoXVisitor import ProtoXVisitor as ProtoXVisitorOriginal


class ProtoXVisitor(ProtoXVisitorOriginal):
    def visitProg(self, ctx):
        return super(ProtoXVisitor, self).visitProg(ctx)

    def visitStatements(self, ctx):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx):
        result = None
        if ctx.expr():
            result = self.visitExpr(ctx.expr())
            print("The result is: " + str(result))
        else:
            result = super().visitStatement(ctx)
        return result

    def visitExpr(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())

        if ctx.PLUS():
            return self.visitExpr(ctx.expr(0)) + self.visitExpr(ctx.expr(1))
