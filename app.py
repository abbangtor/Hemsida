from flask import Flask, request, render_template
from ICMPMiddleware import icmp_app
from authenticateUsers import authenticate_user

app = Flask(__name__)

# Importing ICMPMiddleware app
app.register_blueprint(icmp_app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    return "Login successful"
    

# Run the Flask app
app.run(debug=True)