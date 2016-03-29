# Express

* http://expressjs.com/
 
Express is a "Fast, unopinionated, minimalist web framework for Node.js".

## Basics

It can be installed via NPM.

    npm init // sets up config for NPM. set entry point: (index.js)
    npm install express --save // install locally and includes in config

The express generator lets you get started with a framework for your project.

    npm install express-generator -g // install globally
    express myapp
    cd myapp
    npm install // installs all dependencies
    DEBUG=myapp: * npm start // starts application
    
Sets up a project with the following structure:

├── app.js
├── bin
│   └── www
├── package.json
├── public
│   ├── images
│   ├── javascripts
│   └── stylesheets
│       └── style.css
├── routes
│   ├── index.js
│   └── users.js
└── views
    ├── error.jade
    ├── index.jade
    └── layout.jade

## Routing

Routing determines how the app responds to a client request to an endpoint (path) and a specific method (GET, POST etc).

Each route can have one or more handler functions which are executed when the route is matched.

> app.METHOD(PATH, HANDLER)

* app is an instance of express
* METHOD is a request method (GET, POST, DELETE etc)
* PATH is a path on the server.
* HANDLER is the function executed.
 

    app.get('/', function(req, res) {
        res.send('Hello World!');
    });
    
Static files (images, CSS etc) use the express.static middleware.

    app.use(express.static('public'));
    
This lets you use all files in public directory. e.g:

    http://localhost:3000/images/kitten.jpg
    http://localhost:3000/css/style.css
    http://localhost:3000/js/app.js

Loads the files that are in the public directory.

To create a virtual path for these files specify a 'mount path' for the directory.

    app.use('/static', express.static('public'));
    
So you would use:

    http://localhost:3000/static/images/kitten.jpg
    http://localhost:3000/static/css/style.css
    http://localhost:3000/static/js/app.js
    
It can be safer to use the absolute path.

    app.use('/static', express.static(__dirname + '/public'));
    
__dirname is the name of the directory that the currently executing script resides in. 

## Templating

A template engine uses static tempalte files and, at runtime, replaces the variables in the template with actual values.

Express works with any template engine. [Jade](http://jade-lang.com/) seems to be the default set up by express-generator. The views directory contains template files. 

These are defined in the app.js file:

    app.set('views', path.join(__dirname, 'views'));
    app.set('view engine', 'jade');
    
Jade template look something like this.
    
    html
      head
        title= title
      body
        h1= message

The code for rendering the template is in the router.

    app.get('/', function(req, res){
        res.render('index', {title: 'Hey', message: "Hello There!"});
    });
    
In Jade, Templates can be modular by extending a base template. e.g.

layout.jade:

    doctype html
    html
      head
        title= title
        link(rel='stylesheet', href='/stylesheets/style.css')
      body
        block content

index.jade:

    extends layout
    
    block content
      h1= title
      p Welcome to #{title}

    
## Middlewear

## Error Handling

