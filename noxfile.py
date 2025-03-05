from pathlib import Path

import nox

@nox.session
def coverage_tests(session):
    """Run tests through coverage so it also gets the coverage data."""
    with Path.open("./docs/qa/coverage_run.txt", "w") as out:

        # ensure session is all set up
        session.install("-r", "requirements.txt")
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
