grammar ProtoX;

/***********
Parser Rules
************/

prog : statements EOF;

statements : statement*;

statement : expr;

expr:
  ADD PROC TEXT TO HOSP TEXT
| ADD PROTO TEXT TO PROC TEXT
| ADD PROTO TEXT TEXT
| ADD HOSP TEXT
| ADD PROC TEXT

| SHOW HOSP TEXT PROC
| SHOW HOSP TEXT PROTO
| SHOW PROC TEXT PROTO
| SHOW PROTO TEXT
| SHOW HOSP
| SHOW PROC
| SHOW PROTO

| DELETE PROC TEXT FROM HOSP TEXT
| DELETE PROTO TEXT FROM PROC TEXT
| DELETE HOSP TEXT
| DELETE PROC TEXT
| DELETE PROTO TEXT

| EDIT PROTO TEXT WITH TEXT
;

/**********
Lexer Rules
***********/

//Main methods
ADD : 'add';
DELETE : 'delete';
EDIT : 'edit';
SHOW : 'show';

//Main objects
HOSP : 'hospitals' | 'hospital';
PROC : 'procedures' | 'procedure';
PROTO : 'protocols' | 'protocol';

// Conjunctions
WITH : 'with' ;
FROM : 'from';
TO : 'to';

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
