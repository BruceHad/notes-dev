PHP Notes

* Dated 08th October 2012
* Extracted 29/03/2016

## PHP File Upload (Post Method Upload)

This lets you upload text and binary files.

In the form tag you must specify the enctype:

    enctype = "multipart/formdata"

You can also specify the maximum file type by entering a hidden form field (prior to the upload field).

    <input type="hidden" name="MAX_FILE_SIZE" value="30000" />

Value is measured in bytes. This provides nice user side validation, but shouldn't be trusted.

The global S_FILES variable contains all the uploaded file information.

$_FILE['userfile']['name'] -- original file name.
['type'] -- mime type.
['size'] -- fiel size in bytes.
['tmp_name'] -- new, temporary name.
['error'] -- possible error codes.

Files will be stored in the servers default temporary directory (apparently /tmp/ on linux). This location can be overridden in the php.ini file.

    upload_tmp_dir = /your_www/tmp/

Or you can apparently amend it in the script.

    ini_set('upload_tmp_dir', '/your_www/tmp/');

### Working Example

Uploading images is a common use case, so I'm not about to re-invent the wheel here. I can use the class.upload.php script.

* http://www.php.net/manual/en/features.file-upload.post-method.php
* http://www.verot.net/php_class_upload.htm

## PHP Templates

(31/07/2012)

Templating engine is used to seperate design from business logic. E.g. A Wordpress CMS has a bunch of template files that control the layout of various pages. These pages mix HTML and PHP code that, in turn, produces the HTML code that is sent to the browser.

### Tutorial - How to make a simple HTML template engine in PHP

A simple example of a template file name user_profile.tpl:

    <h1>[@username] profile</h1>    
    <img src="http://www.broculos.net/en/%5B%40photoURL%5D" class="photo" alt="[@name]" />  
    <b>Name:</b> [@name]<br />  
    <b>Age:</b> [@age]<br />  
    <b>Location:</b> [@location]<br />  

### The Code

The code for the templating engine called template.class.php.

    class Template {
        protected $file;
        protected $values = array();
        
        public function __construct($file) {
            $this->file = $file;
        }

        public function set($key, $value) {
            $this->values[$key] = $value;
        }  

        public function output() {
            if (!file_exists($this->file)) {
                return "Error loading template file ($this->file).<br />";
            }
            $output = file_get_contents($this->file);
          
            foreach ($this->values as $key => $value) {
                $tagToReplace = "[@$key]";
                $output = str_replace($tagToReplace, $value, $output);
            }  
            return $output;
        }
    }

We have two main methods here. 

* set() sets the key value pairs in the $values array.
* output() reads through the template file and replaces any instances of the tag with the value found in the array.

### Layout Template

The first template code above only outputs a chunk of code, not the full page. We therefore need a template page that will include all the <head>, <body> tags etc.

For example: index_template.tpl:

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html>
    <head>
    <title>[@title]</title>
    <link rel="stylesheet" type="text/css" href="http://www.broculos.net/en/stylesheet.css" />
    </head>
    <body>
        <div id="header">
            <a href="http://www.broculos.net"><img src="http://www.broculos.net/en/broculo_small.gif" class="logo" alt="Broculos.net" /></a>
            <h1><a href="http://www.broculos.net">Broculos.net</a></h1>
            <h2>Simple PHP Template Engine</h2>
        </div> 
        <div id="menu">
            <h1>Navigation</h1>
            <ul>
                <li><a href="http://www.broculos.net/en/user_profile.php">User profile</a> - example of a user profile page</li>
                <li><a href="http://www.broculos.net/en/list_users.php">List users</a> - example table with listing of users</li>
            </ul>
        </div>
        <div id="content">
            [@content]
        </div>
        <div id="footer">
            Example usage of a simple PHP Template Engine.<br />
            Search <a href="http://www.broculos.net">Broculos.net</a> for more tutorials.
        </div>
    </body>
    </html>

### Output File

Now we can create our output file which will display the results. user_profile.php

    include("template.class.php");
      
    $profile = new Template("user_profile.tpl");
    $profile->set("username", "monk3y");
    $profile->set("photoURL", "photo.jpg");
    $profile->set("name", "Monkey man");
    $profile->set("age", "23");
    $profile->set("location", "Portugal");
      
    $layout = new Template("layout.tpl");
    $layout->set("title", "User profile");
    $layout->set("content", $profile->output());

    echo $layout->output();

