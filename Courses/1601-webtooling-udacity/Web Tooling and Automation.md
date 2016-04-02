# Web Tooling & Automation

## 1. Introduction

* Development environment

* Build Process

* Live Coding

* Automatic Optimisations

This course is all about using tools that help optimise your workflow, saving you from the grunt work. It’s important to assess what optimisations are worthwhile, checking time spent versus time saved.

Failure Modes:

* "I can build a better tool myself" (don’t reinvent the wheel, unless you want to learn how wheels work).

* Choosing a new and shiny tool because it is said to be faster is a false optimisation. Tried and tested tools are generally, better supported and more likely to stay around.

* With tools that promise to do it all, run. Don’t buy into an ecosystem you can’t escape from.

* Avoid optimisations that aren’t worth it.

## 2. Productive Editing

Setting up the development environment (mainly the editor).

IDE vs Editor

Integrated Development Environments are tools that try to do anything. In certain fields (e.g. mobile app development) there is a standard IDE that is part of the controlled platform. On the web, most developers ‘embrace’ the chaos and mix and match specialised tools for the jobs.

In this course, using Sublime Text 3. This a popular, but paid for text editor. Free alternatives include Atom (Github). Shortcuts:

* Ctrl-T - fuzzy file finder. CTRL-P - Quick open files by name.

    * Using the @ symbol (CTRL-R) simple search.

* CTRL-ALT-G - Find next instance.

* Tab expands out tags.

* Column selection (Alt-drag cursor)

* CTRL-D - add next instance to selection.

* There should be a way of selecting all instances (Find should work)

### Extending the Editor

Editors can expand functionality.

First thing to do is install package control. This is the only time you have to manually install. Copy and paste the package control code to ST’s terminal.

ctrl + shift + p brings up the command palette. Contains all the actions sublime can do. Including ‘install package’.

Install:

* Emmet - enhances sublimes snippets (shorthand).

* Sidebar Enhancements - improved the contextual menu for the sidebar.

* Color Picker (ctrl + shift + c)

* Color Highlighter

Remember to restart the editor.

## 3. Build Tools

Tools that you feed tasks, that they then carry out automatically. Web dev specific build tools are fairly new (even though they’ve been around for years in other fields).

Simple build tool is just a shell/bash script. The original build tool MAKE added file management stuff to the bash scripts.

Web development build tools are generally JS/Node based. Popular tools are Grunt and Gulp.

* A build tool should be fast in execution: instant re-load changes.
* Strong community.
* Modular.

Grunt (popular) has a strong community with a lot of users and has a lot of plugins. Gulp is built for speed and can carry out multiple tasks in parallel. Converts open files into streams internally. Chooses code over configuration.

With grunt and other build tools, temporary files are created and worked on. This creates a file/io overhead that slows stuff down. Gulp uses an ‘in memory stream’ so the io is only done twice (start and end).

### Gulp

Install Gulp:

https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md

1. Install gulp globally: $ npm install --global gulp
2. Or, preferably, install gulp in your project devDependencies: $ npm install --save-dev gulp
3. Create a gulpfile.js at the root of your project:

gulpfile.js:

  var gulp = require('gulp');
  gulp.task('default', function() {
    // place code for your default task here
  });

4. Run gulp: $ gulp

The default task will run and do nothing. To run individual tasks, use gulp <task> <othertask>.

### Using Build Tools to make CSS suck less

_SASS_ is a CSS preprocessor. And _Autoprefixer_ automatically sets the correct browser prefixes.

Both these have Gulp plugins.

  npm install gulp-sass

Now we can use Gulp to convert the SASS files to CSS.

First we need a project folder:

project/
	css/
	sass/
	js/
	node_modules/
	index.html
	gulpfile.js

The sass/ folder should contain some scss files.

Now edit the gulpfile.

  var gulp = require('gulp');
  var sass = require('gulp-sass');

  gulp.task('default', function(){
    console.log("Gulped!")
  });
  gulp.task('styles', function(){
    gulp.src('sass/**/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./css'));
  });

