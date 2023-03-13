from flask import Flask, request, abort, render_template

import os

app = Flask(__name__)
app.config['DEBUG'] = True

# domain root
@app.route('/')
def home():
    return 'Hello, World!0418'

@app.route("/qrScan")
def qrScan():
    try:
        return render_template("/api/template/qrScan.html")
    except Exception as e:
        return f"發生錯誤: {str(e)}"
    return

if __name__ == "__main__":
    app.run()