This sets up the content data, generates the user_profile from the equivalent template, then generates a full template and inserts the user_profile into it.

### Another Example

This example shows a list of registered users. It splits the code into a couple of template: 1. For the main content. 2. Another for the information pertaining to each user.

The main template is called list_users.tpl

    <h1>Users</h1>
    <table>
        <thead>
            <tr>
                <th>Username</th>
                <th>Location</th>
            </tr>
        </thead>
        <tbody>
            [@users]
        </tbody>
    </table>

And list_users_row.tpl

    <tr>
        <td>[@username]</td>
        <td>[@location]</td>
    </tr>

In the template class we need to add a new function that will merge multiple templates:

    static public function merge($templates, $separator = "n") {
        $output = "";
      
        foreach ($templates as $template) {
            $content = (get_class($template) !== "Template")
                ? "Error, incorrect type - expected Template."
                : $template->output();
            $output .= $content . $separator;
        }  
        return $output;
    }

And now we can create the list_users.php output file.

    include("template.class.php");
      
    $users = array(
        array("username" => "monk3y", "location" => "Portugal")
        , array("username" => "Sailor", "location" => "Moon")
        , array("username" => "Treix!", "location" => "Caribbean Islands")
    );  
    foreach ($users as $user) {
        $row = new Template("list_users_row.tpl");
      
        foreach ($user as $key => $value) {
            $row->set($key, $value);
        }
        $usersTemplates[] = $row;
    }
    $usersContents = Template::merge($usersTemplates);
      
    $usersList  = new Template("list_users.tpl");
    $usersList->set("users", $usersContents);
      
    $layout = new Template("layout.tpl");
    $layout->set("title", "Users");
    $layout->set("content", $usersList->output());
      
    echo $layout->output();

