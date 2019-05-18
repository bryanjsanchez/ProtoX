# ProtoX

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

1. Download ProtoX from GitHub pressing the top right button.
2. Open the folder in your IDE and make sure that have installed Python 3.7 and antlr4-python3-runtime.
3. Run the class main.py.
4. Start using Proto X on the terminal.

### Example of Program

In ProtoX you can make correct inputs in this way:

```
 -Adds
ADD PROC TEXT TO HOSP TEXT.
ADD PROTO TEXT TO PROC TEXT.
ADD PROTO TEXT TEXT.
ADD HOSP TEXT
ADD PROC TEXT

-Shows
SHOW HOSP TEXT PROC
SHOW HOSP TEXT PROTO
SHOW PROC TEXT PROTO
SHOW PROTO TEXT
SHOW HOSP
SHOW PROC
SHOW PROTO

-Deletes
DELETE PROC TEXT FROM HOSP TEXT
DELETE PROTO TEXT FROM PROC TEXT
DELETE HOSP TEXT
DELETE PROC TEXT
DELETE PROTO TEXT

-Edit
EDIT PROTO TEXT WITH TEXT
```
An example of how you have to write it is this:

````
add hospital "Perea's hospital"
show hospitals
add procedure "CPR"
add protocol "ethics" "ETHICS DESCRIPTION"
add protocol "ethics" to procedure "CPR"
````
### Demo
<iframe width="966" height="543" src="https://www.youtube.com/embed/FYxcxD1X_mw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Contributors

ProtoX was developed by Bryan Sanchez (@bryanjsanchez), Renier Velazco (@velazcorenier), Cristian Torres (cfboy) and Bryan Bonilla (@bryann37) for the Programing Languages course at the University of Puerto Rico Mayaguez Campus
