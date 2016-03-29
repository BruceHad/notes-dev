## MongoDB

https://docs.mongodb.org/getting-started/shell/introduction/

Not used MongoDB.

A record in MongoDB is a document, which is a data structure composed of field/value pairs. Similar to json objects. Fields may include other documents, arrays and arrays of documents. Difference seems to be that documents appear to have an "_id" field in the root. This acts as a primary key.

Documents are stored in collections, which are analogous to tables in an RDB. Unlike a table though, a collections does not require its documents to have the same schema.

### Install

Mongo can be installed from Synaptic. The website claims these are out of date, and suggests using the .deb files provided, but I avoided that.

To start, start the mongod.

    sudo service mongod start
    sudo service mongod stop

Apparently, except that didn't work for me, and mongo seems to be running after install.

Need to install a MongoDB driver for Node.

    npm install mongdb --save

And in node:

    var MongoClient = require('mongodb').MongoClient;
    var assert = require('assert');

Connect to a running mongodb instance by specifying the MongoDB url. 

    var url = 'mongodb://localhost:27017/test';
    MongoClient.connect(url, function(err, db) {
      assert.equal(null, err);
      console.log("Connected correctly to server.");
      db.close();
    });

MongoDB documents are BSON documents, which is a binary representation of JSON, with additional type information. The value of a field can be any BSON data types, including documents, arrays and arrays of documents.

* string
* integer
* double
* date
* byte array
* boolean
* null
* BSON object
* BSON array

https://en.wikipedia.org/wiki/BSON

Documents are kinda like rows or records in a standard database. Documents are stored in collections, which are kinda like tables, a group of related documents _that share common indexes_.

**A MongoDB query** targers a specific collection of documents. A query may include a _projection_ that specifies the field from the matching document to return (select). You can also impose limits, skips and sort orders.

    db.users.find({age: {$gt: 18}}).sort({age: 1})

**Data Modification** refers to create, update, delete operations. These operate on a single collection.

    db.users.insert(
        {
            name: "sue",
            age: 26,
            status: "A",
            groups: ["news", "sports"]
        }
    )

* use mydb //this switches to the database you want to query
* show collections //this command will list all collections in the database
* db.collectionName.find().pretty() //this will show all documents in the database in a readable format; do the same for each collection in the database

http://blog.modulus.io/mongodb-tutorial
http://www.mkyong.com/mongodb/how-to-create-database-or-collection-in-mongodb/

Once installed, include the mongodb module and open a connection.

    > npm install mongodb

    var mongodb = require('mongodb');
    var MongoClient = mongodb.MongoClient;

    var url = 'mongodb://localhost:27017/db_name';

    MongoClient.connect(url, function(err, db){
        if(err)
            console.log('Unable to connect to the mongoDB server:', err);
        else{
            console.log('Connection established.');
            db.close();
        }
    });

The mongodb driver for NodeJS:

1. Keeps query function names and parameters similar to MongoDB commands.
2. All functions take callback as their last argument. The callback has arguments error and result. result is similar to the result of running the query on MongoDB directly.


### Inserting Data

    // Get the documents collection
    var collection = db.collection('users');

    //Create some users
    var user1 = {name: 'modulus admin', age: 42, roles: ['admin', 'moderator', 'user']};
    var user2 = {name: 'modulus user', age: 22, roles: ['user']};
    var user3 = {name: 'modulus super admin', age: 92, roles: ['super-admin', 'admin', 'moderator', 'user']};

    // Insert some users
    collection.insert([user1, user2, user3], function (err, result) {
      if (err) {
        console.log(err);
      } else {
        console.log('Inserted %d documents into the "users" collection. The documents inserted with "_id" are:', result.length, result);
      }

If the 'users' collection doesn't exist, it is created on the first insert.

The records to be inserted are simple js objects.

collection.insert() inserted all the data into the collection.

### Updating

    // Get the documents collection
    var collection = db.collection('users');

    // Insert some users
    collection.update({name: 'modulus user'}, {$set: {enabled: false}}, function (err, numUpdated) {
      if (err) {
        console.log(err);
      } else if (numUpdated) {
        console.log('Updated Successfully %d document(s).', numUpdated);
      } else {
        console.log('No document found with defined "find" criteria!');
      }
      //Close connection
      db.close();
    });

The collection.update() updates records.

The first argument seems to identify the record, based on name.
The second arguments contains a $set record, changing enable to false.

Finally there is a callback with err and numUpdate argument, which presumably counts the number of records updated.

### Querying

collection.find() can be used to query the database. This returns a db cursor. MongoDB doesn't return the full results by default. The toArray function tells the drive that we want the full data for each user.

        // Get the documents collection
        var collection = db.collection('users');

        // Insert some users
        collection.find({name: 'modulus user'}).toArray(function (err, result) {
          if (err) {
            console.log(err);
          } else if (result.length) {
            console.log('Found:', result);
          } else {
            console.log('No document(s) found with defined "find" criteria!');
          }
          //Close connection
          db.close();
        });
      }
    });

Example using the cursor.

    var collection = db.collection('users');

    //We have a cursor now with our find criteria
    var cursor = collection.find({name: 'modulus user'});

    //We need to sort by age descending
    cursor.sort({age: -1});

    //Limit to max 10 records
    cursor.limit(10);

    //Skip specified records. 0 for skipping 0 records.
    cursor.skip(0);

    //Lets iterate on the result
    cursor.each(function (err, doc) {
      if (err) {
        console.log(err);
      } else {
        console.log('Fetched:', doc);
      }
    });


