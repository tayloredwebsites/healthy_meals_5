# Makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
PROJECT = django_project
APPSDIR = ..

.PHONY: html allhtml apidocs Makefile

# Put it first so that "make" without argument is like "make html".
html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

# Outputs rst files from django application code
# Note: all arguments to sphinx-apidoc are relative to --directory argument of make command (or directory run in)
allhtml:
	@$(SPHINXBUILD) --builder html --write-all --fresh-env "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

# Outputs rst files from django application code
# Note: all arguments to sphinx-apidoc are relative to --directory argument of make command (or directory run in)
apidocs:
	sphinx-apidoc -o $(SOURCEDIR) $(APPSDIR) ../*/migrations ../django_project ../docs/* ../manage.py

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
