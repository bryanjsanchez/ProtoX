# Programming Language for Health Care Protocols

## Introduction
We are living in an era of frameworks to solve different computational problems. Technologies are merging to simplify our jobs. Hence, there are more tools to be used when trying to have a solution to a real problem. The perfect moment to contribute to the area of healthcare is now. When chaos presents itself in a hospital, there could be numerous options to alleviate the situation. How do we know that we are taking the most optimized solution for the problem? That's when computation and engineers can contribute to the system. We know that human emotions could be part of the foreground when dealing with victims that suffer from an arbitrary condition or an accident. ProtoX is a programming language whose purpose is to provide a framework to solve complex scenarios when decisions are vital to resolving the conflict. We have decided to create a programming language to simplify the development of surgery protocols in hospitals. We have talked about ProtoX purpose but what about its implementation? The main functionality of ProtoX and where it excels is the simple creation of protocols for a given situation and its retrieval. The user needs to follow a guideline when creating this protocol to ensure its correctness. What constitutes these guidelines? Some are clarity, brevity and a specific set of instructions. When using the programming language users can create protocols. Users can also access these protocols via decision making from a given input stored in variables to use them in an emergency. These protocols are merely an algorithm to follow for a proper situation. The goal of this new programming language is to help new doctors and nurses to act quickly in the medical process to prioritize human life from a bad decision or misstep in practice.

## Language Tutorial
1. Clone ProtoX repository from GitHub. 
2. Open the folder in your IDE and make sure that have installed Python 3.7 and antlr4-
python3-runtime.
3. Run the class main.py.
4. Start using Proto X on the terminal.

## Language Reference Manual
### In ProtoX you can make commands as follows: 

- Adds
  - ADD PROC TEXT TO HOSP TEXT
  - ADD PROTO TEXT TO PROC TEXT
  - ADD PROTO TEXT TEXT
  - ADD HOSP TEXT
  - ADD PROC TEXT

- Shows
  - SHOW HOSP TEXT PROC 
  - SHOW HOSP TEXT PROTO 
  - SHOW PROC TEXT PROTO 
  - SHOW PROTO TEXT 
  - SHOW HOSP
  - SHOW PROC
  - SHOW PROTO

- Deletes
  - DELETE PROC TEXT FROM HOSP TEXT 
  - DELETE PROTO TEXT FROM PROC TEXT 
  - DELETE HOSP TEXT
  - DELETE PROC TEXT 
  - DELETE PROTO TEXT 

- Edit
  -  EDIT PROTO TEXT WITH TEXT

### The following are important keywords in the language:

HOSP = hospital

PROC = procedure

PROTO = protocol

### Some sample commands are:

add hospital "Perea's hospital"

show hospitals

add procedure "CPR"

add protocol "ethics" "ETHICS DESCRIPTION" 

add protocol "ethics" to procedure "CPR"

## Language Development
The ProtoX code was developed using Python, and the IDE that we use was Pycharm. Here we implement a Lexer and a Parser using Antlr. Antlr is a library that automatically create the parser and lexer code and we just have to create the Grammar and run the antlr code. Then we create the different process of the ProtoX code that are the add, shows, delete and edit. All the data that we create they are stored in a module that is call “pickle”. This save/store all the process and save a copy so you can edit.

## Conclusion
The programming language ProtoX was a complete success since we fulfilled our main goal which was to make our methods work and try in the best possible way to not damage the language. Our biggest challenge was with the procedures since it was necessary to take into account that these protocols change for hospitals, and when this is changed, they should not affect each other. Going through the experience of using Antlr was very satisfying since we managed to do the parser and the lexer in a very efficient way. Editing the video was another great experience, were using a platform called iMovie we managed to edit it and bring it to its greatest perfection. In conclusion, this programming language was one that helped us see how everything we learned from the class can be united and put into practice to create a project like this. We hope that later this code will be very helpful for any programmer.

