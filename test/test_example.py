from .base import MyTestCase


class TestMyApp(MyTestCase):
    def test_get_message(self):
        doc = {'result': [{'item': 'Amazoooooooooooon'}]}

        result = self.simulate_get('/example')
        self.assertEqual(result.json, doc)

