# Algorithms, Part I

by Kevin Wayne, Robert Sedgewick

10/06/2014

https://class.coursera.org/algs4partI-005

## Intro to Java

### Basics & Command Line

Java programs are usually split into classes. One file per class. By convention, all classes have a 'main' method that can be called from the command line for test purposes.

	/* HelloWorld.java */
    public class HelloWorld{
    	public static void main(String[] args){
        	System.out.println("Hello World!");
        }
    }

This can be called from the command line. The javac command compiles the bytecode(?) file. The java command runs the program.

	> javac HelloWorld.java
	> java HelloWorld

You can also pass arguments from the CL.

	> java HelloWorld bruce
	
These arguments can be access from the args array.

	system.out.print(args[0]);
	
You can examine the class file from the command line.

	od -x HelloWorld.class
	
od stands for octal dump.

### Data Types

A data type is basically a set of value and a set of operations that can be carried out on the values. e.g. the int datatype is the set of integers and a set of operations such as +, - etc.

Java has 8 built in data types: int, char, long, double, boolean, byte, short, float, plus String.

	int a, b, c;

This declares three variables a, b and c of type int.

Type conversion can be explicit of sometime automatic.