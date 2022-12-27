# -*- coding: utf-8 -*-
import os, sys, re, toml

sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PYPROJECT_TOML = toml.load(os.path.join(PROJECT_ROOT,'pyproject.toml'))
# SPYCE_TOML = toml.load(os.path.join(PROJECT_ROOT,basename(Repo('..').get_config().get(('remote', 'origin'), 'url')).decode("utf-8").strip('.git')+'.toml'))
SPYCE_TOML = toml.load(os.path.join(PROJECT_ROOT,'spyce.toml'))

name = PYPROJECT_TOML['tool']['poetry']['name']
project = PYPROJECT_TOML['tool']['poetry']['description']
author = PYPROJECT_TOML['tool']['poetry']['authors'][0]
release = SPYCE_TOML['sphinx']['document_id']
copyright = SPYCE_TOML['sphinx']['copyright_year'] \
    + ', ' \
    + SPYCE_TOML['sphinx']['organization']
sponsor = SPYCE_TOML['sphinx']['sponsor']
latex_logo = SPYCE_TOML['sphinx']['latex_logo']
html_logo = SPYCE_TOML['sphinx']['html_logo']
techreviewer = SPYCE_TOML['sphinx']['techreviewer']
techtitle = SPYCE_TOML['sphinx']['techtitle']
finalreviewer = SPYCE_TOML['sphinx']['finalreviewer']
finaltitle = SPYCE_TOML['sphinx']['finaltitle']

# -- General configuration ---------------------------------------------------

extensions = [
# 'slides.slides',
'sphinxcontrib.bibtex',
'sphinx.ext.autodoc',
'ablog',
'sphinx.ext.intersphinx',
'sphinx.ext.todo',
'sphinx.ext.autosummary',
# 'invocations.autodoc',
'sphinxcontrib.plantuml',
"sphinx_revealjs",
'sphinxcontrib.programoutput',
# 'zot4rst.sphinx',
# 'sphinx_immaterial',
]

autosummary_imported_members = True

autodoc_docstring_signature = True

slide_include_slides = True

# templates_path = ['_static']
intersphinx_mapping = {'rgvflood': ('https://glossary.rgvflood.com/en/latest', None)}
source_suffix = ".rst"
master_doc = "index"
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = 'sphinx'
numfig = True
numfig_format = {'figure': 'Figure: %s', 'table': 'Table: %s', 'code-block': 'Listing: %s', 'section': 'Section: %s'}


# -- Options for ablog output ---------------------------------------------------

blog_authors = {
    'Andy': ('Andrew Ernest', 'http://water-wizard.org'),
}
blog_default_author = "Andy"

# -- Options for bibtex output ---------------------------------------------------

bibtex_default_style = 'plain'
bibtex_reference_style = 'super'
bibtex_bibfiles = ['references.bib']

# -- Options for plantuml output ---------------------------------------------------

plantuml = "plantuml"

# -- Options for todo output ---------------------------------------------------

todo_include_todos = True

# -- Options for HTML output ---------------------------------------------------

on_rtd = False

if on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_theme_options = {
    "style_external_links" : True,
    }
else:
    # html_theme = 'sphinx_immaterial'
    html_theme = 'alabaster'
    # html_theme = 'nature'
    # html_theme = 'agogo'
html_title = project
html_short_title = name
html_baseurl = "https://docs.rgvflood.com"
html_static_path = ['_static']
htmlhelp_basename = project
html_sidebars = {
   '**': [ 
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
        'postcard.html', 
        'recentposts.html',
        'tagcloud.html', 
        'categories.html',
        'archives.html', ]
}

# -- Options for Revealjs Slide output ---------------------------------------------------
revealjs_script_conf = """
    { 
        hash: true,
        width: 1600,
        height: 900,
    }
"""
revealjs_script_plugins = [
    {
        "src": "revealjs4/plugin/highlight/highlight.js",
        "name": "RevealHighlight",
    },
    {
        "src": "revealjs4/plugin/notes/notes.js",
        "name": "RevealNotes",
    },    
]
revealjs_static_path = ['_static']
revealjs_style_theme = 'bluetunnel.css'


# -- Options for LaTeX output --------------------------------------------------
maketitle = r''' 
\sphinxmaketitle
    %\renewcommand{\familydefault}{\sfdefault}
    \newcommand\signature[3]{% Role; Name; Department
    %\begin{center}
    {\sffamily
    \vspace{1cm}\par
    \textbf{#1}:\par
        \begin{minipage}{10cm}
        \centering
        \vspace{3cm}\par
        \rule{10cm}{1pt}\par
        \textbf{#2}\par
        #3%
        \end{minipage}
    }
    %\end{center}
    }
    \newcommand\insertdate[1][\today]{\vfill\begin{flushright}#1\end{flushright}}
    {\LARGE\sffamily \textbf{Approval Page}}
    
    \signature{Technical Review By}{<techreviewer>}{<techtitle>}
    
    \signature{Final Approval For Submission}{<finalreviewer>}{<finaltitle>}
        
    \insertdate
'''

maketitle = re.sub('<techreviewer>', techreviewer, maketitle)
maketitle = re.sub('<techtitle>', techtitle, maketitle)
maketitle = re.sub('<finalreviewer>', finalreviewer, maketitle)
maketitle = re.sub('<finaltitle>', finaltitle, maketitle)

latex_elements = {
'pointsize': '12pt',
'preamble': '\\usepackage{svg}',
'releasename': html_title+'\par Project Deliverable ID',
'extraclassoptions': 'openany,oneside',
'babel': '\\usepackage[american]{babel}',
'maketitle': maketitle,
}
authors = author
latex_documents = [
  ('index', name+'.tex', sponsor,
   authors, 
   'manual'),
]

latex_show_urls = 'footnote'

latex_appendices = ['glossary']
