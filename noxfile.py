from pathlib import Path

import nox

class NoxfileDocs:

    '''NoxfileDocs class added to attempt to add docstrings to Sphinx automodule.

    noxfile Documentation:
    ======================

    Note: Currently only this class docstring shows in Sphinx

    ..todo:: Get Noxfile session docstrings to display in Sphinx

    Examples:
    ---------

    Local Server Tasks:
    ~~~~~~~~~~~~~~~~~~~

    .. code-block:: python

        # Bring up Healthy Meals in local server.
        nox -s localup

        # Build documentation locally to Sphinx.
        # Note: ignore modules.rst warnings (they are manually in index.rst).
        nox -s makeDocs

        # Rebuild all documentation to Sphinx (cleans up old docs).
        # Note: ignore modules.rst warnings (they are manually in index.rst).
        nox -s remakeDocs

        # Run automated tests (with test coverage) locally.
        nox -s testing

    Docker Tasks:
    ~~~~~~~~~~~~~

    .. code-block:: python

        # Bring up Healthy Meals in docker.
        nox -s dockerUp

        # Only bring up Healthy Meals in docker if not up already.
        nox -s dockerEnsureUp

        # Bring down Healthy Meals in docker.
        nox -s dockerDown

        # Generate the documentation using Sphinx through docker.
        nox -s dockerMakeDocs

        # Regenerate the documentation using Sphinx through docker (cleans up old docs).
        nox -s dockerRemakeDocs

        # Output docker logs out to console. (hit <ctrl>c to stop).
        nox -s dockerLogs

        # Run automated tests (with test coverage) in docker.
        nox -s dockerTests

    '''

    ##################################################################################
    # Local Server tasks


    @nox.session
    def localUp(session):
        #: Bring up Healthy Meals locally.
        ''' Bring up Healthy Meals in local server.'''
        session.run("python3", "managepy", "runserver")


    @nox.session
    def makeDocs(session):
        """Build documentation locally to Sphinx.

       Note: ignore modules.rst warnings (they are manually in index.rst).

        """
        session.run("make", "apidocs", "--directory=docs")
        session.run("make", "html", "--directory=docs")


    @nox.session
    def remakeDocs(session):
        """Rebuild all documentation to Sphinx (cleans up old docs).

        Ignore the warning about modules.rst not included in the toctree,
        as modules are manually entered into index.rst

        """
        session.run("rm", "-fr", "docs/build")
        session.run("make", "apidocs", "--directory=docs")
        session.run("make", "allhtml", "--directory=docs")


    @nox.session
    def testing(session):
        """Run automated tests (with test coverage) through docker."""
        with Path.open("./docs/qa/coverage_run.txt", "w") as out:

            # ensure session is all set up
            session.install("-r", "requirements.txt")
            session.run('python3', 'manage.py', 'makemigrations')
            session.run('python3', 'manage.py', 'migrate')
            session.run('sass', 'static/scss:static/css')
            session.run('python3', 'manage.py', 'collectstatic', '--noinput')

            # empty out tests and coverage directories
            session.run("rm", "-fr", "./docs/qa/tests")
            session.run("rm", "-fr", "./docs/qa/coverage")
            session.run("mkdir", "-p", "./docs/qa/tests/")
            session.run("mkdir", "-p", "./docs/qa/coverage/")

            session.run("coverage", "run", "-m", "pytest", "tests",
                "--junitxml=./docs/qa/tests/junit.xml",
                "--html=./docs/qa/tests/index.html",
                stdout=out, # output to ran_coverage.txt
            ) # run tests with coverage
            session.run("genbadge", "tests",
                "--input-file", "./docs/qa/tests/junit.xml",
                "--output-file", "./docs/qa/tests/tests_badge.svg",
                stdout=out, # output to ran_coverage.txt
            ) # create tests badge
            session.run("coverage", "xml",
                "-o", "./docs/qa/coverage/coverage.xml", # xml output file
                stdout=out, # output to ran_coverage.txt
            ) # create coverage.xml file
            session.run("coverage", "html",
                "-d", "./docs/qa/coverage/html/", # html output directory
                stdout=out, # output to ran_coverage.txt
            ) # create coverage HTML files
            session.run("rm", "-f",
                "./docs/qa/coverage/html/.gitignore", # ensure all files go to repo
            )
            session.run("genbadge", "coverage",
                "--input-file", "./docs/qa/coverage/coverage.xml",
                "--output-file", "./docs/qa/coverage/coverage_badge.svg",
                stdout=out, # output to ran_coverage.txt
            ) # create coverage badge


    ##################################################################################
    # Docker tasks

    @nox.session
    def dockerUp(session):
        '''Bring up Healthy Meals in docker.'''
        session.run("docker", "compose", "up", "--build", "--detach")


    @nox.session
    def dockerEnsureUp(session):
        '''Only bring up Healthy Meals in docker if not up already.'''
        session.run("docker", "compose", "up", "--build", "--detach", "--no-recreate")

    @nox.session
    def dockerDown(session):
        '''Bring down Healthy Meals in docker.'''
        session.run("docker", "stop", "hm_web_image")
        session.run("docker", "stop", "healthy_meals_5-pg_db-1")


    @nox.session
    def dockerMakeDocs(session):
        """Generate the documentation using Sphinx through docker."""
        session.run("docker", "exec", "-it", "hm_web_image", "toc", "-s", "makeDocs")


    @nox.session
    def dockerRemakeDocs(session):
        """Regenerate the documentation using Sphinx through docker (cleans up old docs)."""
        session.run("docker", "exec", "-it", "hm_web_image", "toc", "-s", "remakeDocs")


    @nox.session
    def dockerLogs(session):
        """Output docker logs out to console. (hit <ctrl>c to stop)."""
        session.run("docker", "compose", "logs", "--follow")


    @nox.session
    def dockerTests(session):
        """Run automated tests (localtest) through docker."""
        session.run("docker", "exec", "-it", "hm_web_image", "nox", "-s", "testing")



    ##################################################################################
    # To Do: Other Local Tasks


    @nox.session
    def ruff(session):
        """ run the ruff code standards tool """
        with Path.open("./docs/qa/ruff_run.txt", "w") as out:
            session.run("ruff", "check", stdout=out) # optional parameter: "--fix")

    @nox.session
    def mypy(session):
        """ run the mypy type checker """
        with Path.open("./docs/qa/mypy_run.txt", "w") as out:
            session.run("mypy",
                "./healthymeals",
                "--xslt-html-report",
                "./docs/qa/mypy/",
                stdout=out,
            )

    @nox.session
    def flake8(session):
        """ run the flake8 code standards tool """
        with Path.open("./docs/qa/flake8_run.txt", "w") as out:
            session.run(
                "flake8",
                "./healthymeals",
                "--exit-zero",
                "--format=html",
                "--htmldir=./docs/qa/flake8/html",
                "--statistics",
                "--tee",
                "--output-file",
                "./docs/qa/flake8/flake8stats.txt",
                "--config=setup.cfg",
                "--select=E251",
                stdout=out,
            ) # run flake8 tool
            session.run("genbadge", "flake8",
                "--input-file", "./docs/qa/flake8/flake8stats.txt",
                "--output-file", "./docs/qa/flake8/flake8_badge.svg",
                stdout=out,
            ) # create coverage badge

    @nox.session  # noqa: ERA001
    def djlint(session):  # noqa: ERA001
        """ run the djlint code standards tool """  # noqa: ERA001
        with Path.open("./docs/qa/djlint_run.txt", "w") as out:
            session.run("djlint", "./healthymeals")  # noqa: ERA001

    @nox.session  # noqa: ERA001
    def pylint(session):  # noqa: ERA001
        """ run the pylint code standards tool """  # noqa: ERA001
        with Path.open("./docs/qa/pylint_run.txt", "w") as out:
            session.run("pylint", "./healthymeals")  # noqa: ERA001
