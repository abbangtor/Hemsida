import bcrypt
from redis_config import redis_db  # Importing redis_db from your Redis configuration file


# Function to store user credentials in Redis
def store_user(username, password):
    # Hash the password before storing
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # Store the hashed password in Redis
    redis_db.hset('users', username, hashed_password)

def create_user():
    print("Enter new username")
    user = input()
    print("Enter new password")
    password = input()

    store_user(user, password)


create_user()