from flask import Flask, jsonify
import os

app = Flask(__name__)

# Simulate a microservice endpoint
@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        "service": "ArmorByte Core API",
        "status": "Operational",
        "security_level": "Enforced"
    })

if __name__ == '__main__':
    # Running on 0.0.0.0 for Docker containerization
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) # nosec B104
