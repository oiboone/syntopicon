---
title: Todo List
slug: todo
date: 2018-06-09
modified: 2018-06-09
---

# Todo List

1. *done* Run Nginx on virtual linux server to serve simple static webpage
2. *done* Use vagrant to automate setup of test server, keep shared directory for modifying files
5. *done* Use pandoc to create HTML content more easily
9. *done* Serve flask app via nginx and wsgi? <https://www.e-tinkers.com/2018/08/
8. Learn to write simple dynamic pages in python, flask, and jinja 2
2. Learn HTML 5 to generate more interesting static pages (duckett pdf book, html cheat sheet,head first html and css, New perspectives HTML and CSS, PHP MySQL Javascript and HTML5 for dummies, build your website the right way )
3. Learn CSS 3 to separate styling from content (duckett, css3 cheat sheet, css indepth, css - the definitive guide (grid layout in css, transitions and animations in css, transforms in css,positioning in css, css text, values units and colors, selectors specificity and the cascade))
4. Look at Sass and Less as CSS alternatives??? (learning less,beginning css preprocessors
)
4. Look at webfonts and other design aspects (principles of beutiful web design, head first web design)
6. Create custom template for pandoc html to automate production of static page from markdown
7. Learn javascript for simple client side scripting, modifying DOM and reading values. (eloquent javascript pdf, the good parts book, head first javascript, head first javascript programming,head first html5 programming)

8. Look at pyramid and cornice for web api development <https://opensource.com/article/20/1/python-web-api-pyramid-cornice>
8. Learn to use python environments to prevent library version conflicts
how-to-properly-host-flask-application-with-nginx-and-guincorn/>
9. Authentication via Okta???
10. Install mysql on test server and play with basic database operations
10. Write CRUD app in python using flask and some database package and some database (e.g. mysql???)
 <https://developer.okta.com/blog/2018/07/23/build-a-simple-crud-app-with-flask-and-python><https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one>
