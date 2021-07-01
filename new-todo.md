# Top level

1. Basic tutorials for git/github/github pages
2. Python virtual environment options
    a. venv
    b. https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe
    c. https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko
    d. poetry
    e. conda

# css

1. properties for levels of heading - currently headings are too big
2. better choice of colors
3. Better choice of fonts

# Pelican Template/Plugin Issues

1. next/previous seems random
2, order of categories in navigation panel of categories page
2. Possibly use of toc metadata in index files
3. Top level template should have clickable TOC for while site
4. Put licence icon and link to terms at bottom of navigation panel
5. Colophon page could link to site explaining why various tools were chosen and how to use them. 
6. Pages rather than posts and hierarchical organization.


# Pelican configuration issues

These are the plugins used:

PLUGIN_PATHS = ["../pelican-plugins",]
PLUGINS = [
  'extract_toc',
  'pandoc_reader', // no longer need special version
  'category_meta', // allows index.md file in each directory to specify category
  'neighbors', // doesn't seem to work properly
  'series', // look at adding page hierarchy plugins
]

# settings added by jeff

# these aren't working...It would be nice to be able to save notes and stuff somewher inside content.
PAGE_PATHS = ['pages']
PAGE_EXCLUDES = ['/support']
IGNORE_FILES = ['.#*']

USE_FOLDER_AS_CATEGORY = True
#READERS = {'md': MARKDOWN, PandocReader} // is markdown reader needed here?
# MARKDOWN = {
#   'extension_configs': {
#     'markdown.extensions.toc': {}
#   }
# }


# The next two parameters provide input to pandoc_reader
# Additional command line parameters can be passed to pandoc via the PANDOC_ARGS parameter.

PANDOC_ARGS = [
  #'--mathjax',  // look into moving to mathjax in future
  '--data-dir=./support',
  '--template=pelican.html',
  '--filter=pandoc-citeproc', //switch to --citeproc for new systems
  #'--citeproc',
  #'--filter=pandoc-sidenote',  // works for linux, not windows
  '--lua-filter=./support/notesymbol.lua',
  '--katex=https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/',  // not working on windows
  '--toc',
  '-s',
  '--toc-depth=3',
  '--number-sections',
  '--no-highlight',
]

# Pandoc's markdown extensions can be enabled or disabled via the PANDOC_EXTENSIONS parameter.

PANDOC_EXTENSIONS = [
  '-hard_line_breaks',
  '+citations',
]

# note that a custom pandoc template is used to generate minimal html for use with jinja templates

try this for settings:

   PATH_METADATA = '(?P<path_no_ext>.*)\..*'
    ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}.html'



