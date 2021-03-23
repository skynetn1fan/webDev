from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('./index.html')

@app.route("/blog")
def blog():
  return "These are my thoughts on blogs!"

@app.route("/blog/2020/CV")
def blog2():
  return "These are my computer vision apps!"

# endpoint if we should need it
@app.route('/flavicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'flavicon.ico')

if __name__ == "__main__":
  app.run()
