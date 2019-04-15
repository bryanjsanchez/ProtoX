grammar ProtoX;

/***********
Parser Rules
************/

prog : statements EOF;

statements : statement*;

statement : expr;

expr: ADD HOSP ID
| SHOW HOSP
| ADD PROC ID TO HOSP ID
| LIST PROC ID
| LIST HOSP PROC ID
| LIST HOSP PROTO ID
| SHOW PROTO ID
| EDIT PROTO ID;






/**********
Lexer Rules
***********/

//Main methods
ADD : 'add';
DELETE : 'delete';
EDIT : 'edit';

//Main objects
HOSP : 'hospitals';
PROC : 'procedures';
PROTO : 'protocols';

TO : 'to';
SHOW : 'show';
LIST : 'list';
ID : LETTER (LETTER|DIGIT)*;
NEWLINE : '\r'? '\n' -> skip;
WHITESPACE : (' ' | '\t')+ -> skip;

/********
Fragments
*********/

fragment DIGIT : [0-9];
fragment LETTER : [A-Za-z_-];
