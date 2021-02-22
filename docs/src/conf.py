#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Oríon documentation build configuration file.

This file is execfile()d with the current directory set to its
containing dir.

Note that not all possible configuration values are present in this
autogenerated file.

All configuration values have a default; values that are commented out
serve to show the default.

If extensions (or modules to document with autodoc) are in another directory,
add these directories to sys.path here. If the directory is relative to the
documentation root, use os.path.abspath to make it absolute, like shown here.

How to document -- sources:

   1. `Numpy Standard <https://numpydoc.readthedocs.io/en/latest/format.html>`_
   2. `Python Standard <https://docs.python.org/devguide/documenting.html>`_
   3. `reST general <http://www.sphinx-doc.org/en/stable/rest.html>`_
   4. `reST reference tags <http://www.sphinx-doc.org/en/stable/domains.html#the-python-domain>`_
   5. `Cross-reference <http://www.sphinx-doc.org/en/stable/domains.html#python-roles>`_

"""
import glob
import os
import re
import sys

docs_src_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, docs_src_path)
src_path = os.path.abspath(os.path.join(docs_src_path, "..", "..", "src"))
sys.path.insert(0, src_path)

import orion.core as orion  # noqa

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

extensions = (
    [  # Extensions must be sorted alphabetically to ease maintenance and merges.
        "numpydoc",
        "sphinxcontrib.httpdomain",  # Documentation directives for the REST API.
        "sphinx_gallery.gen_gallery",
        "sphinx.ext.autodoc",
        "sphinx.ext.autosummary",
        "sphinx.ext.coverage",
        "sphinx.ext.doctest",
        "sphinx.ext.extlinks",
        "sphinx.ext.todo",
        "sphinx.ext.viewcode",
        "sphinx.ext.intersphinx",
    ]
)

# General information about the project.
project = u"orion"
_full_version = orion.__version__
author = orion.__author__
copyright = orion.__copyright__

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = re.sub(r"(.*?)(?:\.dev\d+)?(?:\+.*)?", r"\1", _full_version)
# The short X.Y version.
version = re.sub(r"(\d+)(\.\d+)?(?:\.\d+)?(?:-.*)?(?:\.post\d+)?", r"\1\2", release)

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "_build",
    "_templates",
    "**/pptree.py",
    "user/visualizations.rst",
]

# The name of the Pygments (syntax highlighting) style to use.
highlight_language = "python3"
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = "autolink"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "canonical_url": "",
    "analytics_id": "",
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "both",
    #  'style_external_links': False,
    #  'vcs_pageview_mode': '',
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    #  'includehidden': False,
    #  'titles_only': False
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    "**": [
        "relations.html",  # needs 'show_related': True theme option to display
        "searchbox.html",
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "oriondoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "orion.tex", u"Oríon Documentation", u"Epistímio", "manual"),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "orion", "Oríon Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Oríon",
        "Oríon Documentation",
        author,
        "orion",
        orion.__descr__,
        "Miscellaneous",
    ),
]

# -- Autodoc configuration -----------------------------------------------

autodoc_mock_imports = ["_version", "utils._appdirs"]

# -- Gallery configuration -----------------------------------------------

import plotly.io as pio

pio.renderers.default = "sphinx_gallery"

from plotly.io._sg_scraper import plotly_sg_scraper

image_scrapers = (
    "matplotlib",
    plotly_sg_scraper,
)

import sphinx_gallery.sorting

sphinx_gallery_conf = {
    # "doc_module": ("plotly",),
    "backreferences_dir": "gen_modules/backreferences",
    "reference_url": {
        "sphinx_gallery": None,
    },
    "examples_dirs": ["../../examples/plotting", "../../examples/tutorials"],
    "gallery_dirs": ["auto_examples", "auto_tutorials"],
    "image_scrapers": image_scrapers,
    # "compress_images": ("images", "thumbnails"),
    "filename_pattern": "/plot_",
    "matplotlib_animations": True,
    "ignore_pattern": "python_example.py",
    "within_subsection_order": sphinx_gallery.sorting.FileNameSortKey,
    "remove_config_comments": True,
}

# -- intersphinx configuration ------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "plotly": ("https://plotly.com/python-api-reference/", None),
}


# -- extlinks configuration ---------------------------------------------

extlinks = {
    "scipy.stats": (
        "https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.%s.html",
        "test ",
    ),
    "plotly": ("https://plotly.com/python-api-reference/plotly.%s", "test "),
}


# -- Nitpicky mode ------------------------------------------------------

# Enable nitpicky mode - which ensures that all references in the docs
# resolve.

ignore_algo_attr = [
    "configuration",
    "is_done",
    "should_suspend",
    "space",
    "state_dict",
    "judge",
    "observe",
    "seed_rng",
    "set_state",
    "suggest",
    "name",
    "orion.core.utils.Factory.__call__",  # TODO: Why this one fails???
    "orion.core.utils.singleton.SingletonType.__call__",
    "orion.plotting.base.PlotAccessor.__call__",
]

nitpicky = True
nitpick_ignore = [("py:obj", attr) for attr in ignore_algo_attr]

################################################################################
#                             Numpy Doc Extension                              #
################################################################################

# sphinx.ext.autosummary will automatically be loaded as well. So:
# autosummary_generate = True
# autosummary_generate = glob.glob("reference/*.rst")

# Generate ``plot::`` for ``Examples`` sections which contain matplotlib
numpydoc_use_plots = False

# Create a Sphinx table of contents for the lists of class methods and
# attributes. If a table of contents is made, Sphinx expects each entry to have
# a separate page.
numpydoc_class_members_toctree = False


numpydoc_show_inherited_class_members = False
