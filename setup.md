Create virtual environment for Pelican and install needed libraries
Initialize pelican project
Clone github repositories for project, content, and theme
Copy pandoc.html template into pandoc data/templates directory

# Setup for Pelican

## Old Setup process

1. Install venv via sudo apt install python3-venv
2. create virtual environment for pelican via python3 -m venv pelican
3. Activate virtual environment via source pelican/bin/activate
4. Install required packages via pip install -r requirements.txt

## Problems

Unfortunately, this creates an environment in the shared project directory tree that will not work correctly on any machine other than the one on which it was created. Let's try something different.

0. Create ~/venv directory to hold local venvs
1. Install venv via sudo apt install python3-venv
2. create virtual environment for pelican via python3 -m venv ~/venv/pelican
3. Activate virtual environment via source pelican/bin/activate
4. Install required packages via pip install -r requirements.txt
5. pelican-themes -i ../themes/aluminum
6. make devserver or clean or html

* problems with extract_toc, bs4 dependency (renamed?)
* cannot find ieee.csl for citeproc check posts/...linux_specific/packaging.md header format
see example in probability/uncertainty
* correct symbol form margin note in tufte page.
* Wierd sentence in least squared fitting page

# Others

pandoc-sidenote can be installed via apt-get in linux but for windows it is a pain.
pandoc-citeref is no longer needed, uses internal library