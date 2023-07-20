from flask import Flask
import requests

app = Flask(__name__)

# Endpoint that will trigger the website ping
@app.route('/ping-website', methods=['POST'])
def ping_website():
    try:
        # Send a GET request to the website
        response = requests.get('http://ncomic.io.vn/')
        if response.status_code == 200:
            return "Website pinged successfully", 200
        else:
            return "Failed to ping website", 500
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)