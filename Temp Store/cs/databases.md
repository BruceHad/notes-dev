# Relational Database

A relational database stores information about data and how it is related.

Represented in flat, two dimensional tables that preserve relational structuring.

The RDBMS is the physical and logical implementation of the RDB, controlling reads, writes, updates and processing.

The data is formally described according to the DBs relational model (schema).

RDBs tend to be normalised or de-normalised. Normalised DBs have better data integrity, reduced storage space (?), and faster transmissions. Useful for transactional databases.

De-normalisation can improve performance (of reads presumably). Useful for analytic dbs.

Each db is a collection of related tables. A table consists of columns (fields/attributes) and rows (records/tuples containing values).

Relationships exist between the columns of a table and between tables.

* One to One
* One to Many
* Many to Many

Most tables have only one value per cell. In this case there is only a one-to-one relationship within a table.

Tables will usually have a unique, primary key (PK), often generated automatically, that is used to access the record. Performance can be optimised for PKs. Natural keys may also be identified and defined as alternative keys (AK) (sometimes several columns combined). These keys uniquely identify the row.

# ACID

Atomicity, Consistency, Isolation and Durability is a set of properties that guarantee database transactions are processed reliably. 

A single logical operation on the data is called a transaction e.g. transferring funds from one account to another is a single transaction, even if it involves multiple changes.

Atomicity - no partial failures. If any part of a transaction fails, the whole transaction fails.

Consistency - no invalid states. Each transaction moves from a valid state, to a different valid state.

Isolation - concurrent execution of transactions result in a system state that would be obtained if transactions were executed serially.

Durability - Once a transaction has been committed it will be stored permanently and remain so even in the event of a crash or power loss.

# Normalisation

Normal Forms represent guidelines for record desing for relational databases. Normalisation rules are designed to prevent update anomalies and data inconsistencies. With respect to performance tradeoff, these guidelines are biased towards the assumption that all non-key fields will be updated frequently. 

They tend to penalise retrieval since data that may have been retrievable from one one record may have to be retrieved from multiple records in a normalised database. 

## First Normal Form

All records must contain the same number of fields. 

None of the domains of that relation should have elements which are themselves sets [Codd]

A table is in the first normal form if [Chris Date]:

* There's no top-to-bottom ordering to the rows.
* There's no left-to-right ordering to the columns.
* There are no duplicate rows.
* Every row-and-column intersection contains exactly one value from the applicable domain (and nothing else).
* All columns are regular [i.e. rows have no hidden components such as row IDs, object IDs, or hidden timestamps].

## Second Normal Form

Both second and third normal forms deal with the relationship between key and non key field (and only that non-key field). Non key fields must provide a fact about a key. 

The second normal form is violated when a non-key field is a fact about a subset of a key (it is only relevant when the key is composite).

This shows up when redundant, repeated data appears in a table. e.g. 

--------------------------------------------------
| PART | WAREHOUSE | QUANTITY | WAREHOUSE-ADDRESS |
--------------------------------------------------

The warehouse-address will be repeated multiple times. There is also a risk that if a warehouse is empty, you lose the address of that warehouse.

This can be normalised into two tables: Parts and Warehouses.

## Third Normal Form

Third normal form is violated when a non-key field is in fact about another non-key field.

-----------------------------------
| EMPLOYEE | DEPARTMENT | LOCATION |
-----------------------------------

IN this example Location is a fact about both employee and department. This has similar problems to the second normal form violation and can be solved in a similar way.


http://www.bkent.net/Doc/simple5.htm

https://en.wikipedia.org/wiki/Relational_database