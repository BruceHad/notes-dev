Code Complete
Part 1
Laying the Foundation

# Chapter 1 -- Software Construction

## What is Software Construction

Software development be broken down into lots of distinct tasks such as Problem Definition, Requirements, Contruction Planning, Architecture, Detailed Design, Coding, Debugging, Unit, System, Integration Testing, Integration and Maintainance.

"Construction" and "Programming" can be used interchangeably. Construction focuses on the coding and debugging, but also includes the detailed design, integration, testing and other activities. This is what the book focuses on too. Construction doesn't include management, requirements, software architecture, interface design, system testing or maintenance.

# Chapter 2 -- Metaphors for Understanding Software Development

Metaphor and analogy can be used to aid understanding and speed up learning a new topic. This use of metaphor is called 'modeling'.

An algorithm is a set of instructions for carrying out a particular task. It is predictable, deterministic and not subject to chance. A heuristic is a technique that helps you complete a task. It isn't as direct or reliable as an algorithm, but is more generally applicable.

There is no algorithm that will lead to a solution for software problems. Each problem is different. So knowing how to approach a problem is as valuable as knowing the solution for specific problems. That way you can come up with your own solution.

Metaphors are heuristics. Use them to illuminate your problems and guide you towards a solution.

Common metaphors include writing, farming, oyster farming. The later refers to the slow accretion of features on a simple framework. With incremental development, you first make the simplest possible versions of the system that will run. It just has to be a strong enough framework on which to build.

'Building/Contruction' metaphor is compatible with the idea of incremental development and matches up in other ways.

* Complexity of project requires different approaches (building a shed is approached differently from building a skyscraper).
* Can use pre-built components at various levels (bricks, prefabricated walls).
* Alternatively, can use custom build versions for specific purposes.
* Requires a level of planning and architecture.
* Changes in requirements cost more at later stages.

# Chapter 3 -- Prerequisites

First prerequisite is a clear **problem statement** that clarifies what the system is supposed to do. It doesn't refer to possible solution. The definition should be in user language/pov and should not refer to any technology (except where it's explicitely a problem with IT).

**Requirements** describe in detail what the software is supposed to do. The average project experiences around 25% change in requirements during development.

(See requirements checklist)

**System Architecture** is the high level design, that frames the solution. A system architecture needs an overview that describes the system in broad terms. 

The architecture should cover:

* Decisions and reasons for using the final solution, and the alternatives considered. 
* Thee major building blocks in a program. These could be classes or subsystems made up of multiple classes. Each feature listed in the requirements should be covered by at least one block. These blocks should be we defined, cohesive and independant as possible.
* The **data design**, files, tables, db design etc. 
* Resources and management. Performance information.
* Security - coding guidelines should be developed with security implications in mind.
* Interoperability - how it interfaces with other systems.
* Internationalisation/Localisation if appropriate.
* Input/Output schemes.
* Error processing - describing how errors should be handled system wide. 

The prerequisite tasks are aimed at reducing risk of something going wrong with the contstruction. 

Attention to detail and getting things right at the beginning has greater influence on product quality than elsewhere (and saves money).

# Chapter 4 -- Key Construction Decisions

Choose your language. Every language has strenghts and weaknesses.

Establish programming conventions before you begin. Avoid arbitrary variations leaving your brain free to spot the variations that need fixing. 

## The Technology Wave

Technology goes through cycles. e.g. mainframe to pc. command line to gui. windows app to web apps.

As the cycle matures so does the technology and the support tools. At the start of the wave technology is buggy and poorly documented. So how you spend your time depends on the state of the technology you are using, your position on the wave.

But the tools don't have to determine how you think about programming. You can program in a language, limitted by the constructs provided to you by that language. Or you can program "into" the language, using the language to construct your own programs, the way you want to contruct them.

## Select Your Contruction Practices

There are major practices that you should conciously decide about at the start of a project.

* Should the design be up front or while coding
* What coding conventions will be used
* What coding practices will be used
    *   Error handling
    *   Security
    *   Interfaces
    *   Code re-use
    *   Performance
    *   etc
* Where are you on the technology wave.
* Change/Integration procedure.
* Programming in pairs or something?
* TDD/Unit tests/Integration tests etc?
* Code reviews?
* Language/Framework/Stack
* Support tools, debugger etc
 

       
