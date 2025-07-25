#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Martijn Pieters
# Licensed under the MIT license as detailed in LICENSE.txt

#
# aiolimiter documentation build configuration file, created by
# sphinx-quickstart on Wed Mar  5 12:35:35 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from dunamai import Version

if sys.version_info < (3, 11):

    def _read_project_config(path: Path) -> dict[str, Any]:
        import toml

        with path.open() as f:
            return toml.load(f)["project"]

else:

    def _read_project_config(path: Path) -> dict[str, Any]:
        import tomllib

        with path.open("rb") as f:
            return tomllib.load(f)["project"]


_docs_path = Path(__file__).resolve().parent
_project_config = _read_project_config(_docs_path.parent / "pyproject.toml")
_github_path = urlparse(_project_config["urls"]["Repository"]).path
_github_parts = dict(zip(("user", "repo"), _github_path[1:].split("/")))
_name = _project_config["name"]
_authors = ", ".join([a["name"] for a in _project_config["authors"]])


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinxcontrib.spelling",
]

spelling_lang = "en_GB"
tokenizer_lang = "en_GB"

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = _name
copyright = f"2019-{date.today().year}, {_authors}"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
_version = Version.from_git()
version = _version.serialize(format="{major}.{minor}")

# The full version, including alpha/beta/rc tags.
release = _version.serialize()

rst_epilog = f"""
.. |requires-python| replace:: {_project_config["requires-python"].lstrip(">=")}
"""

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# The default language to highlight source code in.
highlight_language = "python3"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "aiohttp_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "logo": None,
    "description": _project_config["description"],
    "canonical_url": _project_config["urls"]["Documentation"],
    "github_user": _github_parts["user"],
    "github_repo": _github_parts["repo"],
    "github_button": True,
    "github_type": "star",
    "github_banner": True,
    "badges": [
        {
            "image": (
                f"{_project_config['urls']['Repository']}/actions/workflows/ci-cd.yml/badge.svg"
            ),
            "target": (
                f"{_project_config['urls']['Repository']}/actions/workflows/ci-cd.yml"
            ),
            "height": "20",
            "alt": "GitHub Actions CI status",
        },
        {
            "image": (
                f"https://codecov.io/github/{_github_parts['user']}/"
                f"{_github_parts['repo']}/coverage.svg?branch=main"
            ),
            "target": (
                f"https://codecov.io/github/{_github_parts['user']}/"
                f"{_github_parts['repo']}"
            ),
            "height": "20",
            "alt": "Code coverage status",
        },
        {
            "image": f"https://img.shields.io/pypi/v/{_project_config['name']}",
            "target": f"https://pypi.org/project/{_project_config['name']}",
            "height": "20",
            "alt": "Latest PyPI package version",
        },
    ],
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = [alabaster.get_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = ''

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = []

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {"**": ["about.html", "navigation.html", "searchbox.html"]}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = f"{_project_config['name']}doc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        "index",
        f"{_name}.tex",
        f"{_name} Documentation",
        f"{_name} contributors",
        "manual",
    )
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", _name, f"{_name} Documentation", [_name], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        _name,
        f"{_name} Documentation",
        _authors,
        _name,
        _project_config["description"],
        "Miscellaneous",
    )
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False
