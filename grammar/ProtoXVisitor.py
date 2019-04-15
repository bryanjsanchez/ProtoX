from grammar.build.ProtoXParser import ProtoXParser
from grammar.build.ProtoXVisitor import ProtoXVisitor as ProtoXVisitorOriginal


class ProtoXVisitor(ProtoXVisitorOriginal):
    def visitProg(self, ctx):
        return super(ProtoXVisitor, self).visitProg(ctx)

    def visitStatements(self, ctx):
        return self.visitChildren(ctx)

    def visitExpr(self, ctx:ProtoXParser.ExprContext):
        result = None
        print(ctx.ADD())
        print(ctx.HOSP())
        print(ctx.LP(0))
        print(ctx.QUOTATION(0))
        print(ctx.ID(0))
        print(ctx.SHOW())
        return result



