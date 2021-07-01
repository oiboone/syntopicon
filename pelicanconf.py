#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'aluminum'
AUTHOR = 'Ogden Boone'
SITENAME = 'test site # 1'
SITEURL = ''

PATH = 'content'
#STATIC_PATHS = ['content/pages/web_dev/testing/images']

TIMEZONE = 'America/Chicago'

DEFAULT_DATE = 'fs' # use file system date if none given in metadata
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d(%a)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll (not used in my template)
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget (not used in my template)
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ["../pelican-plugins",]
PLUGINS = [
  'extract_toc',
  'pandoc_reader',
  'category_meta',
  'neighbors',
  'series',
]

# settings added by jeff

# these aren't working...It would be nice to be able to save notes and stuff somewher inside content.
PAGE_PATHS = ['pages']
PAGE_EXCLUDES = ['/support']
IGNORE_FILES = ['.#*']

USE_FOLDER_AS_CATEGORY = True
#READERS = {'md': MARKDOWN, PandocReader}
# MARKDOWN = {
#   'extension_configs': {
#     'markdown.extensions.toc': {}
#   }
# }


# The next two parameters provide input to pandoc_reader
# Additional command line parameters can be passed to pandoc via the PANDOC_ARGS parameter.

PANDOC_ARGS = [
  #'--mathjax',
  '--data-dir=./support',
  '--template=pelican.html',
  '--filter=pandoc-citeproc',
  #'--citeproc',
  '--filter=pandoc-sidenote',
  '--lua-filter=./support/notesymbol.lua',
  '--katex=https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/',
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
