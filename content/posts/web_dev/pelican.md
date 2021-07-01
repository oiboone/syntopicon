---
title: Static Web Sites with Pelican and Pandoc
date: 2020-07-15
---

# Overview

Our goal in this article is to lay out a complete system for generating a static web site for posting technical articles.
We'll first consider the goals of such a system, then selection of appropriate tools, and finally modifications to standard tools required to achieve our goals.
When we're finished, it would be nice for this page to turn into something like this <https://www.andrewheiss.com/uses/> or <http://proven-inconclusive.com/blog/scientific_blogging_with_pelican_and_pandoc.html> or <https://blog.kdheepak.com/writing-papers-with-markdown.html>

# Goals

We would like to have individual pages similar in quality to LaTeX generated pdfs and websites formated using Tufte CSS.
All applications used in the workflow should be active, open source, cross platform projects.
All site source and configuration files must be UTF-8 text files.
The system should support all of the following features:

1. Equations, both inline and display (ideally including anything allowed by AMS-LaTeX)
Must include the ability to reference equaitons by number in the text.

2. Figures, included from image files or generated via code, complete wiht appropriate placement and figure cptioning and numbering for cross references.

3. Citations, with reference manager support and the ability to control reference format.

4. Links between pages.

5. Table of Content navigation inside individual articles and between articles.

# Tools for Workflow

