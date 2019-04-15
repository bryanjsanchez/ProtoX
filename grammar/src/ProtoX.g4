grammar ProtoX;

/***********
Parser Rules
************/

prog : statements EOF;

statements : statement*;

statement : expr;

expr: ADD HOSP LP QUOTATION ID QUOTATION RP
| SHOW HOSP
| ADD PROC LP QUOTATION ID QUOTATION COMMA QUOTATION ID QUOTATION LP
| LIST PROC LP QUOTATION ID QUOTATION RP
| LIST HOSP PROC LP QUOTATION ID QUOTATION RP
| LIST HOSP PROTO LP QUOTATION ID QUOTATION RP
| SHOW PROTO LP QUOTATION ID QUOTATION RP
| EDIT PROTO LP QUOTATION ID QUOTATION RP;






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

LP: '(';
RP: ')';
SHOW : 'show';
LIST : 'list';
QUOTATION : '"';
ID : LETTER (LETTER|DIGIT)*;
COMMA: ',';
NEWLINE : '\r'? '\n' -> skip;
WHITESPACE : (' ' | '\t')+ -> skip;

/********
Fragments
*********/

fragment DIGIT : [0-9];
fragment LETTER : [A-Za-z_-];
