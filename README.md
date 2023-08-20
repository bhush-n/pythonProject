# Python codes for a refresher

## What is Python?
Python is a high quality, versatile, and powerfully written programming language. Developed by Guido van Rossum, it was first released in 1991. Python is known for its readability, simplicity and ease of use, making it popular for beginners and pros mature as well, here are some of the basic characteristics of Python and how to use it.

1. **Legibility and Ease**: Python syntax is designed to be clear and readable, making it easy to learn and write code quickly.

2. **Versatility**: Python is a general-purpose programming language, which means it can be used for a wide range of applications including web development, data analysis, scientific computing, artificial intelligence , machine learning, automation, and more

3. **Large Standard Library**: Python provides a comprehensive standard library that provides modules and functions for different tasks, making it easy to do common programming tasks without having to write everything from scratch

4. **Interpreted Language**: Python code is executed by an interpreter, allowing rapid development and testing without the need for compilation.

5. **Cross-Platform Compatibility**: Python is available on multiple platforms including Windows, macOS, and Linux, allowing developers to write code that can run on different operating systems

6. **Community and 3rd Party Libraries**: Python has a large active team of developers, offering a large ecosystem of 3rd party libraries and frameworks that extend its powerful models and Django and Flask for web development, NumPy and pandas for data analysis, TensorFlow and PyTorch for machine learning .

7. **Indentation-Based Syntax**: Python uses whitespace (indentation) to define blocks of code, which enforce clea


## Variables in Python
Variables are names given to data that we need to store and manipulate
in our programs. For instance, suppose your program needs to store the
age of a user. To do that, we can name this data userAge and define the
variable userAge using the following statement.

userAge = 0

After you define the variable userAge, your program will allocate a
certain area of your computer's storage space to store this data. You can
then access and modify this data by referring to it by its name, userAge.
Every time you declare a new variable, you need to give it an initial value.
In this example, we gave it the value 0. We can always change this value
in our program later.

We can also define multiple variables at one go. To do that simply write

userAge, userName = 23,
‘Bhushan’

This is equivalent to

userAge = 23
userName = ‘Bhushan’

### Naming a Variable
A variable name in Python can only contain letters (a - z, A - B), numbers
or underscores (_). However, the first character cannot be a number.
Hence, you can name your variables userName, user_name or
userName2 but not 2userName.

In addition, there are some reserved words that you cannot use as a
variable name because they already have preassigned meanings in
Python. These reserved words include words like print, input, if,
while etc. We’ll learn about each of them in subsequent chapters.

Finally, variable names are case sensitive. username is not the same as
userName.

There are two conventions when naming a variable in Python. We can
either use the camel case notation or use underscores. Camel case is
the practice of writing compound words with mixed casing (e.g.
thisIsAVariableName). This is the convention that we’ll be using in
the rest of the book. Alternatively, another common practice is to use
underscores (_) to separate the words. If you prefer, you can name your
variables like this: this_is_a_variable_name.


## Operators in Python
Besides assigning a variable an initial value, we can also perform the
usual mathematical operations on variables. Basic operators in Python
include +, -, , , /, % and * which represent addition, subtraction,
multiplication, division, floor division, modulus and exponent respectively.

Example:

Suppose x = 5, y = 2

Addition: x + y = 7

Subtraction: x - y = 3

Multiplication: x*y = 10

Division: x/y = 2.5

Floor Division: x//y = 2 (rounds down the answer to the nearest whole
number)
Modulus: x%y = 1 (gives the remainder when 5 is divided by 2)
Exponent: x**y = 25 (5 to the power of 2)

### More Assignment Operators
Besides the = sign, there are a few more assignment operators in Python
(and most programming languages). These include operators like +=, -=
and *=.

Suppose we have the variable x, with an initial value of 10. If we want to
increment x by 2, we can write
x = x + 2

The program will first evaluate the expression on the right (x + 2) and
assign the answer to the left. So eventually the statement above
becomes x <- 12.

Instead of writing x = x + 2, we can also write x += 2 to express the
same meaning. The += sign is actually a shorthand that combines the
assignment sign with the addition operator. Hence, x += 2 simply
means x = x + 2.

Similarly, if we want to do a subtraction, we can write x = x - 2 or x -
= 2. The same works for all the 7 operators mentioned in the section
above

## The Assignment Sign
Note that the = sign in the statement userAge = 0 has a different
meaning from the = sign we learned in Math. In programming, the = sign
is known as an assignment sign. It means we are assigning the value on
the right side of the = sign to the variable on the left. A good way to
understand the statement userAge = 0 is to think of it as userAge <-
0.

The statements x = y and y = x have very different meanings in
programming.

Confused? An example will likely clear this up.

Type the following code into your IDLE editor and save it.

x = 5
y = 10
x = y
print ("x = "
, x)
print ("y = "
, y)

Now run the program. You should get this output:

x = 10
y = 10

Although x has an initial value of 5 (declared on the first line), the third
line x = y assigns the value of y to x (x <- y), hence changing the
value of x to 10 while the value of y remains unchanged.

Next, modify the program by changing ONLY ONE statement: Change
the third line from x = y to y = x. Mathematically, x = y and y = x mean
the same thing. However, this is not so in programming.

Run the second program. You will now get

x = 5
y = 5

You can see that in this example, the x value remains as 5, but the value
of y is changed to 5. This is because the statement y = x assigns the
value of x to y (y <- x). y becomes 5 while x remains unchanged as 5.


##  Data Types in Python

### *Integer
Integers are numbers with no decimal parts, such as -5, -4, -3, 0, 5, 7 etc.

To declare an integer in Python, simply write variableName =
initial value

Example:

userAge = 23, mobileNumber = 12398724

