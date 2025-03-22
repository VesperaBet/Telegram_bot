from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Remplace ici par ton token bot et ton chat_id
TOKEN = "TON_TOKEN_BOT_ICI"
CHAT_ID = "-1002553433496"  # Ton chat_id

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route('/send_paris', methods=['POST'])
def send_paris():
    data = request.get_json()
    
    if not data or 'message' not in data:
        return jsonify({"error": "Invalid payload"}), 400

    message = data['message']

    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }

    response = requests.post(TELEGRAM_API_URL, data=payload)

    if response.status_code == 200:
        return jsonify({"status": "Message sent to Telegram"}), 200
    else:
        return jsonify({"error": "Failed to send message"}), 500

@app.route('/', methods=['GET'])
def home():
    return "Bot webhook running!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
