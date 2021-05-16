import json
import unittest
from hello_world import app
from hello_world.formater import SUPPORTED

powitanie_test = {"msg": "Hello World!", "imie": "Kasia"}

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        rj = json.loads(rv.data)
        self.assertEqual(powitanie_test['imie'], rj['imie']) # noqa
        self.assertEqual(powitanie_test['msg'], rj['msg'])
    def test_msg_with_output1(self):
        rv = self.app.get('/?output=xml')
        self.assertEqual(b"<greetings><name>Kasia</name><msg>Hello World!</msg></greetings>", rv.data) # noqa
