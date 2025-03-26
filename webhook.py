from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "my_secret_token"  # Change this to your secret token

@app.route("/webhook", methods=["GET"])
def verify():
    """Verification endpoint for Meta Webhooks."""
    token_sent = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    
    if token_sent == VERIFY_TOKEN:
        return challenge  # Meta requires this response to verify the webhook
    return "Invalid token", 403

if __name__ == "__main__":
    app.run(port=5000)
