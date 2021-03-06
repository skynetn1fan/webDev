from flask import Flask, render_template, send_from_directory, request, redirect
from flask_mail import Mail, Message
import os
import secrets
import csv


app = Flask(__name__)
app.config.from_object('config.Config')
mail = Mail(app)

@app.route("/")
def myhome():
  return render_template('./index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
  return render_template(page_name)

# endpoint if we should need it
@app.route('/static/assets/flavicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/assets'),
                               'flavicon.ico')

def write_to_file(data):
    with open('database.txt', mode='a') as f:
        email = data['email']
        subject = data['subject']
        message = data['message']
        f.write(f'\n {email}, {subject}, {message}')


def write_to_db(data):
    with open('database.csv', mode='a', newline='') as f:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(f, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_db(data)
            msg = Message('CONTACT FROM WEBSITE ',
                          recipients=["hanot.jonas@gmail.com"])
            msg.body = data['message']
            mail.send(msg)
            return redirect('thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong with your message, please try again.'



if __name__ == "__main__":
  app.run()
