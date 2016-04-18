# Quick Notes

Summary:

Short quick notes from articles and books that I am reading, and I want to get something written down. 

## 04/04/2016

Function Programming (Python)

https://codesachin.wordpress.com/2016/04/03/a-practical-introduction-to-functional-programming-for-python-coders/
https://en.wikipedia.org/wiki/Referential_transparency

Functional programming revolves around _pure functions_. In maths terms, a pure function is one that can be represented as a mathematical expression only, _no side-effects_, no i/o operations, no changes to state/context etc.

The output from a _pure function_ is only dependent on its inputs, so gives the same result every time.

> x -> f(x)

The easiest way to initialise a pure function in Python is by using the _lambda_ operative.
 
    square_func = lambda x: x**2
    square_func(3)
    9
    some_list = [(1, 3), (5, 2), (6, 1), (4, 6)]
    some_list.sort(key=lambda x: x[0]**2 - x[1]*3)
    some_list
    [(1, 3), (4, 6), (5, 2), (6, 1)]

The lambda keyword comes from Lambda Calculus, which influenced functional programming.

Lambda functions can also be called anonymous functions, as they aren't given a name (although can be assigned to a variable).

Higher order functions (functions that operate on other functions):

    function_product = lambda F, m: lambda x: F(x)*m
    function_product(square_func, 3)(2)
    12
    
function_product is a higher order function that takes two inputs: a function F(x) and a multiplier m. It returns F'(x) equal to m * F(x).

In this case the function F(x) is the square function, and m is 3 so 2^2*3 = 12.

_immutability_ means that you never modify the value of the data once initialised. In Functional Programming, whenever you call a function on some data, you always get a new instance as a result. You never update the existing values. This implies that once you initialise a variable like x = 3, then x never appears on the left hand side of a statement again.

Functional code can be thought of as a _feed forward_ data flow. 

The immutability of the data leads to a property called Referential Transparency. An expression is said to be referentially transparent if it can be replaced with its value without changing the behaviour of a program. This is helpful because it means the the order of evaluation isn't relevant, the results should be the same regardless. It's easier to analyse and debug.

This also enables the use of memoization, where you can store the outputs of expensive functions with common arguments in a lookup table.

_recursion_ is common in functional programming as the _while_ and _for_ type iterations aren't available.

    fibonacci = (lambda x, x_1=1, x_2=0: 
        x_2 if x == 0
        else fibonacci(x - 1,  x_1 + x_2, x_1))
    fibonacci(1)
    1
    fibonacci(5)
    5
    fibonacci(6)
    8

A recursive fib without using lambda might look something like:

    def fib(x):
        if x == 1: return 1
        elif x == 2: return 1
        else: return fib(x - 1) + fib(x - 2) 

It is better to implement _tail-recursion_ when writing functional code. Easier to optimise.

_map_, _reduce,_ and _filter_ are three higher-order function that appear in all pure functional languages, and Python.

_map_ provides a kind of parallelism by calling a function over all element of a list/array.

    map(lambda x: x**2, [1,2,3])
    [1,4,9]
    
_filter_ takes an input a boolean-returning function and a sequence, and filters that sequence.

    filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [2,4,6]
    
_reduce_ performs a serial iteration over a sequence. It's first argument is a function F(a, x) where a is an accumulator and x is the current input. The second argument is the sequence.

    reduce(lambda x, y: x + y, [1, 2, 3], 0)
    6
    
reduce can also be used to reverse a list.

    reduce(lambda L, element: [element] + L, [1, 2, 3], [])
    [3, 2, 1]
    

## 01/04/2016

Material Design

Principles:

* Material is the Metaphor
    * physical space and motion
    * Influenced by paper and ink
    * Surfaces and Edges
    * Familiarity and affordances
* Bold, graphic, intentional
    * Create heirarchy, meaning and focus
* Motion provides meaning
    * User as prime mover  
    * Clear feedback
    * Efficient transitions

The material environment is a 3d space. Sheets of material occupies a single position along the z-axis and has a standard 1pd (density independent pixel).

The 3d world is emulated (on the web) by manipulating the y-axis.

Within the material environment, virtual light illuminate the scene, creating shadow.  

Material is given various physical properties:

