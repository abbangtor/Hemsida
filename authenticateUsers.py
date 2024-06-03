import bcrypt
from redis_config import redis_db  # Importing redis_db from your Redis configuration file

# Function to authenticate users
def authenticate_user(username, password):
    stored_password_hash = redis_db.hget('users', username)
    if stored_password_hash:
        stored_password_hash = stored_password_hash.decode('utf-8')
        # Check if the provided password matches the stored hash
        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
            return True
    return False




""" import redis
import bcrypt

# Initialize Redis connection
redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)


# Function to authenticate users
def authenticate_user(username, password):
    # Retrieve all user-password pairs from Redis
    users = redis_db.hgetall('users')
    
    # Loop through each user-password pair
    for stored_username, stored_password in users.items():
        # Decode stored password from bytes to string
        stored_password = stored_password.decode('utf-8')
        
        # Check if the provided username matches any stored username
        if username == stored_username.decode('utf-8'):
            # Compare the provided password with the stored hash
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                return True
    return False
 """