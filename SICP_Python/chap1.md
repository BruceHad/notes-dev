# Building Abstractions using Functions

CS is built on fundamental ideas. Begins with representing info, specifying logic to process it, and designing abstractions that manage the complexity of the logic.

To master the fundamentals, learn how computers interpret programs and carry out computation.

Based on Structure and Interpretation of Computer Programs (SICP) -- Harold Abelson, Gerald Jay Sussman, Julie Sussman, but using Python as the programming language rather than Scheme.

## The Very Basics

Programs consist of instructions to either compute some value or carry out some action. Python Code consists of _expressions_ and _statements_. 

Statements typically describe actions. Expressions typically describe computations (calculating a value).

_Functions_ encapsulate logic. This means complex processes can be carried out with simple expressions, because the complexity is hidden in a function.

_Objects_ bundles together data and logic. 

Python also has _compound expressions_ like:

    {w for w in words if len(w) == 6 and w[::-1] in words}
    # {'redder', 'drawer', 'reward', 'diaper', 'repaid'}

This evaluates to a set of words that are also words in reverse. The cryptic notation w[::-1] enumerates each letter in a word, backwards.

_Interpreters_ evaluate the code.

These core concepts are closely related. Functions are objects. Interpreters are instances of both. But developing a clear understanding of these concepts is critical to mastering programming.

Learning to interpret _errors_ and diagnose the cause of unexpected errors is called _debugging_.

1. Test incrementally.
2. Isolate errors.
3. Check your assumptions.
4. Consult others.

Incremental testing, modular design, precise assumptions, and teamwork are themes that persist throughout this text.

## Elements of Programming

Programming language also serves as a framework within which we organise our ideas about compuatational processes. They also share those ideas, so must be written to be read.

Languages provide means to combine simple ideas to form complex ideas.

* Primitive expressions and statements (simplest building blocks).
* Means of combinations to compound elements.
* Means of abstraction, by which compound elements can be named and manipulated as units.

Two kinds of elements functions and data (not so distinct).

### Expressions

Expressions representing numbers may be combined with operators to form compound expressions, which the interpretter will evaluate.

These mathematical expressions use _infix_ notation, with the operator between the operands.

The most important kind of compound expression is a _call_ expressions, wich calls a function and applies it to some arguments.

Mathematical functions are some mapping from an input to an output value.

Function notation extends to nested expressions fairly easily.

### Importing

Python defines a large number of functions, but not all are available by default.

These are organised into modules, which comprise the python library.

    from math import sqrt
    sqrt(256)
    > 16.0

An import statement designates a module name then lists the named attributes of that module to import.

### Names and the Environment

If a value has been given a name, we say that the name binds to that value. New bindings are established using the assignment statement =.

    radius = 10

Names are also bound via import statements.

The interpreter must remember the names and assignments, keeping track of values and binding. This is called an _environment_.

Names can also be bound to functions.

Names are often called variables. They can be bound to new values using assignment. Even built in names can be bound to new values.

The interpreted will evaluate the right hand side before assignement. You can therefore refer to the same name.

    x = 2
    x = x + 1

### Functions

Pure functions have some input and return some output.

Non pure functions can generate side effects, which make some change to the state of the interpreter or computer. e.g. the print function.

Pure functions are restricted in that they cannot have side effects or change behaviour over time. Impossing these restrictions yields benefits:

* The can be composed more reliably into compound expressions.
* They are simpler to test.
* Essential for writing concurrent programs.

## Defining Functions

    def square(x):
        return mul(x,x)

Function definitions consist of a _def_ a name and a comma seperated list of named parameters. then a _return_ statement in the function _body_.

### Environments

An environment in which an expressions is evaluated consists of a sequence of _frames_ (depicted as boxes). Each frame contains bindings.

There is a single global frame. Assignment and import statements add entries to the first frame of the current environment. 

So far though, our environment consists only of the global frame.

Applying a user-defined function introduces a second local frame, which is only accessible to that function. To apply a user defined function:

1. Bind the arguments to the names of the function's formal parameters in a new local frame.
2. Execute the body of the function in the environment that starts with this frame.

Each instance of a function application has its own independent local frame.

The names in the local frame are independent from other frames. This means the names can be re-used, without causing problems for other frames. In other words, the _scope_ of the local name is limited to the body of the function that defines it.

But good naming is also important. In Python the following conventions are encouraged.

1. Function names are lower case, underscored.
2. Parameter names are lowercase, underscored. Single words preferred.
3. Parameters names should evoke the role of the parameter in in the function.

### Functions are abstractions

A function like square is an abstraction. The rest of the code need not concern itself with how the function is implemented, only in that it will return the correct answer. With good function definitions, you can suppress details.

To master the use of function abstraction, it is often useful to consider its three core attributes:

* The domain of a function is the set of arguments it can take.
* The range of a function is the set of values it can return.
* The intent of a function is the relationship it computes between input and outputs (as well as any sideeffects).

## Designing Functions

Functions serve as our primary medium to express computational processes. The qualities of good functions reinforce the idea that a function is an abstraction.

* It should do one job.
* That job should be identified by a good name and be characterisable in a single line of text.
* Should be DRY (do not repeat)
* Functions should be defined generally (e.g. power is a general version of square).

### Docstring

A function definition will often include documentation describing the function (docstring). 

    def pressure(v, t, n):
        """Compute the pressure in pascals of an ideal gas.
        
        v -- volume (cubic metres)
        t -- absolute temperature (kelvin)
        n -- particles of gass
        """
        k = 1.38e-23 # Botlzmann's constant
        return n * k * t /v
        
When you call _help_ with the name of a function, it return the docstring.

### Default Argument Values

A consequence of defining functions to be as general as possible, is that the number of arguments tends to grow. Functions with many arguments can be difficult to call and read.

Functions can provide default arguments, which are then optional when calling.

    def pressure(v, t, n=6.022e23)

As a guide most data values used in a function's body should be expressed as default values to named arguments. That makes them easy to inspect and change by the function's caller.

Some values that never change can be bound in the function body or the global frame.

## Control

Control _statements_ control the flow of a program based on comparisons.

Statements aren't evaluated, they don't compute any values. They are executed and determine what the interpreter does next.

### Testing

Testing verifies that function's behaviour matches expectations.

A test is a mechanism for systematically performing this verification.

Tests typically take the form of another function that contains one or more sample call to the function being tested.

The return value is then verified against the expected result.

(Test also serve as documentation, demonstrating how to call a function)

_Assertions_ verify expectations. 

    assert fib(8) == 13
    
If the expression evaluates to true, nothing happens. When it's false, assert causes and error that halts execution.

    def fib_test():
        assert fib(2) == 1
        assert fib(3) == 1
        assert fib(50) == 7778742049
        
Convention: Tests are typically written in the same file or a neighbouring file with the suffix '_test.py'.

_Doctests_ are a convenient was of placing simple tests in the docstring of a function.

    def sum_naturals(n):
        """Return the sum of the first n natural numbers
        
        >>> sum_naturals(10)
        55
        >>> sum_naturals(100)
        5050
        """
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total

    if __name__ == "__main__":
        import doctest
        print(doctest.testmod())

## Higer Order Functions

