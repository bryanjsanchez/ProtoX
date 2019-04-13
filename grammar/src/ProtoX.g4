grammar ProtoX;

/***********
Parser Rules
************/

prog : statements EOF;

statements : statement*;

statement : expr;

expr : expr PLUS expr | INT;

/**********
Lexer Rules
***********/

INT : DIGIT+;
ID : LETTER (LETTER|DIGIT)*;
PLUS : '+';

NEWLINE : '\r'? '\n' -> skip;
WHITESPACE : (' ' | '\t')+ -> skip;

/********
Fragments
*********/

fragment DIGIT : [0-9];
fragment LETTER : [A-Za-z];
