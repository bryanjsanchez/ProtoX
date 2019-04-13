import sys

from grammar.build.ProtoXLexer import ProtoXLexer
from grammar.build.ProtoXParser import ProtoXParser
from grammar.ProtoXVisitor import ProtoXVisitor
from antlr4 import *


def main():
    filepath = "scripts/test.protox"
    input = FileStream(filepath)
    lexer = ProtoXLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ProtoXParser(stream)
    tree = parser.prog()
    visitor = ProtoXVisitor()
    return visitor.visit(tree)


if __name__ == '__main__':
    main()