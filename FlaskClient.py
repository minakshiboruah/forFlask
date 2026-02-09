from flask import Flask, request,jsonify
import requests
app = Flask(__name__)
@app.route('/weather')
def get_weather():
 # Mumbai Coordinates (Same as IMD ID 43003)
 lat = 19.07
 lon = 72.87
 app.json.ensure_ascii = False
 headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
 url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&timezone=Asia%2FKolkata"
# Flask acts as a CLIENT here
#  response = requests.get("https://api.weatherapi.com/v1/current.json?q=London")
 response = requests.get(url, headers=headers, timeout=10)
 data = response.json()
        
 # 3. Use jsonify to send it back to YOUR client correctly
 return (data)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    # You MUST use 0.0.0.0 to be "visible" to the internet
    app.run(host='0.0.0.0', port=port)
