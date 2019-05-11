# ProtoX

//Video

### Introduction

ProtoX is a programming language whose purpose is to provide a framework to solve complex scenarios when decisions are vital to resolving the conflict. We create a programming language to simplify the development of surgery protocols in hospitals.

### Language Features

The language has three types of “objects”: hospitals, procedures and protocols. A hospital can perform many different procedures and each procedure has associated protocols. Our ProtoX language can perform the following operations:


```language
-Create/delete a hospital.
-Show all hospitals.
-Add a procedure that is done to each hospital.
-Fetch the list of protocols related to a procedure.
-Fetch the list of protocols by hospital depending on which procedures they offer.
-List the procedures done in each hospital for all procedures.
-Create/delete a protocol.
-Edit an existing protocol.
-Assign a protocol to a procedure.
-Remove protocol from a procedure.
```
### Installation

1. Download ProtoX from GitHub pressing the top left button.
2. Open the folder in your IDE and make sure that have installed Python 3.7 and antlr4-python3-runtime.
3. Run the class main.py.
4. Start using Proto X on the terminal.

### Example of Program

In ProtoX you can make correct inputs in this way:

```example of program
 -Add's
ADD PROC TEXT TO HOSP TEXT
ADD PROTO TEXT TO PROC TEXT
ADD PROTO TEXT TEXT
ADD HOSP TEXT
ADD PROC TEXT

-Show's
SHOW HOSP TEXT PROC
SHOW HOSP TEXT PROTO
SHOW PROC TEXT PROTO
SHOW PROTO TEXT
SHOW HOSP
SHOW PROC
SHOW PROTO

-Delete's
DELETE PROC TEXT FROM HOSP TEXT
DELETE PROTO TEXT FROM PROC TEXT
DELETE HOSP TEXT
DELETE PROC TEXT
DELETE PROTO TEXT

-Edit's
EDIT PROTO TEXT WITH TEXT
```
An example of how you have to write it is this:

```Example
add hospital "Bryan's hospital"
show hospitals
add procedure "CPR"
add protocol "ethics" "ETHICS DESCRIPTION"
add protocol "ethics" to procedure "CPR"
```

### Contributors

ProtoX was developed by Bryan Sanchez (@bryanjsanchez), Renier Velazco (@velazcorenier), Christian Torres (cfboy) and Bryan Bonilla (@bryann37) for the Programing Languages course at the University of Puerto Rico Mayaguez Campus
