from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    return "Welcome to this webapage!, This webpage has been viewed "+counter+" time(s)"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7000)
