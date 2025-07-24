
# COMP 170 SU25 WEEK 09

This assignment has two parts: a coding part based on current material we discuss in class and a reflection part to evaluate work you have already submitted.


## Finals week policy

There is no final exam for the course. There will be a final assignemnt that will be published the week before finals and will be due the week of finals. Additionally, 8 students in the course will be invited randomly to a brief meeting with the instructor during the course's final exam slot. The final exam slot for this course is on Tuesday, August 5, 2025 from 11 AM to 1 PM. If you are selected for a brief meeting, we'll spend about 15 minutes during the final exam slot to review your work. This interview will cover coding practices based on your past assignments. It is meant as a checkpoint to ensure that you have internalized the work you submitted.


## Code

We'll focus our work on recursion, a programming technique where a method calls itself except when it reaches a trivial case known as the base case. The file `week09.py` contains two examples of recursive code.


### Sum of digits
Write a *recursive* method `sum_of_digits` that accepts an integer number and returns the sum of its digits. For example, `sum_of_digits(4444)` should return `16`; `sum_of_digits(1234)` should return `10`, and so on. For your conveniene, an *iterative* version of the method is provided in `week09.py`

### Count occurrences
Write a *recursive* function `count_occurrences` that returns how many times a `target` value appears in a list. For example:
```python
count_occurrences([1, 2, 3, 1, 4, 1], 1)  # returns 3
```
 For your conveniene, an *iterative* version of the method is provided in `week09.py`

### Convert `week09.factorial` to iterative method
Write a method `factorial_iterative(n)` that computes $n!$ iteratively.

### Convert `week09.fibonacci` to iterative method
Write a method `fibonacci_iterative(n)` that computes $F(n)=F(n-1)+F(n-2)$ iteratively.


## Code requirements

* Methods that return a value should have one and only one `return` statement. Multiple `return` statements are not allowed.
* The following commands should **not** be used: `import`, `break`, `continue`.


## Reflect

Review the posted solutions from the previous assignment: [`Birthday`](./solutions_week08/Birthday.py), [`Person`](./solutions_week08/Person.py). Compare the posted solutions with your solutions. Notice the differences between your code and the solutions code and describe them. Trivial differences like the names of variables are not that important.

### Frequent mistakes expected at this point

* Your code has multiple return statements.

* **Code has no comments** to demonstrate mastery of the program.

* You do not show a test of `days_until`.

### Read more about:

* Recursion: Chapter 9 from the textbook; [Chapter 6](https://learning.oreilly.com/library/view/data-structures/9780134855912/ch06.xhtml) from Canning, Broder, and Lafore.
* [Type hints in Python](https://docs.python.org/3/library/typing.html); also useful [cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#functions)
* [f-strings in Python](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings)
* [lists in Python](https://docs.python.org/3/tutorial/datastructures.html). Also chapters 7.1 and 7.2 of the textbook.
* [the for statement](https://docs.python.org/3/reference/compound_stmts.html#for) and [for loop over a list in Python](https://docs.python.org/3/tutorial/controlflow.html#for-statements). Also chapter 2.3 and 7.1 of the textbook.
