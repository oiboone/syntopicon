---
# This is a YAML Header (1st line must not be blank, but must be preceeded by blank line)
#
# parse with pandoc -s -S --filter pandoc-citeproc --toc --number-sections pandoc.md -o pandoc.tex
# for pandoc versions < 2
# or parse with pandoc -s --filter pandoc-citeproc --toc --number-sections pandoc.md -o pandoc.tex
# for pandoc version => 2
# Note that comments in YAML header don't appear in output files (even HTML)
#
title: Work Version of Pandoc and Friends
author: Jeffrey A. Jalkio
date: 2020-01-25
orig_date: 2018-03-08
bibliography: [support/MyLibrary.bib]
csl: [support/ieee.csl]

# output:
#   custom_document:
#     path: pandoc-jaj.pdf
#     pandoc_args: ["-s"]

# Panzer style info (deprecated)
style: Notes
styledef:
    Notes:
        all:
            metadata:
                numbersections: true
                fontsize: 12pt
            commandline:
 #               smart: true
                standalone: true
                table-of-contents: true
            filter:
                - run: pandoc-citeproc
                
---

<!---
% Work Version of Pandoc and Friends
% Jeffrey A. Jalkio
% 2017-02-12

<!---
 This is a hidden comment that will not appear in generated files (except for html files)
-->

Introduction
============

In this paper, we'll present a suite of tools for technical writing that makes life easier and better than using either Word or \LaTeX.
This recommended set of tools is:

* Pandoc
* Pweave
* Microsoft Visual Studio Code editor, with these extensions:
	* markdownlint
	* vscode-pandoc
	* python
    * Markdown Preview Enhanced
* Zotero reference manager, with this extension:
	* Better Bibtex


It is assumed that you already have a working installation of python and \LaTeX .

Each of these tools is cross-platform (Linux, Windows, and OSX) and FLOSS (free, libre, open source software). The role of each in the writing process is described briefly below.

## Pandoc

