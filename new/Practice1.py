from flask import Flask
app = Flask(__name__)
@app.route('/')
def Look_what_I_just_made():
    return 'Look what I just made'