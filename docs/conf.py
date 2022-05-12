# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
# serve to show the default.

import os
import sys

#on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
on_rtd = True

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'RGVFlood'
copyright = '2021, Research, Applied Technology, Education & Service, Inc.'
author = 'Andrew N.S. Ernest, Ph.D., P.E., BCEE, D.WRE'

# The full version, including alpha/beta/rc tags
release = '0.9.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#'myst_parser',
#'sphinxcontrib.plantuml',
'sphinxcontrib.bibtex',
'sphinx.ext.autodoc',
'hieroglyph',
'sphinx.ext.todo',
'sphinxcontrib.plantuml',
]

bibtex_bibfiles = ['refs.bib']
plantuml = 'java -jar /usr/share/plantuml/plantuml.jar'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []
# Display todos by setting to True
todo_include_todos = True

numfig = True
#numfig_format['figure'] = 'Figure %s'
numfig_format = {'figure': 'Figure: %s', 'table': 'Table: %s', 'code-block': 'Listing: %s', 'section': 'Section: %s'}

# -- Options for HTML Slide output ---------------------------------------------------

slide_theme = 'slides2'
#slide_theme_path = ['_static']
#slide_theme_options = {
#    'presenters': [
#        {
#            'name': 'Andrew N.S. Ernest, Ph.D., P.E., BCEE, D.WRE',
#            # 'twitter': '@author',
#            # 'www': 'http://example.com/author',
#            # 'github': 'http://github.com/author/example'
#        },
#    ],
#}
#slide_theme_options = {'custom_css':'custom.css'}

# slide_link_html_to_slides = not on_rtd
# slide_link_html_sections_to_slides = not on_rtd
# slide_relative_path = "./slides/"
#
# slide_link_to_html = True
# slide_html_relative_path = "../"

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
if on_rtd:
    import sphinx_rtd_theme

    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

else:
    html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "RGVFlood"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "RGVFlood"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'RGVFlood'

pdf_documents = [('index', u'rst2pdf', u'Sample rst2pdf doc', u'Your Name'),]
# index - master document
# rst2pdf - name of the generated pdf
# Sample rst2pdf doc - title of the pdf
# Your Name - author name in the pdf

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '12pt',

# Additional stuff for the LaTeX preamble.
'preamble': '\\usepackage{svg}',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'RGVFlood.tex', u'RGVFlood',
   u'Andrew N.S. Ernest, Ph.D., P.E., BCEE, D.WRE \\and Christopher B. Fuller, Ph.D. \\and William Kirkey, Ph.D. \\and Peter Kirkey, \\and Linda Navarro, \\and Ivan Santos-Chavez, \\and Carlos Reyes',
   'manual'),
  ('requirements/index', 'Requirements.tex', u'RGVFlood User Inteface Requirements Determination',
   u'Andrew N.S. Ernest, Ph.D., P.E., BCEE, D.WRE \\and Christopher B. Fuller, Ph.D. \\and William Kirkey, Ph.D. \\and Peter Kirkey, \\and Linda Navarro, \\and Ivan Santos-Chavez, \\and Carlos Reyes',
   'manual'),
  ('predevelopment/index', 'Predevelopment.tex', u'RGVFlood Pre-Development Plan',
   u'Andrew N.S. Ernest, Ph.D., P.E., BCEE, D.WRE \\and Christopher B. Fuller, Ph.D. \\and William Kirkey, Ph.D. \\and Peter Kirkey, \\and Linda Navarro, \\and Ivan Santos-Chavez, \\and Carlos Reyes',
   'manual'),
  ('implementation/index', 'Implementation.tex', u'RGVFlood User Interface Implemention',
   u'Andrew N.S. Ernest, Ph.D., P.E., BCEE, D.WRE \\and Christopher B. Fuller, Ph.D. \\and William Kirkey, Ph.D. \\and Peter Kirkey, \\and Linda Navarro, \\and Ivan Santos-Chavez, \\and Carlos Reyes',
   'manual'),
  ('model_requirements/t1requirements/index', 'T1Requirements.tex', u'Tier I Real-Time Model Requirements Determination',
   u'Andrew N.S. Ernest, Ph.D., P.E., BCEE, D.WRE \\and Christopher B. Fuller, Ph.D. \\and William Kirkey, Ph.D. \\and Peter Kirkey, \\and Linda Navarro, \\and Ivan Santos-Chavez',
   'manual'),   
  ('model_requirements/t2requirements/index', 'T2Requirements.tex', u'Tier II Sub-Regional Model Requirements Determination',
   u'Andrew N.S. Ernest, Ph.D., P.E., BCEE, D.WRE \\and Christopher B. Fuller, Ph.D. \\and William Kirkey, Ph.D. \\and Peter Kirkey, \\and Linda Navarro, \\and Ivan Santos-Chavez',
   'manual'),      
  ('model_requirements/t3requirements/index', 'T3Requirements.tex', u'Tier III Urban Model Requirements Determination',
   u'Andrew N.S. Ernest, Ph.D., P.E., BCEE, D.WRE \\and Christopher B. Fuller, Ph.D. \\and William Kirkey, Ph.D. \\and Peter Kirkey, \\and Linda Navarro, \\and Ivan Santos-Chavez',
   'manual'),         
  ('geodatamodel/index', 'GeoDataModel.tex', u'Survey Data Model Manual',
   u'Christopher B. Fuller, Ph.D., \\and Linda Navarro, \\and Andrew N.S. Ernest, Ph.D., P.E., BCEE, D.WRE \\and William Kirkey, Ph.D. \\and Peter Kirkey, \\and Ivan Santos-Chavez',
   'manual'),   
  ('implementation/survey_manual/index', 'SurveyManual.tex', u'Survey Manual',
   u'Christopher B. Fuller, Ph.D., \\and Linda Navarro, \\and Andrew N.S. Ernest, Ph.D., P.E., BCEE, D.WRE \\and William Kirkey, Ph.D. \\and Peter Kirkey, \\and Ivan Santos-Chavez',
   'manual'),  
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "RATESLogo.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
latex_appendices = ['glossary']

# If false, no module index is generated.
#latex_domain_indices = True
