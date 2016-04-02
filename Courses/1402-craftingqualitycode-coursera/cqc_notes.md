    # Crafting Quality Code

https://class.coursera.org/programming2-001/class/index

Start Date - March 25th 2013

You know the basics of programming in Python: elementary data types (numeric types, strings, lists, dictionaries and files), control flow, functions, objects, methods, and mutability. You need to be good at these in order to succeed in this course.

Here are the parts of this course:

Video lectures (which should take you a couple hours a week, including doing the in-video quizzes). The in-video quizzes are not part of the marking scheme. Students have reported that it is helpful to use IDLE (the program we use to write Python programs) while the lectures progress, typing in the Python code that we show.

Four exercises and two programming assignments. (There is no final exam!)

## Week 1

* Pre-course Survey
* 6 Lectures
 ** 3 Algorithms for identifying a palindrome.
 ** Resturant Lists code.
* 1 quiz (11/12)

Complete Wednesday 27th March

## Week 2

* 6 Lectures

Function design recipes, doctest, automated testing, the __name__, __main__ thing; unittest

Types are classes. Try help(str).

Don't really understand method and function calls. What is the difference???

Choosing Test Cases: Size (empty, single, small, large), dichotomies, boundaries, order

UnitTest: 

import the function to test
import 'unittest'
create a class:

	class TestNumBuses(unittest.TestCase):

For each test case create a method for the class. Each method name should begin with 'test'.
Finally, add the main function call

	if __name__ == '__main__':
	    unittest.main(exit=False)

## Week 3 - Algorithms

Analyse algorithms to find out how long they run. Read the code and count the number of steps they take.

Logarithms: log_2(n): the number of times we divide n by 2 in order to reach 1.

cProfile. run(statement, filename=None, sort=-1) Profiles your statement and tells you where to look to improve performance.

Sorting Algoriths: Bubble Sort, Selection Sort, Insertion Sort

## Week 4 - Objects and Classes

Seemed to be about re-using built in methods of the object module. __init__ is an easy example. It is called whenever a new object is created. Similarly you can write custom __str__ method which will be used when print(object).

## Assignment 2

Implement 2 classes: Rat and Maze.

