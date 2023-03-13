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

@app.route("/test")
def test():
    return """<!DOCTYPE html>
            <html lang="zh-TW">
            <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1" />
              <title>賴田捕手</title>
            </head>
            <body>
              <h1>賴田捕手第 20 天</h1>
              <p>全身都是肌肉沒半點腦子。反正，那就是鄭尼那晚照顧的草泥馬。我完全無法了解，我發誓我沒辦法。</p>
            </body>
            </html>"""

if __name__ == "__main__":
    app.run()