[Pandoc](http://pandoc.org/) is a filter written in Haskell that converts between a wide variety of text formats. This includes HTML, Microsoft Word's docx, LibreOffice's odt, and \LaTeX. Through these formats and others it is possible to produce pdf's, Ebooks, web pages, slideshows, and man pages for software.

Pandoc supports an extended version of the lightweight markup language Markdown that provides for inclusion of images, equations,and references and allows extension filters to provide additional functionality. Some of the currently available [filters](https://github.com/jgm/pandoc/wiki/Pandoc-Filters) provide automatic numbering of equations and figures and other useful features.

One filter provided with pandoc is pandoc-citeproc, which provides a powerful bibliography generation system similar to Bibtex but with the flexibility of csl (citation style language) support.

Note: you may want to include panzer also. If so include edit of source code (add to eliminate double spacing of tex output by adding newline='' parameter to file write:

```python
   else:
            with open(self.options['pandoc']['output'], 'w', newline='',
                      encoding=const.ENCODING) as output_file:
                output_file.write(self.output)
                output_file.flush()
```
## PWeave

[PWeave](http://mpastell.com/pweave/) is a filter program for generating scientific reports that include data or plots from Python. It allows a user to create a Markdown document that includes python scripts in clearly labeled 'chunks' and will execute those chunks and place the output into the generated document.

## Zotero

[Zotero](https://www.zotero.org/) is a reference management tool that allows for easy clipping of bibliographic data from webpages, searching of pdfs and other documentation, annotation and organization of references, and generation of citations and bibliographies. Using the extension [better bibtex](https://github.com/retorquere/zotero-better-bibtex) one can generate a bibtex format bibliography file and can simplify the process of pulling citation reference id's into a document. Note: mention refgen.bat routine for making it easier to insert references in text. 

## Visual Studio Code

Microsoft has produced a surprisingly good, open source, cross platform text editor. It provides syntax highlighting for many languages, a great deal of customizability, and an integrated command line. Vscode (run as code from the command line) can be opened in a directory to provide project level editing of files in that directory tree. Note: mention hacking of markdown syntax file to allow highlighting of fenced python code.

## Python and LaTeX

In order to use PWeave, you'll need to know python and have it installed on your computer. [Think Python](http://greenteapress.com/wp/think-python/) is a FLOSS python tutorial and [Anaconda](https://www.continuum.io/downloads) provides a nice python installation for scientific use.

If you want to produce pdf files or Beamer slide presentations, you'll want a LaTeX  installation also.

## Overview of what follows

Together, these programs provide an environmetn that makes writign of technical documents painless and enjoyable. In the following sections we'll look at aspects of using each of these tools and how they work together.

Pandoc Markdown Language
========================

Before we look at the use of pandoc as a filter, we should get to know the pandoc markdown language.

Markdown Variations
-------------------

Markdown comes in many varieties. The list of registered variants can be found 
[here](https://www.iana.org/assignments/markdown-variants/markdown-variants.xhtml) and a more complete unofficial list is 
[here](https://github.com/jgm/CommonMark/wiki/Markdown-Flavors). Pandoc's version of Markdown includes most of the features found in the other variants and the pandoc program can be used to convert Pandoc Markdown into most of the other common formats as well as a wide variety of other text formats. Therefore, we'll be focusing on Pandoc Markdown in the following text. However, it's worth taking a quick look at the differences between the major flavors.

* John Gruber's orignal Markdown is described [here](http://daringfireball.net/projects/markdown/syntax#list). It was intended to be a shorthand for HTML and allows inline HTML to be included as needed.
* [CommonMark]() was developed to provide a standard definition for basic markdown since the original definition was too vague. It's a subset that should be common to all other varieties.
* [Github Flavored Markdown]() (also known as GFM) is used for documentaiton on Github and other websites. It allows URL autolinking, strikethrough, fenced code blocks, syntax highlighting, and tables. It only allows certain HTML to be embedded.
* [Markdown Extra](https://michelf.ca/projects/php-markdown/extra/) adds similar features to GFM
* [MultiMarkdown]() adds features like tables, footnotes, citations, and the ability to output to multiple formats other than HTML. It's similar to pandoc's markdown but implements the additional features differently. Since it doesn't support as many output formats I prefer pandoc. The one nice feature that Multimarkdown has which is absent in pandoc is the glossary feature. Of course this could in theory be added via a custom pandoc filter.

[This website](https://css-tricks.com/choosing-right-markdown-parser/) lists the versions of markdown that support various features.

Features and Syntax
-------------------

### Basic Formating

Text can be highlighted with single asterisks to produce *italicized text* or with two asterisks to produce **bold** texts. Actual 
linebreaks in the 
original text are irrelavent to the formatting of the final output. A blank line is needed to separate paragraphs.

To force line breaks without blank lines, you can use a backspace at the end of a line\
like these\
lines have.

### Lists

* Bullet lists are easy
* Including multi-level
  * lists
  * like this
    * or this
    * or this

The list above is a compact list. One can also put blank lines between the bullet items

* Like this

* or this which has multiple paragraphs. All but the first indented by 4 spaces

    like this one does.

    Or this very short paragraph.
    
* While this starts the next bulleted item.

1) numbered list are easy to generate
4) The actual numbers don't matter except the frst one.
17) Each item is assigned the next consecutive number.

I) You can even have lists with Roman numerals
II) By simply using I instead of 1.
    A) or alphabetic ones for outlines
        i) or lower case romans
        ii) like this
    b) or lower case alpha

### Horizontal rules

Horizontal rules can be produced by

---

(three -)

*** 

(three *)
or

___

(three _)

These can be preceded by 0 to 3 spaces. Spaces are also allowed between the characters or after them.

### Headings

Headings can be specified two different ways. ATX style headings have one to 6 hashtags to indicate heading level. With #Heading being the highest level and ###### being subsubsubsubsubsubsections. Setext format can be used to indicate top level headings which are underlined by ===== or second level headings underlined by ---. My impression is that the raw markdown is most readable if Setext headings are used for level one and two headings. 

### Indented Code blocks

    Text indented by 4 spaces
    is passed verbatim to the output and isn't processed as markdown. 
    The leading spaces are removed from the text and it is 
    printed in monospace font like this.

### Fenced codeblock

Three backticks or three tildes can be used to start or end a section of code. An info string can follow the opening fence to indicate the language (so that syntax highlighting works).  

For example: 

```python

""" Docstring Header
Here's a classic recursive definition of factorial
"""

def fact(n):
    if (n == 0):
        return 1
    else:
        return n*fact(n-1)

for j in range(10):
    print j, fact(j)
```

It is also possible to include an identifier tag, one or more classes, and other attributes in braces:

    ```{python .numberLines startFrom="100" echo=True results='verbatim'}
    for i in range(10):
        print "Hello world"
    ```

