from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis_container', port = 6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'hello, scut. I have been accessed by %s times' % redis.get('hits') 

if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug = True)
    app.run(host='0.0.0.0', port = 8081)


