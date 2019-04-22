grammar ProtoX;

/***********
Parser Rules
************/

prog : statements EOF;

statements : statement*;

statement : expr;

expr: SHOW HOSP
| ADD PROC TEXT TO HOSP TEXT
| ADD PROTO TEXT TO PROC TEXT
| LIST PROC TEXT
| LIST HOSP PROC TEXT
| LIST HOSP PROTO TEXT
| SHOW HOSP TEXT PROC
| SHOW HOSP TEXT PROTO
| SHOW PROC TEXT PROTO
| SHOW HOSP
| SHOW PROC
| SHOW PROTO TEXT
| SHOW PROTO
| EDIT PROTO TEXT WITH TEXT
| ADD HOSP TEXT
| ADD PROC TEXT
| ADD PROTO TEXT TEXT
| DELETE HOSP TEXT
| DELETE PROC TEXT FROM HOSP TEXT
| DELETE PROTO TEXT FROM PROC TEXT
| DELETE PROC TEXT
| DELETE PROTO TEXT
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

WITH : 'with' ;
FROM : 'from';
TO : 'to';
SHOW : 'show';
LIST : 'list';
TEXT : SINGLEQUOT (LETTER|DIGIT|SPACE|PUNCTUATION|DOUBLEQUOT)+ SINGLEQUOT
    | DOUBLEQUOT (LETTER|DIGIT|SPACE|PUNCTUATION|SINGLEQUOT)+ DOUBLEQUOT;
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
