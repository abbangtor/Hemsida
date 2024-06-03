import redis
import subprocess
REDIS_HOST = "localhost"
REDIS_PORT = "6379"
REDIS_USERNAME = "UPPqrt"
REDIS_PASSWORD = "avKvjAI8Mxlmew"

#redis_db = None

""" try:
    redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)
    redis_db.auth(REDIS_USERNAME, REDIS_PASSWORD)
    print("Successfully connected to Redis server")
except Exception as e:
    print(f"Error connecting to Redis server: {e}")


 """

# Command to authenticate with redis-cli
auth_command = f"redis-cli -h {REDIS_HOST} -p {REDIS_PORT} -a {REDIS_PASSWORD} auth"

# Run the authentication command using subprocess
try:
    subprocess.run(auth_command, shell=True, check=True)
    print("Authentication successful")
except subprocess.CalledProcessError as e:
    print(f"Error authenticating with Redis: {e}")