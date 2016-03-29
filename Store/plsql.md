# PL/SQL

SQL is a set-oriented language that manipulates the contents of a relational database. But SQL can't be used to implement all the business logic required of an application.

PL/SQL offers a set of procedural command that extend SQL. With PL you can combine SQL with loops, if statements, variables and such.

PL is block-structured language, defined by the keywords DECLARE, BEGIN, EXCEPTION and END, which break the program up into three sections.

1. Declarative: statements that declare variables, constants and other code elements.
2. Executable: statements that are run when the block is executed.
3. Exception handlers: to catch any exceptions that are raised when executable runs.

Only executable is mandatory.

Hello World:

	BEGIN
		DBMS_OUTPUT.put_line ('Hello World');
	END;

Declaring a variable:

	DECLARE
		l_message
		VARCHAR2 (100) := 'Hello World!';
	BEGIN
		DBMS_OUTPUT.put_line(l_message);
	END;
	

Blocks can be nested in other blocks:

	DECLARE
		l_message
		VARCHAR (100) := 'Hello';
	BEGIN
		DECLARE
			l_message2
			VARCHAR (100) := l_message || ' World 3';
		BEGIN
			DBMS_OUTPUT.put_line (l_message2);
		END;
	END;
	
These blocks have been anonymous. In PL you can hide complexity by naming the block and creating sub-programs (procedures or functions).

Named block (subprogram):

	CREATE OR REPLACE PROCEDURE
	hello_world
	IS
		l_message
		VARCHAR2 (100) := 'Hello World 3!';
	BEGIN
		DBMS_OUTPUT.put_line (l_message);
	END hello_world;

Subprograms sometimes need parameters.

	CREATE OR REPLACE PROCEDURE
	hello_place (place_in IN VARCHAR2)
	IS
		l_message VARCHAR2 (100);
	BEGIN
		l_message := 'Hello ' || place_in;
		DBMS_OUTPUT.put_line (l_message);
	END hello_place;
	
Try this out like so:

	BEGIN
		hello_place ('World');
		hello_place ('Universe');
	END;
	
Procedures/functions can take multiple parameters. They all follow the same basic form:

	procedure_name(parameter_name parameter_mode   datatype)
	
Functions take value(s), process them, then return the result. They are set up similar to procedures.

	CREATE OR REPLACE FUNCTION
	hello_message (place_in IN VARCHAR2)
	RETURN VARCHAR2
	IS
	BEGIN
		RETURN 'Hello ' || place_in;
	END hello_message;

Once created this can be used like so:

	select hello_message('World')
	from dual;

Usually it is simple enough to write the SQL statement directly in the block, then add the code needed to interface between the SQL statement and PL/SQL code.

	DECLARE
		l_name employees.last_name%TYPE;
	BEGIN
		SELECT last_name
			INTO l_name
		FROM employees
		WHERE employess_id = 138;
		
		DBMS_OUTPUT.put_line (l_name);
	END;

Note, when delaring the variable l\_name we 'anchored' the datatype back to a table's column. I guess this ensures that the datatypes always match.

INTO places the last\_name in the l\_name variable.


http://www.oracle.com/technetwork/issue-archive/2011/11-mar/o21plsql-242570.html