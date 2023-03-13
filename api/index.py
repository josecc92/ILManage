from flask import Flask, request, abort, render_template
import sqlite3
import os

app = Flask(__name__)
app.config['DEBUG'] = True

TEMPLATE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'template'))
SERVER_DIR = os.path.abspath(os.path.dirname(__file__))
app.template_folder = TEMPLATE_DIR

@app.before_first_request
def create_database():
    try:
        # 檢查資料庫檔案是否已存在
        if not os.path.exists(f'{SERVER_DIR}/data/database.db'):
            # 建立資料庫
            conn = sqlite3.connect(f'{SERVER_DIR}/data/database.db')
            # 在資料庫中創建表格
            c = conn.cursor()
            c.execute('''CREATE TABLE users
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          email TEXT NOT NULL,
                          age INTEGER NOT NULL)''')
            # 關閉資料庫連接
            conn.close()
    except Exception as e:
        return f"發生錯誤: {str(e)}"
    return 

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
