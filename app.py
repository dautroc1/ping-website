from flask import Flask
import requests

app = Flask(__name__)

# Endpoint that will trigger the website ping
@app.route('/ping-website', methods=['GET'])
def ping_website():
    try:
        # Send a GET request to the website
        response = requests.get('https://ncomic.io.vn/')
        if response.status_code == 200:
            return "Website pinged successfully", 200
        else:
            return "Failed to ping website", 500
    except Exception as e:
        return f"Error: {str(e)}", 500
@app.route('/ping-api', methods=['GET'])
def ping_api():
    try:
        # Send a GET request to the website
        response = requests.get('https://test-gpt-y58q.onrender.com')
        return "Website pinged successfully", 200
        
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