Now running gulp styles at the command line should build the css files from the .scss files.

Now install auto-prefixer.

  npm install --save-dev gulp-autoprefixer

Now we include autoprefixer in our gulpfile and add an new instruction to our pipe stream, so that auto-prefixer is run. This example provides prefixes for the last 2 versions of browsers.

  var gulp = require('gulp');
  var sass = require('gulp-sass');
  var autoprefixer = require('gulp-autoprefixer');

  gulp.task('default', function(){
    gulp.watch('sass/**/*.scss', ['style'])
  });

  gulp.task('styles', function(){
    gulp.src('sass/**/*.scss')
      .pipe(sass().on('error', sass.logError))
      .pipe(autoprefixer({
        browsers: ['last 2 versions']
      }))
      .pipe(gulp.dest('./css'));
  });

Now we can test it out. In our main.scss files find the img selector that has all the webkit prefixes and remove the prefixes.

Now run gulp styles again at the terminal. Check the generated .css files and they should have the webkit prefixes added.

### Gulp 'Watch'

Gulp has a feature called watch, which is an automatic trigger that looks for changes in your files and triggers and action. Save you having to run gulp from the cl everytime you want to build.

We can include this in our 'default' action like so.

  gulp.task('default', function(){
    gulp.watch('sass/**/*.scss', ['styles'])
  });

So this is looking for any changes to .scss files, then running the 'callback' function, the 'styles' task we defined earlier.

To run the default run gulp command from the cl, and from then on the watcher will be running, and any changes you make to the .scss file will trigger the 'styles' task.

## 4. Live Editing

Live Editing saves the repeated cycle of save - build - refresh to check changes you have made. It does this by setting a watcher to look for changes to your files, that communicates with a watcher in the browser, that refreshes or updates the page on the fly.

There are three methods shown here:

1. On each keystroke in the editor.
2. On each save (via Gulp).
3. Skipping the editor and doing live editing within the browser itself.

There are various methods for editing within the browser itself, including Brackets, Takana and the workspaces feature of the Chrome dev tools. The issue with this method is that it doesn't hook up to your build tools.

BrowserSync is a live editing plugin that works alongside the build tool. It can use the 'watch' task that we used earlier.

BrowserSync creates a proxy webserver that servers and tracks file changes. It is compatible with most node build tools.

1. Install browser sync:

  npm install browser-sync --save-dev

2. Create a browser-sync object and initialize the server.

  var browserSync = require('browser-sync').create();
  browserSync.init({
      server: "./"
  });
  browserSync.stream();

3. Run gulp in Terminal, see how browser opens with the page open.

This doesn't seem to do much, but following the (instructions here)[https://www.browsersync.io/docs/gulp/] got me up and running with live editing of HTML and CSS.

The gulpfile I ended up with is below. Running the gulp command, runs the 'default' task.

1. Launches the browserSync server.
2. Sets a watcher for sass files and runs the 'styles' task on any change.
3. Sets a watcher for HTML, and reloads the browser on change.
3. And the 'styles' task does what it did before, with the additional command, which seems to refresh the browser after changes have been made.

Basic live editing seems to work. Probably requires some modification to get running smoothly.

  var gulp = require('gulp');
  var sass = require('gulp-sass');
  var autoprefixer = require('gulp-autoprefixer');
  var browserSync = require('browser-sync').create();

  gulp.task('default', function(){

    browserSync.init({
      server: {
          baseDir: "./"
      }
    });

    gulp.watch('sass/**/*.scss', ['styles']);
    gulp.watch("*.html").on('change', browserSync.reload);

  });

  gulp.task('styles', function(){
    gulp.src('sass/**/*.scss')
      .pipe(sass().on('error', sass.logError))
      .pipe(autoprefixer({
        browsers: ['last 2 versions']
      }))
      .pipe(gulp.dest('./css'))
      .pipe(browserSync.stream());
  });

