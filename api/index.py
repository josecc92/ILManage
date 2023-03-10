from flask import Flask, request, abort, render_template
import sqlite3
import os

app = Flask(__name__)
app.config['DEBUG'] = True

TEMPLATE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'template'))
SERVER_DIR = os.path.abspath(os.path.dirname(__file__))
app.template_folder = TEMPLATE_DIR

# domain root
@app.route('/')
def home():
    return '20230313 1119'

@app.route("/qrScan")
def qrScan():
    try:
        return render_template('qrScan.html')
    except Exception as e:
        return f"發生錯誤: {str(e)}, path:{app.template_folder}"
    return current_path

@app.route("db/CreateDb")
def createDb():
    return

if __name__ == "__main__":
    app.run()
