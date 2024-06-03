from flask import Blueprint, request, abort
from redis_config import redis_db  # Importing redis_db from your Redis configuration file

icmp_app = Blueprint('icmp_app', __name__)

# Middleware to block ICMP Ping Requests
@icmp_app.before_request
def block_ping_requests():
    if request.method == 'GET' and request.args.get('icmp') == 'ping':
        ip_address = request.remote_addr
        if is_blocked(ip_address):
            abort(403)  # Forbidden

# Function to check if an IP address is blocked
def is_blocked(ip_address):
   try:
        return redis_db.exists(ip_address)
   except Exception as e:
        # Handle any potential errors, such as Redis connection issues
        print(f"Error checking blocked IP: {e}")
        return False



# Middleware to block ICMP Ping Requests

# Function to block an IP address
def block_ip_address(ip_address):
     try:
        redis_db.set(ip_address, 1)
     except Exception as e:
        # Handle any potential errors, such as Redis connection issues
        print(f"Error blocking IP address: {e}")



# Function to unblock an IP address
def unblock_ip_address(ip_address):
     try:
        redis_db.delete(ip_address)
     except Exception as e:
        # Handle any potential errors, such as Redis connection issues
        print(f"Error unblocking IP address: {e}")


# Testing blocking and unblocking
if __name__ == "__main__":
    # Replace these IP addresses with the ones you want to test
    ip_to_block = "192.168.1.100"
    ip_to_unblock = "192.168.1.101"

    # Block an IP address
    redis_db.set(ip_to_block, 1)

    # Unblock the IP address
    redis_db.delete(ip_to_block)

    # Block another IP address
    redis_db.set(ip_to_unblock, 1)

    # Unblock the second IP address
   # redis_db.delete(ip_to_unblock)


