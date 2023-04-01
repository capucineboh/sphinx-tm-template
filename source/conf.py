# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from tmconfig import tmconfig


# -- Project information -----------------------------------------------------

project = tmconfig.title
author = tmconfig.author
copyright = f'2023, {author}'

# The full version, including alpha/beta/rc tags
release = tmconfig.release


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    'sphinx_copybutton',
    'sphinx_design',
    'sphinxcontrib.bibtex'
]

# Configure Bibtex
bibtex_bibfiles = ['online.bib']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'fr'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_title = tmconfig.title
html_logo = 'logo.png'
html_favicon = 'favicon.png'

html_theme_options = {
  "home_page_in_toc": True,
  "use_download_button": True,
  "show_navbar_depth": 1,
  "repository_url": tmconfig.repository_url,
  # "use_issues_button": True,
  "use_edit_page_button": True,
}


####### MyST configuration
myst_enable_extensions = ["colon_fence"]


# -- Options for LaTeX output ---------------------------------------------


latex_elements = {
   'papersize':"a4",
   'author': tmconfig.author,
   'date': tmconfig.date(),
   'title': tmconfig.title,
   'release' : tmconfig.release,
   'releasename' : "Collège du sud, Travail de maturité",
   'fontpkg': '\\usepackage{times}',
   'babel': '\\usepackage[francais]{babel}',
   'preamble': r'''
%\usepackage[titles]{tocloft}
%\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
%\setlength{\cftchapnumwidth}{0.75cm}
%\setlength{\cftsecindent}{\cftchapnumwidth}
%\setlength{\cftsecnumwidth}{1.25cm}
\newcommand{\seminarytitle}{<<seminary_title>>}
\newcommand{\customizeinfos}{<<customize_infos>>}
'''.replace(
  '<<seminary_title>>', tmconfig.seminary_title
)
.replace(
  '<<customize_infos>>', r'Modifiez les informations de cette page dans le fichier {\verb tsource/tmconfig.py}' if tmconfig.first_name == 'Prénom' else ''
)
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'tm-ecrit.tex', tmconfig.title,
   tmconfig.author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
latex_show_urls = True

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True
