
# current issues

1. Fill in readme.md file
2. FIXED: article sidebars show only toc not header or footer - problem was nested nav tags. Put back class .sidebar and based layout on that :(
3. dark mode doesn't stick between pages
4. hide daggers for margin notes when large.
5. pdfs don't show properly
6. format for author in blockquotes
7. correct margin note symbol in tufte file
8. FIXED: toc indentation and numbering? Style needed to be renamed. Leave numbering for now.
9. FIXED: font size and layout are different in chrome and firefox - even after using normalize. forgot $ at start of one reference to a font stack.
10. Font choice needs to be improved
11. id order of files in category by alpha order of filenames and prepend filename with 3 digit sequence number, use 010, 020, 030 and sequence.

# Where to find todo issues

1. Here!
3. content/web_dev/pelican.md - This should have description of current system and how it got that way.
4. content/web_dev/testing/problems.md - all these issues are here now.

# todo list

## metadata fields to include in markdown yaml for source files

1. title
2. subtitle
3. date - perhaps use file date instead by using DEFAULT_DATE='fs' in pelicanconf.py
4. author - or we can use the default in peliconconf.py
5. series - if the article is part of a series
6. series_index
7. category if not taken from directory name
8. summary
9. tags

## jinja template modifications

1. next and previous buttons on articles - possibly limit to series?
2. TOC that includes series - done
3. Use variables in peliconconf.py for features that might vary from site to site. e.g.
    a) SITE_LICENSE to include in page footers
    b) titles as in the elegant theme's 'templates/_includes/_defaults.html
4. TOC with parts of series listed <https://elegant.oncrashreboot.com/how-to-use-series-plugin> - done
5. Custom home page (e.g:)

```python
ARTICLE_URL = 'posts/{category}/{slug}'
ARTICLE_SAVE_AS = 'posts/{category}/{slug}.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'
```

## CSS modifications

1. blockquotes and epigraph styling like tufte
2. fullwidth style for figures, etc. like tufte
3. Improve solarized pygments theme
    a) <https://gist.github.com/tdreyno/1125708>
    b) <http://honza.ca/solarized-pygments/>
4. Allow light/dark toggle 
    a) <https://web.dev/prefers-color-scheme/>
    b) <https://getpocket.com/redirect?url=https%3A%2F%2Fflip.it%2FZ9NQRT>
5. Improve font stacks
    a) <https://www.filamentgroup.com/lab/font-loading.html>
6. Menu button for small screens
    a) <https://www.w3schools.com/css/css3_transitions.asp>
    b) <https://www.w3schools.com/css/css_dropdowns.asp>
    c) <https://css-tricks.com/solved-with-css-dropdown-menus/>
    d) <https://www.briankephart.com/dropdowns-without-javascript>
    e) handy testing website for css features <https://jsfiddle.net/cUCvY/1/>

7. Alternative color schemes. Avoid high or low contasts.
    a) <https://www.nngroup.com/articles/low-contrast/>
    b) contrast testing <https://marijohannessen.github.io/color-contrast-checker/>
    c) <https://www.visualexpert.com/FAQ/Part6/cfaqPart6.html>

8. Look at alternatives for code line numbering and highlighting.

## Pelicanconf.py

### Plugins
1. liquid_tags - Allows code listings from external files with buttons for download and live ipython sessions, Might conflict wiht jinja_templates
2. [jinja2content](https://github.com/getpelican/pelican-plugins/tree/master/jinja2content) allows use of jinja2 template language inside markdown before going to pandoc. (Does it support pandoc?)
3. neighbors - permits previous and next  Installed - now fix templates t use it correctly,
4. series - allows multi-part articles - installed and working
5. [pelican-ipynb](https://github.com/danielfrg/pelican-jupyter/tree/f58e12480d8b888525648d876fe86c6b405cf45a) works wiht liquid tags to provide jupyter access for pelican.
### Configuration variables 
1. DIRECT_TEMPLATES = [404] to get custom 404 page.
2. Custom labels as described under jinja templates.


## Things to steal from elegant

1. https://elegant.oncrashreboot.com/code-snippets-copy-to-clipboard
2. https://elegant.oncrashreboot.com/live-filter-for-tags
3. https://elegant.oncrashreboot.com/unique-home-page-features
4. https://elegant.oncrashreboot.com/zero-clutter-categories
5. https://elegant.oncrashreboot.com/tables
6. 

## Appearance and style

6. Katek or mathjax setup with font selection and other features - not just default values
    a) https://www.wild-inter.net/posts/mathjax-in-jekyll
    b) https://github.com/mathjax/mathjax-docs/wiki/Can-MathJax-use-font-xxxx%3F

