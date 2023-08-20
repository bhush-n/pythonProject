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

### *Float

Float refers to numbers that have decimal parts, such as 1.234, -0.023,
12.01.

To declare a float in Python, we write variableName = initial
value

Example:
userHeight = 1.82, userWeight = 67.2


### *String

String refers to text.

To declare a string, you can either use variableName = ‘initial
value’ (single quotes) or variableName = “initial value”
(double quotes)

Example:
userName = ‘Bhushan’
, userSpouseName = “Minal”
, userAge
= ‘23’

In the last example, because we wrote userAge = ‘23’, userAge is a
string. In contrast, if you wrote userAge = 23 (without quotes),
userAge is an integer.

We can combine multiple substrings by using the concatenate sign (+).
For instance, “Bhushan” + “Chaudhari” is equivalent to the string
“BhushanChaudhari”.

#### Built-In String Functions

Python includes a number of built-in functions to manipulate strings. A
function is simply a block of reusable code that performs a certain task.

An example of a function available in Python is the upper() method for
strings. You use it to capitalize all the letters in a string. For instance,
‘Bhushan’.upper() will give us the string “BHUSHAN”. You can refer to
Appendix A for more examples and sample codes on how to use
Python’s built-in string methods.

### *List
List refers to a collection of data which are normally related. Instead of
storing these data as separate variables, we can store them as a list. For
instance, suppose our program needs to store the age of 5 users. Instead
of storing them as user1Age, user2Age, user3Age, user4Age and
user5Age, it makes more sense to store them as a list.

To declare a list, you write listName = [initial values]. Note
that we use square brackets [ ] when declaring a list. Multiple values are
separated by a comma.

Example:
userAge = [21, 22, 23, 24, 25]

We can also declare a list without assigning any initial values to it. We
simply write listName = []. What we have now is an empty list with
no items in it. We have to use the append() method mentioned below to
add items to the list.

Individual values in the list are accessible by their indexes, and indexes
always start from ZERO, not 1. This is a common practice in almost all
programming languages, such as C and Java. Hence the first value has
an index of 0, the next has an index of 1 and so forth. For instance,
userAge[0] = 21, userAge[1] = 23

Alternatively, you can access the values of a list from the back. The last
item in the list has an index of -1, the second last has an index of -2 and
so forth. Hence, userAge[-1] = 25, userAge[-2] = 24.

You can assign a list, or part of it, to a variable. If you write userAge2 =
userAge, the variable userAge2 becomes [21, 22, 23, 24, 25].

If you write userAge3 = userAge[2:4], you are assigning items with
index 2 to index 4-1 from the list userAge to the list userAge3. In other
words, userAge3 = [23, 24].

The notation 2:4 is known as a slice. Whenever we use the slice notation
in Python, the item at the start index is always included, but the item at
the end is always excluded. Hence the notation 2:4 refers to items from
index 2 to index 4-1 (i.e. index 3), which is why userAge3 = [23, 24]
and not [23, 24, 25].

The slice notation includes a third number known as the stepper. If we
write userAge4 = userAge[1:5:2], we will get a sub list consisting
of every second number from index 1 to index 5-1 because the stepper is
2. Hence, userAge4 = [22, 24].

In addition, slice notations have useful defaults. The default for the first
number is zero, and the default for the second number is size of the list
being sliced. For instance, userAge[ :4] gives you values from index
0 to index 4-1 while userAge[1: ] gives you values from index 1 to
index 5-1 (since the size of userAge is 5, i.e. userAge has 5 items).

To modify items in a list, we write listName[index of item to be
modified] = new value. For instance, if you want to modify the
second item, you write userAge[1] = 5. Your list becomes userAge
= [21, 5, 23, 24, 25]

To add items, you use the append() function. For instance, if you write
userAge.append(99), you add the value 99 to the end of the list. Your
list is now userAge = [21, 5, 23, 24, 25, 99]

To remove items, you write del listName[index of item to be
deleted]. For instance, if you write del userAge[2], your list now
becomes userAge = [21, 5, 24, 25, 99] (the third item is
deleted)
To fully appreciate the workings of a list, try running the following
program.

#declaring the list, list elements can be of different
data types myList = [1, 2, 3, 4, 5,
“Hello”]

#print the entire list.
print(myList)
#You’ll get [1, 2, 3, 4, 5,
“Hello”]

#print the third item (recall: Index starts from
zero).
print(myList[2])
#You’ll get 3

#print the last item.
print(myList[-1])
#You’ll get “Hello”

#assign myList (from index 1 to 4) to myList2 and
print myList2
myList2 = myList[1:5]
print (myList2)
#You’ll get [2, 3, 4, 5]

#modify the second item in myList and print the
updated list myList[1] = 20
print(myList)
#You’ll get [1, 20, 3, 4, 5,
'Hello']

#append a new item to myList and print the updated
list myList.append(“How are you”)
print(myList)
#You’ll get [1, 20, 3, 4, 5,
'Hello'
,
'How are you']

#remove the sixth item from myList and print the
updated list del
myList[5]
print(myList)
#You’ll get [1, 20, 3, 4, 5,
'How are you']


