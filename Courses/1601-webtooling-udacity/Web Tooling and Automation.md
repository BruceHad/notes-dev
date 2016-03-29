# Web Tooling & Automation

## Introduction

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

## Productive Editing

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

## Extending the Editor

Editors can expand functionality.

First thing to do is install package control. This is the only time you have to manually install. Copy and paste the package control code to ST’s terminal.

ctrl + shift + p brings up the command palette. Contains all the actions sublime can do. Including ‘install package’.

Install:

* Emmet - enhances sublimes snippets (shorthand).

* Sidebar Enhancements - improved the contextual menu for the sidebar.

* Color Picker (ctrl + shift + c)

* Color Highlighter

Remember to restart the editor.

## Build Tools

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

## Using Build Tools to make CSS suck less

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

## Gulp 'Watch'

Gulp has a feature called watch, which is an automatic trigger that looks for changes in your files and triggers and action. Save you having to run gulp from the cl everytime you want to build.

We can include this in our 'default' action like so.

  gulp.task('default', function(){
    gulp.watch('sass/**/*.scss', ['styles'])
  });

So this is looking for any changes to .scss files, then running the 'callback' function, the 'styles' task we defined earlier.

To run the default run gulp command from the cl, and from then on the watcher will be running, and any changes you make to the .scss file will trigger the 'styles' task.

## Live Editing

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

## Live Editing Node App



