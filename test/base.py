# This test was copy/pasted directly from the falcon framework test documentation.
# Run by CDing into the base project directory (up one from here) and running
# `python -m unittest discover -t . -s test`
from falcon import testing
from worker import app


class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()

        # Assume the hypothetical `app` package has a
        # function called `getApp()` to initialize and
        # return a `falcon.API` instance.
        self.app = app.getApp()
