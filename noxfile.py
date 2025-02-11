
import nox

@nox.session
def tests(session):
    """Run the test suite, including test reports generation and coverage reports. """
    session.install("-r", "requirements.txt")
    session.run('pytest', '--junitxml=reports/junit/junit.xml', '--html=reports/junit/index.html')
    session.run('coverage', 'run', '-m', 'pytest', 'tests') # run tests with coverage
    session.run('coverage', 'xml') # write XML report to 'reports/coverage/coverage.xml'
    session.run('coverage', 'html') # write HTML report to reports/coverage_html/index.html
    session.run('genbadge', 'coverage') # create coverage badge
    session.run('genbadge', 'tests') # create tests badge
