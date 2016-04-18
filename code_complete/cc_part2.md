Code Complete
Part 1
Creating High Quality Code

# Chapter 5 -- Design

On small projects, design can be part of the construction. On larger projects, the design is rarely detailed enough to allow programmers to ignore the design.

Design should be integrated with the system architecture.

Software design is the conception of a method for implementing the specification.

A good top-level design provides a structure that can containj multiple lower level designs.

Good design is useful on small projects, essential on large ones.

The point of design is partly to create possibilities and partly to restrict them, preventing sprawl.

Design is a heuristic process. It is also 'emergent', i.e. it grows out of multiple different tasks.

Objects have two types of properties, essential and accidental. The essential properties are what define that thing. A car without wheels isn't really a car. But a car without a roof is.

Software has accidental difficulties (which Fred Brooks says have largely been solved) and essential difficulties. The core essential difficulty is complexity (which can be both accidental and essential).

**Managing complexity is the most important technical topic ins software development.**

Any non-trivial software program is too large/complex to fit into anyone's head. Instead programs should be organised so that we can safely focus on one part of it at a time. Minimise the mental balls you have to keep in the air at any one time.

Reduce a complex system into simpler subsystems.

Make the subsystems independent, so you can safely focus on one at a time.

Minimise the amount of essential complexity that anyone has to deal with at one time.

Keep accidental complexity from proliferating.

**All other technical considerations are secondary to managing complexity.**

Aim for:

* Minimal complexity
* Ease of maintenance.
* Loose coupling
* Extensibility - allows you to extend functionality with minimal impact.
* Reusability
* High 'fan in' - good use of low level utility classes.
* Low 'fan out' - minimise the number of classes a class has to use.
* Leanness
* Good Stratification - able to look at code at a single 'level' without having to dip into other levels.
* Using Standard techniques

Levels of a system:

1. Software system
2. Subsystems/Packages
3. Classes in package
4. Methods and properties of a class
5. Routines

Each of these levels need to be designed.

## Design Heuristics

* Find real world objects
    *   Identify objects and their attributes.
    *   Determine what can be done with each object.
    *   Determine what each object will be allowed to do to other objects.
    *   Determine visible parts.
    *   Define the public interface.

_Abstraction_ is the ability to engage with a concept while safely ignoring some of its details.

Base classes are abjstractions that allow you to focus on common attributes of a set of derived classes and ignore the details of the specific classes while you're working on them. 

A good interface lets you work with an object without thinking about the internal workings.

Abstractions can be created at different levels, from the routines up to the packages.

_Encapsulation_ is the flip side of abstraction. Encapsulation hides the lower level details.

_Inheritance_ works with abstraction. You can define an general class and create multiple different implementations that inherit base functionality, and just define the differences.

This means that you can define different implementations of the same general function, and other parts of the program can use those functions without knowing the implemtation details, or even the type of object they are dealing with (until run time). This is known as _polymorphism_.

_Encapsulation_ and _Information Hiding_ keep implementation details hidden from the rest of the program. If done well, and changes you make to the hidden details should be local to the class, and not ripple beyond the class interface.

A class should reveal as little as possible about its inner workings. It's interface should be designed to minimise the need for changes. If the design doesn't stabalise, maybe the approach is wrong.

Two reasons for hiding:

1. Hiding complexity.
2. Hiding sources of change, to ensure effects are localised.

Circular dependencies, as when a routing in class A calls a routine in class B and vice versa, is a barrier to information hiding. Such dependencies should be avoided.

One good ability is to identify areas that are likely to change, so they can be isolated. 

1. Identify items that seem likely to change.
2. Seperate items that are liekly to change -- compartmentalise each volatile component into its own class or a class with other components that are likely to change _at the same time_.
3. Design interface so that changes are limitted to the inside of the class.

Likely changes:

* Business rules
* Hardware dependencies
* Inputs and outputs
* Difficult areas
* Status variables - likely to change, e.g. from Bool to Status code. use access routines rather than accessing variables directly
* Data size constraints

Keep coupling loose, so that classes are not dependant on a lot of other classes.

Kinds of coupling:
    
* Simple parameter coupling - loose
* Simple object coupling - loose
* Object-Parameter coupling - when a third object is passed between two objects as a parameter - tighter
* Semantic coupling - ???

Use Design Patterns: patterns reduce complexity by providing ready made abstractions.

A _Factory Method_ is a pattern that allows you to instantiate any class derived from a specific base class without needing to keep track of the individual derived classes anywhere but the factory method.

Patterns reduce errors by using common and tested code.

Patterns are easier to match to a problem, than designing a solution from scratch.

Patterns make discussion and communcation easier, by moving the dialogue to a higher level.
