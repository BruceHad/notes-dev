# Javascript Support Tools

## Browserify

01/04/2016

https://github.com/substack/browserify-handbook
https://github.com/substack/node-browserify
https://en.wikipedia.org/wiki/CommonJS
http://browserify.org/

Browserify is a tool for compiling 'node-flavoured' commonjs modules for the browser. You can use it for organising code and using third party libraries. The module system is the same as _node_. 

## Help

You can install the handbook with:
    
    npm install -g browserify-handbook

Then the _browserify-handbook_ will open the document.

## Modules and Require (CommonJS)

There is a _require()_ function for loading code from other files (usually installed with npm).

    > npm install uniq
    
Then:

    var uniq = require('uniq');
    
You can also include other js files.

    var foo = require('./foo.js');
    
Relative paths are resolved with respect to the invoking file's location.

_require()_ returns the _exports_ of the module name that you specify.

## Exports

For other files to import (require) something (any value/function or whatever), it must be exported, assigned to the module.exports.

    module.exports = function(n){
        return n*111;
    }

Then, when required, that function will be assigned to the variable.

_module.exports_ is the same as _exports_ and is initially set to an empty object. So you can also export using the form:

    module.exports.beep = function (n) { return n * 1000 }
    module.exports.boop = 555

## Bundling for the Browser

In node you can run a file like:

    > node foo.js

In browserify they can do something similar, except you are generating a stream of concatenated js files on stdout using the > operator.

    > browserify foo.js > bundle.js
    
Now bar.js contains all the javascript and can be used in the browser.

    <html>
      <body>
        <script src="bundle.js"></script>
      </body>
    </html>

If you put the script tag right before the closing _</body>_ tag, you can use all the dom elements without waiting for the onready event.



## Auto Recompile

Various tools to support the automatic compilation of the bundle file. Some support live-reloading.

### Watchify

You can use _watchify_ interchangeably with browserify. It will compile the bundle, then watch for changes to any file int he dependency graph and recompile.

    > watchify browser.js -d -o static/bundle.js -v
    
Configuration for using watchify and browerify with the package.json "scripts" field.

    {
      "build": "browserify browser.js -o static/bundle.js",
      "watch": "watchify browser.js -o static/bundle.js --debug --verbose",
    }

To build the bundle, do _npm run build_ and to watch files during development do _npm run watch_.

### Beefy

Beefy with set up a server that automatically recompliles your code when you modify it.

    beefy main.js

### browserify-middleware, enchilada

If you are using express, browserify-middleware or enchilda can provide middleware for serving browserify bundles.

## Using with Gulp

https://github.com/gulpjs/gulp/blob/master/docs/recipes/fast-browserify-builds-with-watchify.md

Watchify doesn't have a gulp plugin, you can use vinyl-source-stream to pipe the bundle stream into your gulp pipiline.

    'use strict';
    
    var watchify = require('watchify');
    var browserify = require('browserify');
    var gulp = require('gulp');
    var source = require('vinyl-source-stream');
    var buffer = require('vinyl-buffer');
    var gutil = require('gulp-util');
    var sourcemaps = require('gulp-sourcemaps');
    var assign = require('lodash.assign');
    
    // add custom browserify options here
    var customOpts = {
      entries: ['./src/index.js'],
      debug: true
    };
    var opts = assign({}, watchify.args, customOpts);
    var b = watchify(browserify(opts)); 
    
    // add transformations here
    // i.e. b.transform(coffeeify);
    
    gulp.task('js', bundle); // so you can run `gulp js` to build the file
    b.on('update', bundle); // on any dep update, runs the bundler
    b.on('log', gutil.log); // output build logs to terminal
    
    function bundle() {
      return b.bundle()
        // log errors if they happen
        .on('error', gutil.log.bind(gutil, 'Browserify Error'))
        .pipe(source('bundle.js'))
        // optional, remove if you don't need to buffer file contents
        .pipe(buffer())
        // optional, remove if you dont want sourcemaps
        .pipe(sourcemaps.init({loadMaps: true})) // loads map from browserify file
           // Add transformation tasks to the pipeline here.
        .pipe(sourcemaps.write('./')) // writes .map file
        .pipe(gulp.dest('./dist'));
    }   


