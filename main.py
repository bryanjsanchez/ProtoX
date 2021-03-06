import sys

from grammar.build.ProtoXLexer import ProtoXLexer
from grammar.build.ProtoXParser import ProtoXParser
from grammar.ProtoXVisitor import ProtoXVisitor
from antlr4 import *


def main():
    print("----------------------------------------------------")
    print("Welcome to ProtoX!")
    while True:
        print("----------------------------------------------------")
        inputStream = InputStream(input())
        print()
        lexer = ProtoXLexer(inputStream)
        stream = CommonTokenStream(lexer)
        parser = ProtoXParser(stream)
        tree = parser.prog()
        visitor = ProtoXVisitor()
        if visitor.visit(tree):
            print(visitor.visit(tree))


if __name__ == '__main__':
    main()
