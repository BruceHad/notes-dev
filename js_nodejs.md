# Getting Started with NodeJS

A barebones Node.js app using [Express 4](http://expressjs.com/).

This application supports the [Getting Started with Node on Heroku](https://devcenter.heroku.com/articles/getting-started-with-nodejs) article - check it out.

## Running Locally

Make sure you have [Node.js](http://nodejs.org/) and the [Heroku Toolbelt](https://toolbelt.heroku.com/) installed.

```sh
$ git clone git@github.com:heroku/node-js-getting-started.git # or clone your own fork
$ cd node-js-getting-started
$ npm install
$ npm start
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```
$ heroku create
$ git push heroku master
$ heroku open
```
or

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Node.js on Heroku, see these Dev Center articles:

- [Getting Started with Node.js on Heroku](https://devcenter.heroku.com/articles/getting-started-with-nodejs)
- [Heroku Node.js Support](https://devcenter.heroku.com/articles/nodejs-support)
- [Node.js on Heroku](https://devcenter.heroku.com/categories/nodejs)
- [Best Practices for Node.js Development](https://devcenter.heroku.com/articles/node-best-practices)
- [Using WebSockets on Heroku with Node.js](https://devcenter.heroku.com/articles/node-websockets)

# Testing Node

http://mherman.org/blog/2015/09/10/testing-node-js-with-mocha-and-chai/
https://mochajs.org/
http://chaijs.com/api/bdd/
https://en.wikipedia.org/wiki/Behavior-driven_development

We've grabbed a test application from https://github.com/mjhea0/node-mocha-chai-tutorial.git and installed mocha and dependencies:

    npm install

Then set up a test/ folder with a test-server.js file:

    describe('Blobs', function() {
      it('should list ALL blobs on /blobs GET');
      it('should list a SINGLE blob on /blob/<id> GET');
      it('should add a SINGLE blob on /blobs POST');
      it('should update a SINGLE blob on /blob/<id> PUT');
      it('should delete a SINGLE blob on /blob/<id> DELETE');
    });

This is boilerplate Mocha test code.

* describe() - groups tests
* it() - individual test cases that test one feature or situation.

Mocha can use any assertion library. In this case we install chai.

    npm install chai@3.2.0 chai-http@1.0.0 --save-dev
    
And include it in our test code, requiring both chai and chai-http and our app.js file.

    var chai = require('chai');
    var chaiHttp = require('chai-http');
    var server = require('../server/app');
    var should = chai.should();
    chai.use(chaiHttp);

Chai allows you to choose the style of assertion you choose. The _should_ assertion library uses BDD style assertions. BDD stands for Behavior Driven Development. It comes from TDD, and combines the general techniques of TDD with principles from 'Domain Driven Design' and OOAD.

In Chai the BDD styles are _expect_ and _should_. Both use the same chainable language to construct assertions. These include chainable getters to improved the readability of assertions, such as to, be and is. For example:

    expect(foo).to.not.equal('bar');
    expect(foo).to.be.a('string');
    foo.should.be.a('string');
    foo.should.equal('bar');
    
Now our first test statement (it()) becomes:

    it('should list ALL blobs on /blobs GET', function(done) {
      chai.request(server)
        .get('/blobs')
        .end(function(err, res){
          res.should.have.status(200);
          res.should.be.json;
          res.body.should.be.a('array');
          done();
        });
    });

This test passes an anon function to the it() statement. It makes a GET request to the /blobs endpoint and then asserted that
1. The response contained a [200 http status](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#2xx_Success). 
2. The result is json.
3. The result body is an array.

To run tests:
    
    mocha // if mocha is installed globally.
    node node_modules/.bin/mocha // if it is installed locally.
    
Alternatively we can add the test script to the package.json file.

    "scripts": {
        "test": "mocha"
    }
    
Then we can run it with npm:

    npm test
    
We can also test POST requests:

    it('should add a SINGLE blob on /blobs POST', function(done) {
      chai.request(server)
        .post('/blobs')
        .send({'name': 'Java', 'lastName': 'Script'})
        .end(function(err, res){
          res.should.have.status(200);
          res.should.be.json;
          res.body.should.be.a('object');
          res.body.should.have.property('SUCCESS');
          res.body.SUCCESS.should.be.a('object');
          res.body.SUCCESS.should.have.property('name');
          res.body.SUCCESS.should.have.property('lastName');
          res.body.SUCCESS.should.have.property('_id');
          res.body.SUCCESS.name.should.equal('Java');
          res.body.SUCCESS.lastName.should.equal('Script');
          done();
        });
    });

## Test Database

The tests above use the main database for testing. Alternatively we can set up a test database, add a dummy blob to it.The

This uses _hooks_.

The beforeEach() and aferEach() hooks add and remove a dummy document to the database before and after each test case is ran.

server/_config.js:

    var config = {};

    config.mongoURI = {
      development: 'mongodb://0.0.0.0/node-testing',
      test: 'mongodb://0.0.0.0/node-test'
    };
    
    module.exports = config;

And update app.js:

    // *** config file *** //
    var config = require('./_config');
    
    // *** mongoose *** ///
    mongoose.connect(config.mongoURI[app.settings.env], function(err, res) {
      if(err) {
        console.log('Error connecting to the database. ' + err);
      } else {
        console.log('Connected to Database: ' + config.mongoURI[app.settings.env]);
      }
    });

And remember to update the test script to indicate the environment to use:

    process.env.NODE_ENV = 'test';
    
Now you can add the hooks to the test script.

    describe('Blobs', function() {
    
      Blob.collection.drop();
    
      beforeEach(function(done){
        var newBlob = new Blob({
          name: 'Bat',
          lastName: 'man'
        });
        newBlob.save(function(err) {
          done();
        });
      });
      afterEach(function(done){
        Blob.collection.drop();
        done();
      });
      ...

Now before each test case the database is cleared and a new blob is added. And after each test, the database is cleared.