* [How to make a simple HTML template engine in PHP](http://www.broculos.net/en/article/how-make-simple-html-template-engine-php)

## PHP Classes and Objects

A class is basically a template that is used to generate an Object (an instance of the class).

    class ShopProduct {
        // Class Body
    }

Objects are constructed from Classes. 

    $product = new ShopProduct();

Classes can have properties (variables) and methods (functions). These things tend to have a scope (public or private) but default to public.

    class ShopProduct {
        public $title = "The Title";

        public function printTheTitle() {
            print $this->title;
        }
    }

An object's properties and methods can be accessed using the arrow notation (similar to dot notation in python).

    $product = new ShopProduct();
    print($product->title);
    # The Title
    $product->printTheTitle();
    # The Title

(Note the lack of the $ sign preceding the 'title' property.)

The code above introduced the $this keyword, which basically refers to the current object.

You don't have to declare all properties in the class definition, you can add new ones them at runtime. You also don't have to declare the values of the properties in the class definition, but if you do, you can override them. 

    $product->title = "A new title";

But this is probably all considered bad practice. Better to have a method that is designed to maintain the properties, so you can build some validation into that process.

One special case is the contruct method, which is called automatically when a new object is created.

    function __contruct() {
        // Contructor code.
    }

### Hints and Type Checking

PHP is loosely typed, which is flexible but can cause problems tracking down bugs where the wrong/unexpected data type has been supplied.

Therefore type checking is important whenever data is being passed. For primitive you can use php function like is_int() or is_bool() to check the type, and die, for example, if the wrong type is detected.

Objects themselves have a primitive data type (Object), but the class is basically a type definition, so it also belongs to that type. Objects can be passed as arguments the same as other primitives. If you want to confirm the type of the object then you can use hinting, by indicating the class name of the object being passed as an argument.

    function printObject(ShopProduct $product) {
        var_dump($product);
    }

So if an object of a different Class is passed to the function as an argument, a fatal error occurs.

Unfortunately type hinting cannot be used for primitives.

### Inheritance

Classes define the type of the object instantiated from them. But types can also define the family of the class through inheritance. This is where one Class is derived from a parent Class, inheriting some of it's features. Generally a child class will add/replace functionality from its parent, known as extending the parent.

    class ChildClass extends BaseClass {
    
    }

You can readily identify patterns where inheritance can be used if you have a class where parts (methods or properties) don't seem to belong. In these cases, the parts can be split into a new Class, extending from the original class.

#### Overriding Parent Methods

The constructor of a parent class is not called automatically by the child. That becomes the responsibility of the child class.

    public function __contruct($title) {
        parent::__contruct($title);
    }

This uses the Paamayim Nekudotayim (double colon ::) which replaces the arrow (->) in the scope of Classes as opposed to Objects.

A child class will often just amend the parent slighly, so rather than replacing entire methods, you can often use the parent keyword as above to call the parent's method and make a small change to it.

    public function printDetails(){
        parent::printTheTitle();
        print($this->theYear);
    }

#### Access (Public, Private or Protected)

There are three levels of access that can be granted for methods and properties -- Public, Private or Protected. 

Public - The default. This means any other object can access it.
Private - This means it can only be accessed from within the same object.
Protected - This means it can only be accessed from within the same object or from a subclass of the object.

It's good practice to make everything private and reveal them only when necessary.

#### Accessor Methods

Even when other classes need access to properties, it can be a good idea to keep them private and control the access using Accessor (Getter and Setter) methods.

### Static Properties and Methods

Classes are not just templates for building objects, sometime the classes themselves are used in the program. There are methods and Properties known as 'static' that can be accessed by all instances of the class. I think of these like globals, since if the static properties change, it changes for all objects.

    class StaticExample {
        static public $aNum = 0;

        static public function sayHello() {
            print "Hello";
        }
    }

Since these are only used in the context of a class, the double colon is used.

    StaticExample::$aNumb;
    StaticExample::sayHello();

Static methods appear to be useful in creating factory type methods. This means you can create a static method that generates and instance of its own subclass (or class?). That method can then be called without having to instantiate any new objects.

### Constants

Constants are properties/variables that don't change. They are declared with the const keyword.

    class ShopProduct {
        const AVAILABLE = 0;
        ...
    }

Constants can only contain primitives.

Like static properties, constants are accessed in the class not the instance. No symbol or dollar sign is required.

    print ShopProduct::AVAILABLE;

### Abstract Classes

Abstract classes cannot themselves be instantiated. Instead, they define the interfaces for any class that extends them.

    abstract class ShopProductWriter {
        protected $products = array();

        public function addProduct(ShopProduct $shopProduct) {
                $this->products[] = $shopProduct;
        }
        abstract public function write();
    }

As in the above example, an abstract class will often contain an abstract method, that has no code. It's just there to guarantee that child classes implement this method.

### Interfaces

While Abstract class can partially implement methods, Interfaces can only define methods. That is, a method can be declared but not implemented.

Any class that implements an interface, will have to figure out how to implement all the methods declared in the interface.

    interface Chargeable {
        public function getPrice();    
    }

    class ShopProduct implements Chargeable {
        ...
        public function getPrice(){
            return ($this->price - $this->discount);
        }
        ...
    }

### Conventions:

* Class names appear to be capitalised (e.g. ClassName)
* Objects appear to be lower case (e.g. object = new ClassName();)
* Methods and Properties appear to be camelCased (e.g. methodName)
* Constant properties seem to be UPPERCASE

* [Php Objects, Patterns and Practice](http://books.google.co.uk/books?id=KZoAq_mbhXAC)

## PHP Debugging

I believe error reporting can be switched on in the file that you are working on or can be configured in the php.ini file (this is probably the best option as you can have it switched on for the test server but off for the live server).

The following code will switch on Error reporting on the page you are working.

    ini_set('display_errors',1);
    error_reporting(E_ALL|E_STRICT);

Alternatively edit the php.ini file.

    /etc/php5/apache2/php.ini

And stick this somewhere:

    error_reporting = E_ALL & E_STRICT


### About Errors

* Syntax errors are known as Parse Errors. 
* Fatal Errors cause the program to fail. The syntax is correct, in that PHP understands the instruction, it just cannot comply.
* Warning Errors can be supressed as they are not fatal, but they are warning you that something might be wrong.
* Notices are other minor errors that the code can deal with.

### var_dump()

var_dump() is a useful function that prints out a variable or expression in a human readable way. I've been using print_r() but var_dump() might work better as it includes a lot more information, such as the type.

### Debugging Tools

FirePHP

 * [Debugging techniques for PHP programmers](http://www.ibm.com/developerworks/library/os-debug/)(IBM)
 * [PHP Error Reporting](http://www.phpfunctionalism.com/config/error-reporting/)
 * {How to Debug in PHP](http://thinkvitamin.com/code/how-to-debug-in-php/)