* Material has varying x/y dimensions and uniform thickness (1dp)
* Shadows result from the relative elevation.
* Content is displayed on material.
* Content is limited by the bounds of the material.
* Input events can't pass through material.
* Multiple meterials can't occupy the same space or pass through other material.
* Material can change shape, grow and shrink.
* Material never bends or folds.
* Material can join/merge.
* Material can be spontaneously generated or destroyed.
* Z axis motion is typically the result of a user interaction.

Material shares some qualities with physical objects. These qualities form a spatial model that is familiar.

Object hierarchy. How you organise objects determines how they move in relation to each other. Objects are organised in a hierarchy, objects can be child of the system or other objects.

Items parented to the root move independently of other objects.

Children have minimal z-axis seperation from their parent. Other objects do not get inserted between parents and children.



## 31/03/2016

https://codewords.recurse.com/issues/six/immutability-is-not-enough
https://github.com/facebook/immutable-js

Immutable data structure are key to modern, functional programming. Cannot, be modified, instead they are copied with changes applied.

Benefits, if used properly, it avoids the state change bugs that can be rife in imperative programming.

In javascript you might have state variables. e.g.

    var state = {
        pos: {x: 200, y: 220}  // Manuel's position.
    };
    
Can make this immutable using Immutable.js, which provides persitant, immutable data sets including Maps (key/value pairs).

    var initialState = Immutable.Map({
        pos: Immutable.Map({x: 200, y: 220})  // Manuel's position.
    });
    
It's now impossible to update the state directly. Instead you have to create a new state variable.

A function to update the state which originally look like this.

    if (dpad.right) {
        pos.x += 3;
    } else if (dpad.left) {
        pos.x -= 3;
    }

Now has to be done like this.

    function processInput(state) {
      var currX = state.getIn(['pos', 'x']);
      if (dpad.right) {
        return state.setIn(['pos', 'x'], currX + 3);
      } else if (dpad.left) {
        return state.setIn(['pos', 'x'], currX - 3);
      }
      return state;
    }
    
This makes them side-effect free (not sure what the side-effects are in this case???).

Functions can be composed into a pipeline so that instead of this:

    drawBackground(state);
    processInput(state);
    drawManuel(state);
    
You can have this.

    var newState =
          drawManuel(
          drawBackground(
          processInput(state)));

In each case, the state value from one function is passed to the next.

A bit on Function.prototype.bind():

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind

The bind method creates a new function that, when called, has its _this_ keyword set to the provided value. The new _bound_ function has the same 'body' as the original function (the target function).

    fun.bind(thisArg[, arg1[, arg2[, ...]]])
    
* thisArg - the value to be passed as the _this_ parameter.
* arg1... - Arguments to prepend to arguments provided to the bound function, when invoking the target function???

Bind can be used to ensure that the state is passed as an argument when the function is invoked.

A 'functional' render look like this.

    window.requestAnimationFrame(function render(state) {
      clearCanvas();
    
      var newState =
          drawManuel(
          drawBackground(
          processInput(state)));
    
      window.requestAnimationFrame(render.bind(null, newState));
    }.bind(null, initialState));

On each invocation of render, the current state is passed through a function pipeline.

A function that only needs to read the state (drawManuel) can just return the same object it was given. 

Advantages:

* Ata  glance, we can now see which function can read and write the state.
* The main components of the game now have a clearly defined interface: the state object.


Now try imagining creating a function to handle collision detection. The code checks the state and if the sprite is occupying the same space as another object, it should be moved. This could be included in the pipeline.

    var newState =
        drawManuel(
        drawBackground(
        processInput(
        handleCollisions(state))));

Note though, that there is a bug here. handleCollisions is called before processInput. 

So code is sensitive to ordering, and this is sometimes not very obvious.

[Alternative examples get steadily more complicated, without solving the issue.]


## 29/03/2016

http://chrismm.com/blog/how-to-reduce-the-cognitive-load-of-your-code/
https://news.ycombinator.com/item?id=11380762

Four basic concepts for keeping your code clean:

1. Keep personal quirks out of it. 

(How do you recognise personal quirks, esp. as opposed to 'idiomatic' code).

2. Single Responsibility Principle (Modular code)

TDD has benifit of forcing people to apply principles such as stateless code.

3. Avoid using language extension and libararies that do not play well with your IDE.

4. Make it readable

5. Remember that you will forget everything, and will have to read the code later.

Similarities between code and english: paragraphs with single point to get across, short sentences, organisation, abstraction.

