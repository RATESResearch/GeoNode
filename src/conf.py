# -*- coding: utf-8 -*-
import os, sys, datetime, re, toml
from dotenv import load_dotenv

# -- Project information -----------------------------------------------------

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT,'.env'))

sys.path.insert(0, os.path.abspath(os.path.join(PROJECT_ROOT, 'src')))

PYPROJECT_TOML = toml.load(os.path.join(PROJECT_ROOT,'pyproject.toml'))
project = PYPROJECT_TOML['tool']['poetry']['description']
authors = ''
author_list = PYPROJECT_TOML['tool']['poetry']['authors']
for author in author_list:
    if author == author_list[len(author_list)-1]:
        authors += author
    else:
        authors += author + ' \\and '

latex_logo = os.getenv('LATEX_LOGO', default='static/logo.png')
html_logo = os.getenv('HTML_LOGO', default='static/logo.png')
name = os.getenv('NAME', default=os.path.basename(PROJECT_ROOT))
release = os.getenv('DOCUMENT_ID', default='v0.0.0')
copyright_year = os.getenv('COPYRIGHT_YEAR', default=datetime.date.today().year)
# organization = os.getenv('ORGANIZATION', default='Research, Applied Technology, Education and Service, Inc.')
organization = os.getenv('ORGANIZATION', default='RATES, Inc.')
copyright = str(copyright_year) \
    + ', ' \
    + organization
sponsor = os.getenv('SPONSOR', default=organization)

techreviewer = os.getenv('TECHREVIEWER', default=author_list[0])
techtitle = os.getenv('TECHTITLE', default='Technical Reviewer')

finalreviewer = os.getenv('FINALREVIEWER', default=author_list[0])
finaltitle = os.getenv('FINALTITLE', default='Final Reviewer')

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
'sphinxcontrib.mermaid',
# 'sphinx_js',
]

# mermaid_output_format = 'png'
# mermaid_cmd = '/usr/local/bin/mmdc'
# mermaid_verbose = True

js_language = 'typescript'

autosummary_imported_members = True

autodoc_docstring_signature = True

slide_include_slides = True

# templates_path = ['_static']
# intersphinx_mapping = {'rgvflood': ('https://glossary.rgvflood.com/en/latest', None)}
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
bibtex_bibfiles = ['static/references.bib']

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
html_static_path = ['static']
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
revealjs_static_path = ['static']
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
# authors = author
latex_documents = [
  ('index', name+'.tex', sponsor,
   authors, 
   'manual'),
]

latex_show_urls = 'footnote'

latex_appendices = ['static/glossary']
