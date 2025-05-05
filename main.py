from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import smtplib
import datetime as dt
from twilio.rest import Client

import os

email = "jkbakerygoods@gmail.com"
email_pw = os.environ.get('EMAIL_PW')
phone = os.environ.get('PHONE')
acct_sid = os.environ.get('ACCT_SID')
auth_token = os.environ.get('AUTH_TOKEN')

app = Flask(__name__)
Bootstrap5(app)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == 'POST':
        data = request.form
        now = dt.datetime.now()
        print(now)
        print(data['name'])
        print(data['email'])
        print(data['subject'])
        print(data['message'])
        # client = Client(acct_sid, auth_token)
        # message = client.messages.create(
        #     body=f"Message from JK Bakery website.\n\n{data['subject']} from {data['name']}\n{data['email']}\n{data['message']}",
        #     from_=twilio_phone,
        #     to=phone,
        # )
        # print(message.status)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=email_pw)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"Subject:{data['subject']}\n\nFrom - {data['name']} - {data['email']},\n\n{data['message']}"
            )
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)