10. Try an asynchronous python framework instead of flask
11. Learn how to communicate between javascript and backend app.
12. Experiment with model-view-controller and related patterns
13. Undersand SOAP and REST
14. Try node.js.<https://codeburst.io/the-only-nodejs-introduction-youll-ever-need-d969a47ef219>
15. Look at noSql like mongodb and other types
16. Try digital ocean droplet (1GB ram, 1virtual cpu, 25 GB ssd 1 TB transfer for $5/month <https://www.digitalocean.com/pricing/>)
17. Learn go, typescript,etc???
18. try ajax, jquery (head first jquery)
19. Android apps using html, css, and javascript?
20. Try using Kotlin instead of javascript
20. Try using elm instead of javascript
21. Try compiling to webasm?
22. HTTPS first using self signed certificates on localhost then using letsencrypt.org <https://github.com/reindrich/ansible-nginx-lets-encrypt>
23. Try deployment of static sites via github pages, bitbucket pages  netlify, surge.sh, or ZeitNow <https://dev.to/bholmesdev/why-im-using-surge-and-not-github-pages-4lf5>
24. Serverless applications? <https://zeit.co/blog/python-wsgi>

## Todo List for web development

### Top Level Stuff

Here are some useful summaries
+ <https://codeburst.io/the-2018-web-developer-roadmap-826b1b806e8d>
+ <https://medium.com/tech-tajawal/modern-frontend-developer-in-2018-4c2072fa2b9c>
+ <https://github.com/kamranahmedse/developer-roadmap>
+ <https://coder-coder.com/learn-web-development/>
+ <https://dzone.com/articles/the-modern-application-stack-part-1-introducing-th> - The mean stack 
    1. Angular (or react) front end framework for dynamic UI
    2. Express back end framework running on node.js
    3. Node.js Javascript runtime to impleemnt backend logic in javascript
    4. mongoDB -nosql database
+<https://hackernoon.com/modern-web-development-bf0b2ef0e22e>
<https://hackernoon.com/the-2018-devops-roadmap-31588d8670cb>


#### Server Lamp Stack

1. Linux - OS
2. Apache - HTTP Server (also NGINX)
3. MySQL - database server (or MongoDb for noSQL)
4. PHP - server side programming (or python)

#### Network Protocols

1. TCP/IP
1. http

#### Front End Client Side components

1. HTML - content or something that compiles to HTML like JavaScript XML (jsx) <https://en.wikipedia.org/wiki/React_(JavaScript_library)#JSX>
2. CSS - style sheets <https://medium.com/actualize-network/modern-css-explained-for-dinosaurs-5226febe3525>
2. Alternatively something that compiles to CSS
    a. LESS (Leaner Style Sheets) Written in javascript
    a. SASS (syntactically Awesome Stylesheets) written in Ruby
    a. SCSS (sassy CSS) - SASS with syntax like CSS, so valid CSS is also valid SCSS.
3. JS - javascript code for automation in browser (Kotlin transcompiles to js)
4. Alternatively something that transpiles to javascript
    a. kotlin - <https://blog.jetbrains.com/kotlin/2013/10/writing-kotlin-in-the-browser/> or 
 <https://medium.com/bcgdv-engineering/building-a-full-stack-web-app-in-kotlin-af8e8fe1f5dc>
    b. typescript
    c. Dart - Google's modern language that transpiles to javascript
    d. what about asmjs <https://en.wikipedia.org/wiki/Asm.js> and webassembly?


### Frameworks

#### Front End Frameworks

1. Front end template
    a. boilerplate - <https://www.quora.com/Is-Bootstrap-a-complement-or-an-alternative-to-HTML5-Boilerplate-or-vice-versa-Can-they-be-used-together-or-do-we-have-to-pick-a-side/answer/Nicolas-Gallagher#>
    a. Initializr for generating a template for you <http://www.initializr.com/>
1. CSS frameworks - <https://github.com/ikkou/awesome-css#architecture><http://nicolasgallagher.com/about-normalize-css/>
    a. normalize.css - <https://stackoverflow.com/questions/6887336/what-is-the-difference-between-normalize-css-and-reset-css>
    a. bootstrap
    a. <https://www.webdesigndegreecenter.org/ten-best-css-libraries-developers-designers/>
    a. <https://www.catswhocode.com/blog/top-10-lightweight-css-frameworks-for-building-fast-websites-in-2018>
    a. milligram, skeleton
1. SVG Icon sets
    a. Glyph <https://glyph.smarticons.co/>
    a. OpenIconic <http://useiconic.com/open>
    a. featherIcons <https://feathericons.com/>
    a. More <https://superdevresources.com/free-svg-icons/> fontAwesome, material design, octocons, Entypo, zondicons, hawkons,Linea, icomoon, linearicons, typicons
    <https://tagliala.github.io/vectoriconsroundup/>
1. Javascript UI frameworks
    a. Angular with typescript
    a. React with jsx
    a. Vue -lightest
1. Other tools
    a. Build tools
        i. gulp
    a. bundling
        i. webpack

#### Back end Frameworks

1. Ruby - Rails
2. Python -
    a. Django
    b. Flask
    c. Quart - an asynchronous framework similar to flask
    d. aiohttp ???
3. Java and other JVM Languages
    a. Java EE
    b. other application servers

#### Content Management Systems

1. Drupal
1. Wordpress

### HTTPS

1. <https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https>

### Image sources

<https://en.wikipedia.org/wiki/Wikipedia:Public_domain_image_resources>

http://courseweb.stthomas.edu/physics/faculty/jalkio/ 

### Development tools

1. WAMP - LAMP for windows allows testing locally on windows machine
<https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server> - how to set up a testing server on a linux box.
Here are setup instructions for python 3's http.server so that it handles cgi-scripts : <https://stackoverflow.com/questions/30516414/how-to-run-cgi-hello-world-with-python-http-server>
<https://dzone.com/articles/python-simple-http-server-with-cgi-scripts-enabled> 
<https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04>
