# Coding Standards

## Description

In this exercise, we will use flake8 to explore some of the most important PEP8 recommendations.

You will need to have [flake8](https://pypi.org/project/flake8/) installed, ideally in a container or virtual environment.

> For this exercise we recommend you to use a standard simple text editor or your current editor with the Linter disabled.

##

## Tasks

###

### Task 1

Create a file named `task1.py`. In this file, define a variable named `first` and assign any text string you like to it.

Then check the style with flake8 in the command line (i.e run `flake8 task1.py`).

If it produces any errors, fix them and run it again until it produces no error.

###

### Task 2

Create a file named `task2.py` and define a function named `greet` with no arguments. This function will print "Hello World!".

Then check the style with flake8. If it produces any errors, fix them and run it again until it produces no error.

###

### Task 3

Create a file named `task3.py` and define two functions named `first` and `last`, with no arguments. They will print the text **first** and **last**.

In the same file, and after the functions, call those two functions.

Then check the style with flake8. If it produces any errors, fix them and run it again until it produces no error.

###

### Task 4

Create a file named `task4.py` and define a function named `greet` that will accept two positional arguments `first` and `last`. The function will print "Hello, {first} {last}!".

After the function, call it with any two texts of your choice.

Then check the style with flake8. If it produces any errors, fix them and run it again until it produces no error.

###

### Task 5

Create a file named `task5.py` and define a function named `greet` that will accept two keyword arguments `first` and `last` with default values `John` and `Doe`. The function will print "Hello, {first} {last}!".

> If you prefer, you can change or copy the `task4.py` file.

After the function, call it using keyword arguments with any two texts of your choice.

Then check the style with flake8. If it produces any errors, fix them and run it again until it produces no error.

###

### Task 6

Create a file named `task6.py` and write the Python code that matches this pseudo-code:

```
function check {
  luck = produce random number
  if luck < 0.5 then print "Sorry"
  else print "Congratulations"
}
check()
```
> **Hint**: you may import the module `random` to produce the random number, but don't put it inside the function.

Then check the style with flake8. If it produces any errors, fix them and run it again until it produces no error.

###

### Task 7

Create a file named `task7.py` and define a function named `my_custom_validation_function` that takes ten positional arguments named `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, `nine` and `ten`.

> The body of the function may be left empty (with the `pass` keyword)

Then call this function with the first five arguments as `True` and the last 5 as `False`.

Then check the style with flake8. If it produces any errors, fix them and run it again until it produces no error.

###

### Task 8

Take the previous task and now change the arguments to keyword arguments and define the function with default values (`False` for the first 5 and `True` for the last five).

Call the function with keyword arguments and set the first 5 to `True` and the last 5 to `False`.

Then check the style with flake8. If it produces any errors, fix them and run it again until it produces no error.

###

### Task 9

Take the previous task and now write a conditional inside the function that checks if the first 5 arguments are `True` and the last 5 are `False`. In that case, it will print "ok".

Call the function with keyword arguments again.

Then check the style with flake8. If it produces any errors, fix them and run it again until it produces no error.

###

### Task 10

Take the previous task and now write a comment saying `Checking arguments` before the conditional (in a new line) and another comment for the print, to the right of it, in the same line, saying `arguments are ok`.

Then check the style with flake8. If it produces any errors, fix them and run it again until it produces no error.
