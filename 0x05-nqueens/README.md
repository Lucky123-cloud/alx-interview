
Curriculum
Short Specializations
Average: 116.4%
0x05. N Queens
Algorithm
Python
 Weight: 1
 Project will start Aug 26, 2024 6:00 AM, must end by Aug 30, 2024 6:00 AM
 Checker was released at Aug 27, 2024 6:00 AM
 An auto review will be launched at the deadline
The “0x05. N queens” project is a classic problem in computer science and mathematics, known for its application of the backtracking algorithm to place N non-attacking queens on an N×N chessboard. To successfully complete this project, you will need to understand several key concepts and have access to resources that will help you grasp the necessary algorithms and techniques.

Concepts Needed:
Backtracking Algorithms:

Understanding how backtracking algorithms work to explore all potential solutions to a problem and backtrack when a solution cannot be completed.
Backtracking Introduction
Recursion:

Using recursive functions to implement backtracking algorithms.
Recursion in Python
List Manipulations in Python:

Creating and manipulating lists, especially to store the positions of queens on the board.
Python Lists
Python Command Line Arguments:

Handling command-line arguments with the sys module.
Command Line Arguments in Python
By studying these concepts and utilizing the resources provided, you will be equipped with the knowledge required to implement an efficient solution to the N queens problem using Python. This project not only tests programming and problem-solving skills but also offers an excellent opportunity to learn about algorithmic thinking and optimization techniques.

Additional Resources
Mock Interview
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
All your files must be executable
Tasks
0. N queens
mandatory

Chess grandmaster Judit Polgár, the strongest female chess player of all time


The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
Read: Queen, Backtracking

julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
Repo:

GitHub repository: alx-interview
Directory: 0x05-nqueens
File: 0-nqueens.py
 
Copyright © 2024 ALX, All rights reservedd


0x05. N Queens
==============

- By Dev Nderitu

Requirements
------------

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version 1.7.*)
- All your files must be executable

Tasks
-----

### 0\. N queens

mandatory

![](http://www.crestbook.com/files/Judit-photo1_602x433.jpg)\
Chess grandmaster [Judit Polgár](https://alx-intranet.hbtn.io/rltoken/fZ1ecpPEmVL9nvkBn8WQGg "Judit Polgár"), the strongest female chess player of all time

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

- Usage: `nqueens N`
  - If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
- where N must be an integer greater or equal to `4`
  - If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
  - If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
- The program should print every possible solution to the problem
  - One solution per line
  - Format: see example
  - You don't have to print the solutions in a specific order
- You are only allowed to import the `sys` module

Read: [Queen](https://alx-intranet.hbtn.io/rltoken/ghWqI1wvx6g-Ul7nrufMKA "Queen"), [Backtracking](https://alx-intranet.hbtn.io/rltoken/-hgZbgRFkwmxaKnLnCIuEQ "Backtracking")

```
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$

```

**Repo:**

- GitHub repository: `alx-interview`
- Directory: `0x05-nqueens`
- File: `0-nqueens.py`

## Solution

```
import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_q = int(sys.argv[1])
except ValueError:
    print('N must ba a number')
    exit(1)

if n_q < 4:
    print('N must ba at least 4')
    exit(1)


def solve_nqueens(n):
    ''' self descriptive '''
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def attack_queen(square, queen):
    '''self descriptive'''
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    '''self descriptive'''
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True


for answer in reversed(solve_nqueens(n_q)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
```
