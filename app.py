import os
from flask import Flask

app = Flask(__name__)

# Define a route that uses environment variables
@app.route('/env_variables')
def env_variables():
    # Get the public environment variable
    public_variable = os.environ.get('PUBLIC_VARIABLE', 'Public variable not set')
    
    # Get the secret environment variable
    secret_variable = os.environ.get('SECRET_VARIABLE', 'Secret variable not set')
    
    # Return the values of the environment variables
    return f"Public variable: {public_variable}\nSecret variable: {secret_variable}"

# Define the existing route
@app.route('/')
def hello():
    return "Hello from our Kubernetes demo app with Flask!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