1. [Pandoc](https://pandoc.org/) for generating HTML from Markdown. Together with specific settings and filters. This provides most of the text features we desire.

2. [Python](https://www.python.org/) as a scripting languge for generating graphs, filters, etc.

3. [Pelican](https://blog.getpelican.com/) as the static site generator. 
Written in Python, it is easily extended via plugins and supports a wide range of themes.

4. [Jinja2]() template language used by pelican and also the flask python web backend framework. (see future backend page...)

4. [Visual Studio Code](https://code.visualstudio.com/) is an editor that provides syntax highlihgting for markdown, python, yaml, and a wide range of other languages.
It is also easily extended via plugins that provides build, lint, and debug tools, spell checking, and markdown previewing.

5. [Zotero](https://www.zotero.org/) is an open source reference manager that provides reference harvesting from websites, bibtex support, and a range of other features. 

6. [nginx](https://www.fullstackpython.com/nginx.html) for self hosting.
This page also has links on configuration and security issues.

7. [Github pages]() for free site hosting.

# Pelican

## Pelican installation, setup, and configuration

Several sites provide guidance on installing pelican and setting up your ssytem.
<https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/>
<https://pagpires.github.io/its-just-a-curve.html>

### Overall system

Files needed for pelican setup are in pelican github site. Install locally
Content is in owncloud synopticon tree

### Initial setup

cd to pelican subdirectory and create virtual environment and populate with required packages:

```bash
python3 -m venv pelican
pip install -r requirements.txt
cd syntopicon_site
pelican-quickstart
```
Create a link the syntopicon content tree in owncloud to the content subdirectory in syntopicon_site

### Updating site and serving locally

```bash
source ../pelican/bin/activate
make html
cd output
python -m http.server 8000
```

### Push to github pages
???

[Pelican Plugins](https://github.com/getpelican/pelican-plugins) is a github repository where most of these plugins can be found.


## Pelican Plugins in use

[Extract Table of Contents](https://git.fangmeier.tech/caleb/pelican-plugins/src/65c9a48b4cea89bc628f27982f90f8c7cd603023/extract_toc) allows a site to put an article's table of contents in a navigation pane.

[Pandoc Reader](https://github.com/liob/pandoc_reader/tree/9ef0197eed5d141bf0f3b9a8468cd37ad3e5fbd7) I'm using a branch with a pull request that also parses Yaml metadata. I then modified the code to add the following to the metadata:
  * parent - parent directory of the current file. Useful for index file of nested categories to determine hierarchy. 

[category_meta](https://github.com/getpelican/pelican-plugins/tree/master/category_meta) allows category information to be provided in index files and posts kept in subdirectories by category.

[series](https://github.com/getpelican/pelican-plugins/tree/master/series) allows articles to be grouped and ordered in series. Metadata should include series: "series name" and series_index = #. Articles in template can be sorted by articles|sort(attribute="category,series_name,series_index)

[neighbors](https://github.com/getpelican/pelican-plugins/tree/master/neighbors) allows next and previous tags in template.

[subcategory](https://github.com/getpelican/pelican-plugins/tree/master/subcategory) 
## Python libraries needed by these plugins

* BeautifulSoup - used by "Extract Table of Contents"
* gitpython - used by filetime_from_git

## Possible Plugins to try

[assets](https://github.com/getpelican/pelican-plugins/tree/master/assets) combines and minisifies static assets like css and javascript files.

[Figure-ref](https://github.com/cmacmackin/figure-ref/tree/40e04d32bff468a6b3e63c373c5d95fca39783fe) provides figure references. I think the pandoc filters might be better but we shouod check.

[filetime_from_git](https://github.com/getpelican/pelican-plugins/tree/master/filetime_from_git)
 provides dates for file based on git but it didn't work when I tried it.

[glossary](https://github.com/getpelican/pelican-plugins/tree/master/glossary) creates a glossary page of definiton lists from individual pages.

[more categories](https://github.com/getpelican/pelican-plugins/tree/master/more_categories) adds nested categories, multiple categories per areticle

[neighbors](https://github.com/getpelican/pelican-plugins/tree/master/neighbors) provides next and previous metadata


# Pandoc settings and filters

The pandoc reader must be added as a plugin for pelican. Currently, the main branch is missing a few features (including reading YAML metadata for Pelican) so I'm using a branch on pull request #13.

All pandoc command line arguments are set in peliconconf.py

```python
PANDOC_ARGS = [

  '--filter=pandoc-citeproc',
  '--katex=https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/',
  '--toc',
  '-s',
  '--toc-depth=3',
  '--number-sections',
  '--template=pelican.html',
]
```

1. --number-offset can be used to continue numbering from one file to another

## Other Settings and Filters to try

1. [panflute](https://github.com/sergiocorreia/panflute) provides a pythonic package for generating pandoc filters

2. [pweave](http://mpastell.com/pweave/) and [knitr](https://yihui.org/knitr/) provide python and R integration wiht pandoc. 
[rmd reader](https://github.com/andrewheiss/Rmd-Pandoc-Reader) is a reader for these files.
<https://tech-notes.maxmasnick.com/literate-python-setup-with-pweave-and-atom><https://iaingallagher.tumblr.com/post/41359279059/python-pweave-and-pandoc-howto><https://stackoverflow.com/questions/40171949/using-python-together-with-knitr><http://almart.in/pelican-with-rmd.html><https://rjweiss.github.io/articles/2014_08_25/testing-rmarkdown-integration/>

3. Consider modifying pandoc reader to allow a more general command, e.g. [pandocomatic](https://heerdebeer.org/Software/markdown/pandocomatic/#converting-a-series-of-documents) to allow templates for pandoc.

4. [pandoc-xnos](https://github.com/tomduck/pandoc-xnos) is a set of filters for numbering tables, figures, equations, and sections.
Built wiht pandocfilters in python.

# Pelican Theme issues

## Theme comparisons

1. [Elegant](https://elegant.oncrashreboot.com/) looks like the best choice for a theme. It does include the bootstrap framework so it might be larger than needed.
However it does have a lot of nice features and is actively maintained.
I need to look into making tweaks to layout, font, and color choice modificaitons however.
<https://jackdewinter.github.io/2019/09/08/static-websites-getting-ready-for-publishing-themes-and-minutiae/> is a great example of what can be done with this theme.
It also has some great articles on using Pelican.
<https://pagpires.github.io/styling-of-the-blog-using-theme-elegant-with-modifications.html> uses a modified elegant theme to look more like tufte.
If we decide to use elegant theme, custom.css can be used to modify the style of pages without breaking updates.<https://elegant.oncrashreboot.com/customize-style>

1. [Astrochelys](https://out-of-cheese-error.netlify.app/astrochelys#orgcf4bba5_1) has a fixed navigation panel on the left which I like, but the color scheme sucks.
It also has margin notes that seem to work well.

2. <https://standage.github.io/pages/notebook-setup.html> has a nice color scheme and footer

3. <https://johndmart.in/> (Source code here <https://github.com/jdmar3/jdmar3.github.io>) uses a modified tufte css theme. Nice color and font.

4. [Tufte CSS](https://edwardtufte.github.io/tufte-css/) provides a style sheet with a tufte look and feel including sidenotes and a variety of special styles.
[Tufte theme for Jekyll](https://github.com/clayh53/tufte-jekyll)
<https://github.com/mandaris/TuftePelican> provides a pelican theme based on this.
<https://lawler.io/about/> is a website using a pelican theme based on tufte css.

5. <http://duncanlock.net/tag/pelican.html> ok theme, but also thoughtful comments on building a static site. About page has link to github site with theme.

6. <https://pythonforundergradengineers.com/how-i-built-this-site-3.html> uses the bootstrap theme but provides a nice tutorial on setting up a site and customizing pelican.

## Marginal Notes

1. Use of a pandoc filter to convert footnotes to sidenotes <https://blog.kdheepak.com/pelican-margin-notes-with-pandoc.html>
Links on this page provide interesting comments on the advantages of sidenotes, footnotes, popup notes.

# Templates

## Jinja templates

<https://github.com/joachimneu/pelican-jinja2content/issues/3> describes the {\% include %\} directive.

## CSS and HTML 

<https://www.smashingmagazine.com/2009/08/designing-a-html-5-layout-from-scratch/> is a nice tutorial on writing html5.
<https://css-tricks.com/guides/> has many useful css guides.
<https://www.webfx.com/blog/web-design/20-html-best-practices-you-should-follow/>

### Color issues

Questions on both how to pick a color scheme and how to represent in css so it is understandable and easy to change.

<http://geoffgraham.me/naming-sass-color-variables/> <https://css-tricks.com/what-do-you-name-color-variables/><>