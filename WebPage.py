from flask import Flask, render_template, session, request
from flask import session
from MSSentiment import *
from TwilioAPI import *
from twilio.twiml.messaging_response import MessagingResponse
from MongoConnection import *
import os

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27daasf27567d441f2b6176a'

os.environ['u_id'] = 'admin'


@app.route('/')
@app.route('/index')
def index():
    if 'name' in session:
        data = []
        data.insert(0, session['name'])
        # os.environ['u_id'] = u_id
        # return render_template('dashboard.html', result=session['name'])
        return render_template('dashboard.html', result=data)
    return render_template('login.html')


@app.route('/log_out', methods=['GET', 'POST'])
def log_oout():
    #os.environ['u_id'] = 'admin'
    session['name'] = ""
    session.pop('name', None)
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # global u_id
    user_id = request.values.get('user_id', None)
    os.environ['u_id'] = request.values.get('user_id', None)
    password = request.values.get('password', None)
    answer_list = verify_user(user_id, password)

    def_messages = get_message_template(user_id)
    data = []
    first = "value=\'"+def_messages[0].strip()+"'"

    pos = "value=\'"+def_messages[1].strip()+"'"
    neg = "value=\'"+def_messages[2].strip()+"'"
    data.insert(1, first)
    data.insert(2, pos)
    data.insert(3, neg)

    if answer_list[0]:
        session['name'] = answer_list[1]
        data.insert(0, session['name'])
        # os.environ['u_id'] = u_id
        # return render_template('dashboard.html', result=session['name'])
        return render_template('dashboard.html', result=data)
    else:
        return render_template('login.html', result="Login Attempt Failed")


@app.route('/register', methods=['GET', 'POST'])
def register():
    name = request.values.get('name', None)
    u_id = request.values.get('user_id', None)
    phone = request.values.get('phone', None)
    password = request.values.get('password', None)
    insert_user(u_id, name, password, phone)
    return render_template('login.html')


@app.route('/respond', methods=['GET', 'POST'])
def send_response():
    # global u_id
    # text_sentiment = 0.0

    body = request.values.get('Body', None)
    cust_number = request.values.get('From', None)

    # get customer product
    product = get_customer_product(cust_number)

    # get positive and negative message
    # messages = get_message_template(os.environ['u_id'])
    # messages = get_message_template("admin")
    name = "admin"
    if 'name' in session:
        name = session["name"]
    print ("name: " + name)
    # messages = get_message_template(name)
    messages = get_message_templateC(cust_number)
    positive = messages[1].replace("<productType>", product)

    negative = messages[2].replace("<productType>", product)
    resp = MessagingResponse()

    # From MSSentiment
    text_sentiment = sentiment(body)
    print text_sentiment

    if text_sentiment >= 0.5:
        resp.message(positive)
    else:
        resp.message(negative)

    return str(resp)


@app.route('/send', methods=['GET', 'POST'])
def send():
    # if request.args.get('name', None) and request.args.get('cust_number', None):
    cust_name = request.values.get('name', None)
    type = request.values.get('type', None)
    cust_number = request.values.get('cust_number', None)
    first_message = request.values.get('first_message', None)
    positive = request.values.get('positive', None)
    negative = request.values.get('negative', None)
    # add customer to db
    insert_customer(cust_name, cust_number, type)

    # message template to db
    insert_messageTemplateC(cust_number, first_message, positive, negative)

    # def_messages = get_message_template(os.environ['u_id'])
    data = []
    data.insert(0, session['name'])
    data.insert(1, first_message)
    data.insert(2, positive)
    data.insert(3, negative)

    first_message = first_message.replace("<firstName>", cust_name)
    text = first_message.replace("<productType>", type)
    # text = cust_name + type + first_message
    send_message(str(text), cust_number)
    return render_template('dashboard.html', result=data)


if __name__ == "__main__":
    app.run()
