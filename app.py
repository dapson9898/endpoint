from flask import Flask, jsonify, request

from datetime import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def endpoint():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    
    #implement the logic for getting the curren week day & utc time
    current_day = datetime.now().strftime('%A')
    utc_time =  datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ') 

    return jsonify ({
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/dapson9898/endpoint/blob/main/app.py",
        "github_repo_url": "https://github.com/dapson9898/endpoint",
        "status_code": 200
     })

if __name__ == 'main':
    app.run()


# E.g.: http://example.com/api?slack_name=example_name&track=backend.                