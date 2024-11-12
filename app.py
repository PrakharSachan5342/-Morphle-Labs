from flask import Flask
import subprocess
import datetime
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Prakhar Sachan"  
    username = os.getenv("USER", "default_user")  # Use an environment variable for username
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.getoutput("top -b -n 1")  # This should work, but if not, replace with a simpler command

    response = f"""
    Name: {name}<br>
    User: {username}<br>
    Server Time (IST): {server_time}<br>
    <pre>TOP output:\n{top_output}</pre>
    """
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
