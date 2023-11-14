import unittest
from flask.testing import FlaskClient
from slack_practice import SlackApp

class SlackAppTest(unittest.TestCase):
    def setUp(self):
        self.test_verification_token = 'TEST_VERIFICATION_TOKEN'
        self.test_port = 3000
        self.slack_app = SlackApp(verification_token=self.test_verification_token, port=self.test_port)
        self.app_client = self.slack_app.app.test_client()

    def test_slack_event_endpoint(self):
        sample_payload = {
            'token': self.test_verification_token,
            'payload': '{"type": "event", "text": "Hello, Slack!"}'
        }
        response = self.app_client.post('/slack/events', data=sample_payload)
        self.assertEqual(response.status_code, 200)

    def test_process_slack_event(self):
        sample_payload = '{"type": "event", "text": "Hello, Slack!"}'
        self.slack_app.process_slack_event(sample_payload)
if __name__ == '__main__':
    unittest.main()
