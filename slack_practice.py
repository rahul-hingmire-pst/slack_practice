from flask import Flask, request, jsonify

class SlackApp:
    def __init__(self, verification_token, port=3000):
        self.app = Flask(__name__)
        self.verification_token = verification_token

        @self.app.route('/slack/events', methods=['POST'])
        def slack_events():
            try:
                if request.form.get('token') != self.verification_token:
                    return jsonify({'error': 'Invalid verification token'}), 403

                slack_event = request.form.get('payload')
                if not slack_event:
                    return jsonify({'error': 'Invalid request'}), 400
                self.process_slack_event(slack_event)

                return jsonify({'success': True}), 200
            except Exception as e:
                print(f"Error processing Slack event: {e}")
                return jsonify({'error': 'Internal Server Error'}), 500
                self.port = port
                

    def run(self):
        self.app.run(port=self.port)

    def process_slack_event(self, slack_event):
        print("Received Slack Event:", slack_event)

if __name__ == '__main__':
    slack_app = SlackApp(verification_token='YOUR_VERIFICATION_TOKEN', port=3000)
    slack_app.run()
    
