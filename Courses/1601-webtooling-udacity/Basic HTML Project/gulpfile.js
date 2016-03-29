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
