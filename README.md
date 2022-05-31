# alx-higher_level_programming

## Tasks
0. Run Python file
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE
File: 0-run
   
1. Run inline
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE
File: 1-run_inline
   
2. Hello, print
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
File: 2-print.py
   
3. Print integer
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.
File: 3-print_number.py
	   
4. Print float
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.
File: 4-print_float.py

5. Print string
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
File: 5-print_string.py
	   
6. Play with strings
Complete this source code to print Welcome to Holberton School!
File: 6-concat.py

7. Copy - Cut - Paste
Complete this source code
File: 7-edges.py

8. Create a new sentence
Complete this source code to print object-oriented programming with Python, followed by a new line.
File: 8-concat_edges.py

9. Easter Egg
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

10. Linked list cycle
Technical interview preparation:
Prototype: int check_cycle(listint_t *list);
compile: `gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle`

Return: 0 if there is no cycle, 1 if there is a cycle
File: 10-check_cycle.c, lists.h

11. Hello, write
Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.
File: 100-write.py
   
12. Compile
Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE
```
johndoe@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

johndoe@ubuntu:~/py/0x00$ export PYFILE=main.py
johndoe@ubuntu:~/py/0x00$ ./101-compile
Compiling main.py ...
johndoe@ubuntu:~/py/0x00$ ls
101-compile  main.py  main.pyc
johndoe@ubuntu:~/py/0x00$ cat main.pyc | zgrep -c "Best School"
1
johndoe@ubuntu:~/py/0x00$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
johndoe@ubuntu:~/py/0x00$ 
```
The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
File: 101-compile

13. ByteCode -> Python #1
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
```
	3           0 LOAD_CONST               1 (98)
	3 LOAD_FAST                0 (a)
	6 LOAD_FAST                1 (b)
	9 BINARY_POWER
	10 BINARY_ADD
	11 RETURN_VALUE
```
Tip: Python bytecode
File: 102-magic_calculation.py

