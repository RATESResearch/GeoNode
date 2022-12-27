# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = src
BUILDDIR      = src/_build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).

conf: 
  wget https://raw.githubusercontent.com/RATESResearch/RGVFlood/main/src/conf.py -O src/conf.py
  wget https://raw.githubusercontent.com/RATESResearch/RGVFlood/main/requirements.txt -O requirements.txt
  wget https://raw.githubusercontent.com/RATESResearch/RGVFlood/main/config.ini -O config.ini
	virtualenv -p /usr/bin/python3 .venv; . .venv/bin/activate; pip install -r requirements.txt

fire:
	. .venv/bin/activate ; $(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O); firebase deploy
	
docs:
	. .venv/bin/activate ; $(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O); $(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O); $(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
# ANE
# Add .nojekyll to docs folder to prevent github-pages from doing its thing
# copy index.html to docs folder to redirect github-pages to html folder
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	