14. Favicon
27. MathJax fallback for Katex <https://github.com/rbnvrw/katex-auto-render>

## Pelican related

29. Nested categories <https://pypi.org/project/pelican-more-categories/> and <https://github.com/getpelican/pelican-plugins/tree/master/subcategory>
15. category page templates and general site and page layout
16. Look at elegant for other features to add
23. How to control order of articles in list
24. Table of contents that has articles (or parts of multipart article) at top layer
25. Continue numbering from one file to another. (Use part numbers for multi-part articles.)

## Page Layout and Site Organization

11. multi-part articles
12. Next and Previous buttons

## Source Code Cleanup

1. Find better place to put bib files, lua filter, citation style class file.
2. Use git better
    a) <https://www.softwarelab.it/2018/10/12/adding-an-existing-project-to-github-using-the-command-line/>
    b) https://stackabuse.com/git-add-all-files-to-a-repo/
    c) https://www.gimp.org/about/meta/git-workflow.html
3. Use semantic URLs when possible <https://en.m.wikipedia.org/wiki/Clean_URL>

## Pandoc related

9. modify pandoc_reader to read command line parameters from yaml in pandoc files. 
    a) Perhaps all that is needed is to change command to panrun <https://github.com/mb21/panrun>
    b) Perhaps use frontmatter readers to parse frontdata. <https://pypi.org/project/python-frontmatter/> and <https://stackoverflow.com/questions/25697664/how-would-i-parse-front-matter-with-python>

7. Modify lua filter to include sidenote functionality
8. Figure, equation, section numbering filters for pandoc

10. use file dates for dates
28. Look for better ways to refer to static resources (images, etc.) that doesn't break for pdf files. (Possibly a Lua filter to remove <static> flag.) Can <static>./img/foo.png be used?
17. pweave or knitr integration
18. Pandoc structure that works for pdf or website
19. Diagrams in pandoc (graphvis, plantuml, wavedrom, etc.)
20. cross references between pages (ideally that work in pdf as well as website)
21. Common reference page for multiple articles?
26. Look at other pandoc options like --section-div and --email-obfuscate --id-prefix
50. Other pandoc extras <https://pandoc.org/extras.html>

## Efficiency, speed, quality

1. Minify css, js
2. Try using javascript rot13 to obfuscate email address
3. https://www.smashingmagazine.com/2008/11/12-principles-for-keeping-your-code-clean/
4. async loading of css <https://www.filamentgroup.com/lab/load-css-simpler/>


# Open questions

best layout for online book?


# Problems that need to be fixed

## Issues with static site generator

* display of pdfs is bad. viewer embedded in page Is there a better way??

* Fix templates to add *.html to page links or fix servver t not need it (clean vs. unclean links)


## Issues with pandoc and friends

* remove panzer from pandoc and friends test page

* Possibly add pandocomatic or pp comments?

* Possibly add comments on pelican?

## Things to add to pandoc and friends or other test page

* python code and graphics to use pweave

* spans and divs [span text]{.class} and :::class ... ::: for epigraphs, newthought, footer


## combining tufte-pandoc, astrochelys theme

1. First modify astrochelys theme:
    a. Make menu/toc shrink to menu button for small screens
    b. Change pygments color scheme to solarized
    <https://guizishanren.com/change-syntax-highlight-with-pygments-CSS-for-Pelican-blog/>
    c. Design site page structure and layouts
    d. change pygments color scheme to solarized

2. Merge in tufte style
    a. fullwidth class
    b. newthought class
    d. epigraphs style
    e. consider a background change or border for sidenotes and margin notes when expanded in mobile mode.


