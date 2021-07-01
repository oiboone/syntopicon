---
title: mo html mo problems
date: 2020-07-22
---

## Issues with static site generator

* look into static content like images and where to store them, how to reference them

* display of pdfs is bad. viewer embedded in page

* Allow different pandoc options for different files. Mod pandoc reader to read options form yaml in file.

* Fix templates to add *.html to page links

* Nexted categories <https://pypi.org/project/pelican-more-categories/> and <https://github.com/getpelican/pelican-plugins/tree/master/subcategory>

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
    b. Change color scheme to solarized
    <https://guizishanren.com/change-syntax-highlight-with-pygments-CSS-for-Pelican-blog/>
    c. Design site page structure and layouts
    d. change pygments color scheme to solarized

2. Merge in tufte style
    a. fullwidth class
    b. newthought class
    d. epigraphs style
    e. consider a background change or border for sidenotes and margin notes when expanded in mobile mode.

