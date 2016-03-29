# Wordpress Templates and Themes

Through its Theme system, WordPress allows you to define as few or as many Templates as you like all under one Theme. Each of these Template files can be configured for use under specific situations.

WordPress Themes are files that work together to create the design and functionality of a WordPress site. Each Theme may be different, offering many choices for site owners to instantly change their website look.

WordPress Themes should be coded using the following standards:

* Use well-structured, error-free PHP and valid HTML.
* Use clean, valid CSS. 
* Follow design guidelines in Site Design and Layout.

WordPress Themes live in wp-content/themes/. 

The Theme's subdirectory holds all of the Theme's stylesheet files, template files, and optional functions file (functions.php), JavaScript files, and images.

## Style.css

In addition to CSS style information for your theme, style.css provides details about the Theme in the form of comments. The stylesheet must provide details about the Theme in the form of comments. e.g.

    /*
    Theme Name: Twenty Ten
    Theme URI: http://wordpress.org/
    Description: The 2010 default theme for WordPress.
    Author: wordpressdotorg
    Author URI: http://wordpress.org/
    Version: 1.0
    Tags: black, blue, white, two-columns, fixed-width, custom-header, custom-background, threaded-comments, sticky-post, translation-ready, microformats, rtl-language-support, editor-style, custom-menu (optional)
    
    License:
    License URI:
    
    General comments (optional).
    */

The comment header lines in style.css are required for WordPress to be able to identify a Theme and display it in the Administration Panel under Design > Themes.

## Functions.php

A theme can optionally use a functions file, which resides in the theme subdirectory and is named functions.php. This file basically acts like a plugin, and if it is present in the theme you are using, it is automatically loaded during WordPress initialization.

* Enable Theme Features such as Sidebars, Navigation Menus, Post Thumbnails, Post Formats, Custom Headers, Custom Backgrounds and others.
* Define functions used in several template files of your theme.
* Set up an options menu, giving site owners options for colors, styles, and other aspects of your theme.

## Template Files

Templates are the files which control how your WordPress site will be displayed on the Web. These files draw information from your WordPress MySQL database and generate the HTML code which is sent to the web browser. 

WordPress allows you to define separate templates for the various aspects of your site. It is not essential, however, to have all these different template files for your site to fully function. Templates are chosen and generated based upon the Template Hierarchy, depending upon what templates are available in a particular Theme.

Here is the list of the Theme files recognized by WordPress. Of course, your Theme can contain any other stylesheets, images, or files.

* style.css -- The main stylesheet. 
* index.php -- The main template. 
* comments.php -- The comments template.
* front-page.php -- The front page template, it is only used if you use a static front page.
* home.php -- The home page template, which is the front page by default. If you use a static front page this is the template for the page with the latest posts.
* single.php -- The single **Post** template.
* page.php -- The **page** template.
* category.php -- The category template.
* tag.php -- The tag template. Used when a tag is queried.
* search.php -- The search results template. 
* attachment.php -- Attachment template. Used when viewing a single attachment.
image.php
* 404.php -- The 404 Not Found template. 

And there are more. See template hierarchy.


----------------
* http://codex.wordpress.org/Templates
* http://codex.wordpress.org/Theme_Development
* http://codex.wordpress.org/WordPress_Coding_Standards
* http://codex.wordpress.org/Site_Design_and_Layout
* http://make.wordpress.org/core/handbook/

