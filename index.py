from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return """<h2>Flask deployed through Vercel</h2>"""