.python (or python) is a class indicating the language to use, .numberlines is a class indicating that lines should be numbered. startFrom is an attribute used by pandoc to specify the initial line number and echo and results are attributes used by pweave to specify how to display results. This code yields

```{.python .numberLines startFrom="100" }

for i in range(10):
    print "Hello world"

```

Note that you must be careful of capitalization in attributes (camelCase is used) and of spacing around the = sign (none) or things won't work.

### Equations

Standard \LaTeX  equations work in Pandoc Markdown. Single $'s surround equations like : $x=e^{-\alpha t}$ and double $'s surround display equations like this :

$$y=\int_{-\infty}^\infty e^{-x ^ 2 /{2 \sigma^2}} dx$$

### Links

Links to URI's can be as simple as surrounding the URI with pointy brackets (e.g. \< URI \>) as in <http://google.com> <mailto:jajalkio@stthomas.edu> or specifying the link inline as \[title text](url) as in [Write me!](mailto:jajalkio@stthomas.edu).

It's also possible to use reference links where the text simply includes a reference to the hyperlink in square brackets, like this [link] and another line (either before or after) contains the definition of the link. For example, we could include the line:

\[link]: http://www.waste.org "Optional Title"

to define the link URI and provide an optional title.

[link]: http://www.waste.org "Optional Title"

You can also have internal links to other sections of your document by refering to the section title. For example [Headings].

### Images

Any of the link formats mentioned in the preceeding section can be used to specify an image by preceding the link with an !.
For example \![paste](./images/solderpaste.jpg "paste plot"){width=20%}  is an image of solderpaste like this 
![paste]({static}./images/solderpaste.jpg "paste plot"){width=20%}. An image specified on it's own line is treated as a standalone figure.

![pdf file image format]({static}./images/matlab.pdf "fake title"){width=20%}

![example of a png file]({static}./images/raster_example.png "fake title"){width=20%}

Note: it appears that pdf images and the \{width=20%} attribute don't work in docx format. Examine further....

### Footnotes

A Link reference preceeded with a caret is treated as a footnote. For example \^\[This is a footnote.] yields this ^[This is a footnote.]. Also a reference whose link name starts with a caret is treated as a footnote which is defined elsewhere in the file. So \[^1] becomes a link like this [^1] if later in the file you have the definition:

\[^1]: Here's a silly footnote. ...

[^1]: Here's a silly footnote. This style of footnote can span multiple lines and can even include other things like

    Multiple paragraphs as long as their first line is indented.

    1. lists
    2. more lists

The first non-indented paragraph after the note definiton signals the end of the footnote.

### Citations

See the Zotero section on generatign and maintaining your Bibtex bibliogrphaphy file. In that file, each refernce will have a reference id code. To cite a reference just include `[@refid]` in your text. For example [@lehman2006]. If you want to include a footnote that contains the citation, you can do something like `^[See ref @patashnik1988, p. 10]` to get the desired result ^[See ref @patashnik1988, p. 10].

Use ` <div id="refs"></div>` to specify where the reference section should be placed (if not at the end of your document). For example, let's but our bibliography right here :

<div id="refs"></div>

### Tables

We can add tables via 

 Right     Left     Center     Default
-------    ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1

Table:  Demonstration of simple table syntax.

-------------------------------------------------------------
 Centered   Default           Right Left
  Header    Aligned         Aligned Aligned
----------- ------- --------------- -------------------------
   First    row                12.0 Example of a row that
                                    spans multiple lines.

  Second    row                 5.0 Here's another one. Note
                                    the blank line between
                                    rows.
-------------------------------------------------------------

Table: Here's the caption. It, too, may span
multiple lines.

: Sample grid table.

+---------------+---------------+--------------------+
| Fruit         | Price         | Advantages         |
+===============+===============+====================+
| Bananas       | $1.34         | - built-in wrapper |
|               |               | - bright color     |
+---------------+---------------+--------------------+
| Oranges       | $2.10         | - cures scurvy     |
|               |               | - tasty            |
+---------------+---------------+--------------------+

| Right | Left | Default | Center |
|------:|:-----|---------|:------:|
|   12  |  12  |    12   |    12  |
|  123  |  123 |   123   |   123  |
|    1  |    1 |     1   |     1  |

  : Demonstration of pipe table syntax.

