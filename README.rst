DJANGO SCRIPTER
===============
Django Scripter is a simple app for django to manage JS and CSS file on django projects.

Original uses cases:
--------------------
We at Egomedia Bali create an in-house CMS that consist of several in-house django apps to build this another django CMS.
Our CMS is working as a modular content system, that means each part of content is a page module. eg. Title/subtitle module, text module, image gallery module, contact form module.

And to use those module is as easy as drag and drop, put content and save it. The problem comes when we need to use several javascript library and saparate CSS for each module, because basically each module is an django app, so we want them as independent as possible, do not rely on other module js or css, so they bring their own css and js file event they are exist in other modules static files.

We need a way to avoid duplicate css or js needed on one page if module appear more than one time at the same page, no problem for css but can be a problem for loading js file more than one, such as loading jQuery more than one.


What it does:
-------------
Basically Django-scripter bundled with several js and css library that we use frequently such as latest version Jquery and 960gs css. and we can use it in each new project without re-downloading and re-putting them together each time we need them, as long as django-scripter installed, we can access them anytime in the template header file.

The principal thing how i works is, if you include the same javascript or css from many different code, this app will filter it out and will display only one on the head section of your page.

How to use it:
--------------
As I explained above, django-scripter bundled with jQuery and 960gs.
First check whats available scripts:

::

    $> python manage.py list_scripts

Will list all available scripts:

::

    \* Available Javascripts

    jquery

    \|____[1.7.2], "scripter/js/jquery/jquery-1.7.2.min.js"

    \* Available Stylesheet

    reset

    \|____[reset], "scripter/css/960gs/reset.css"

    \|____[text], "scripter/css/960gs/text.css"

    960gs

    \|____[12cols], "scripter/css/960gs/960_12_col.css"

    \|____[16cols], "scripter/css/960gs/960_16_col.css"

    \|____[24cols], "scripter/css/960gs/960_24_col.css"


If we want to use them at template we just need to call the tags from template.

::

    {% load scripts %}
    <html>
    <head>
    <!-- this will include all needed css -->
    {% head_css "reset, 960gs==12cols" %}

    <!-- this will iclude all needed js -->
    {% head_js "jquery" %}
    </head>
    <body></body>
    </html>

Above tags will print:

::

    <html>
    <head>
    <!-- this is result of "reset" -->
    <link rel="stylesheet" href="/static/scripter/css/960gs/reset.css" media="all"/>
    <link rel="stylesheet" href="/static/scripter/css/960gs/text.css" media="all"/>

    <!-- this is result of "960gs==12cols" -->
    <link rel="stylesheet" href="/static/scripter/css/960gs/960_12_col.css" media="all"/>

    <!-- this is result of "jquery" -->
    <script type="text/javascript" src="/satic/scripter/js/jquery/jquery-1.7.2.min.js"></script>

    </head>
    <body></body>
    </html>

Available template tags:
------------------------
* **head_css**
  
  This will be holder for all CSS file that called or registered to show at head section of html. 
  ::
      
      Usage:

      {% head_css %}

      or

      {% head_css "cssname, other_cssname==version/id" %)

* **head_js**

  This will be holder for all JS file that called or registered to show at head section of html. 
  ::
      
      Usage:

      {% head_js %}

      or

      {% head_js "jsname, other_jsname==version/id" %)


Available methods:
------------------


* **include_head_js**

  Use this method if you want to include javascript to head section of your page from app code.  
  ::
      
      Usage:

      from scripter import scripts

      # if you need jQuery to run the scripts
      scripts.include_head_js(['myapp/js/some_js.js', 'myapp/js/other_js.js'], ['jquery'])

      or

      # if no need for other js depedencies
      scripts.include_head_js(['myapp/js/some_js.js', 'myapp/js/other_js.js'])

* **print_head_js**

  Use this method if you want to include javascript inline javascript code to head section of your page from app code.  
  ::
      
      Usage:

      from scripter import scripts

      # if you need jQuery to run the scripts
      myscript = """
      <script type="text/javascript">
         alert('helo world');
      </script>
      """
      scripts.print_head_js(myscript, ['jquery'])

      or

      # if no need for other js depedencies
      scripts.print_head_js(myscript)

* **include_head_css**

  Use this method if you want to include css file to head section of your page from app code.  
  ::
      
      Usage:

      from scripter import scripts

      scripts.include_head_js(['myapp/css/some_css.css', 'myapp/css/other_style.js'])

* **print_head_css**

  Use this method if you want to include inline css code to head section of your page from app code.  
  ::
      
      Usage:

      from scripter import scripts

      mycss = """
      <style type="text/css">
         body{background:#fff;}
      </style>
      """
      scripts.print_head_css(mycss)

Notes
-----
I know this is just a short HOWTO of Django-scripter application, far from perfect and I am sure not all projects need this apps, if you need more information on how it works and how to customize it, just drop me an email at ekaputra[at]balitechy.com.
