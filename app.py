from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Secret key'
# db = SQLAlchemy(app)

@app.route('/')
def Index():
   return render_template("index.html")

if __name__ == "__main__":
   app.run(debug=True)