### Live Editing Node App

## 5. Preventing Distaster (Linting, Testing)

### Linting

Using the right tools can heavily improve the quality of you code.

Linting is a way to check you JS code for errors. I can be done via your editor, your build process, or a hook in your version control.

Linting can be heavily opinionated (no right or wrong so configure towards your style).

Code style linting

Syntax linting

There are three popular linting tools for JS: JSlint, JSCS and ESLint. We'll stick with ESLint here.

Linting helps:

* Code style problems
* Eliminate dead code or variables.

Setting up eslint in Sublime Text.

    npm install -g eslint

Now install sublime-linter and sublime-linter-eslint.

Eslint doesn't do anything until you configure it.

    eslint --init

This takes you through a wee wizard to configure eslint. It creates a eslintrc.js file with all the configuration details. You can have a local .eslintrc file that overrides the global settings.

You can also set local eslint configration in the file you are editing. So, for example, you can have different linting for your nodejs files than for your browser files.

In a comment on the file enter:

    /*eslint-env node*/

eslint can also be added to the Gulp build file.

    npm install gulp-eslint

Then in the gulpfile you need to include the package.

    var eslint = require('gulp-eslint');

    gulp.task('default', ['styles', 'lint'], function() {
      gulp.watch('sass/**/*.scss', ['styles']);
      gulp.watch('js/**/*.js', ['lint']);

      browserSync.init({
        server: './'
      });
    });

    gulp.task('lint', function () {
      return gulp.src(['js/**/*.js'])
        // eslint() attaches the lint output to the eslint property
        // of the file object so it can be used by other modules.
        .pipe(eslint())
        // eslint.format() outputs the lint results to the console.
        // Alternatively use eslint.formatEach() (see Docs).
        .pipe(eslint.format())
        // To have the process exit with an error code (1) on
        // lint error, return the stream and pipe to failOnError last.
        .pipe(eslint.failOnError());
    });

### Unit Testing

Unit test create the functionality of the code. 

Tests can be automated. But tests have to be run in the browser.

[Jasmine](http://jasmine.github.io/) uses a _headless browser_ for testing. _PhantomJs_ is a headless version of webkit.

So phantom has to be installed first.

Download from phantomjs website the prebuilt package : http://phantomjs.org/download.html then open a terminal and go to the Downloads folder

    sudo mv phantomjs-1.8.1-linux-x86_64.tar.bz2 /usr/local/share/.
    cd /usr/local/share/
    sudo tar xjf phantomjs-1.8.1-linux-x86_64.tar.bz2
    sudo ln -s /usr/local/share/phantomjs-1.8.1-linux-x86_64 /usr/local/share/phantomjs
    sudo ln -s /usr/local/share/phantomjs/bin/phantomjs /usr/local/bin/phantomjs
    phantomjs --version
    > 2.1.1

Now install gulp phantom

    npm install gulp-jasmine-phantom

Now add the appropriate require to your gulpfile.

    var jasmine = require('gulp-jasmine-phantom');

Now we can create a new task called tests:

    gulp.task('tests', function(){
        gulp.src('tests/spec/extraSpec.js')
        .pipe(jasmine({
            integration: true,
            vendor: 'js/**/*.js'
            }));
        });

Now it can be run as usual using 

    gulp tests

If you look at the tests:

    describe('window height', function() {
        it('returns window height', function() {
            expect(getWindowHeight()).toEqual(jasmine.any(Number));
        });
    });

Testing is covered in another course though.

Since it's slow to run tests, they don't get integrated with the default build tasks.

### Continuous Integration

Continuous integration in the cloud is making sure your code can always be integrated with the repository, so you always have a stable build.

Dev ops is covered in another course.

CI is a good place to run unit tests.

A cloud solution like jenkins watches the commits, and triggers terminal commands. So the test suite can run on every commit. Then emails if it fails.

## 6. Optimisations

Release, you can minify and concatenate the code. The build process can automate this.

 
