grammar ProtoX;

/***********
Parser Rules
************/

prog : statements EOF;

statements : statement*;

statement : expr;

expr: SHOW HOSP
| ADD PROC TEXT TO HOSP TEXT
| LIST PROC TEXT
| LIST HOSP PROC TEXT
| LIST HOSP PROTO TEXT
| SHOW HOSP
| SHOW PROC
| SHOW PROTO TEXT
| SHOW PROTO
| EDIT PROTO TEXT
| ADD HOSP TEXT
| ADD PROC TEXT
| ADD PROTO TEXT TEXT
;






/**********
Lexer Rules
***********/

//Main methods
ADD : 'add';
DELETE : 'delete';
EDIT : 'edit';

//Main objects
HOSP : 'hospitals' | 'hospital';
PROC : 'procedures' | 'procedure';
PROTO : 'protocols' | 'protocol';

TO : 'to';
SHOW : 'show';
LIST : 'list';
TEXT : SINGLEQUOT LETTER (LETTER|DIGIT|SPACE|PUNCTUATION|DOUBLEQUOT)* SINGLEQUOT
    | DOUBLEQUOT LETTER (LETTER|DIGIT|SPACE|PUNCTUATION|SINGLEQUOT)* DOUBLEQUOT;
NEWLINE : '\r'? '\n' -> skip;
WHITESPACE : (SPACE | '\t')+ -> skip;

/********
Fragments
*********/

fragment DIGIT : [0-9];
fragment LETTER : [A-Za-z_-];
fragment PUNCTUATION : [,./?!;:{}];
fragment SPACE : [ ];
fragment SINGLEQUOT : ['];
fragment DOUBLEQUOT : ["];
