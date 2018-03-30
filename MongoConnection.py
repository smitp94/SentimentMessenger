from pymongo import MongoClient


def setConn():
    client = MongoClient('mongodb://smitp:123456@ds223609.mlab.com:23609/sentimentmessengerdb')
    db = client['sentimentmessengerdb']
    return db


def insert_user(id, name, password, number):
    db = setConn()

    #Collection = Tables
    #Documents = rows

    user = db.User
    post_user = {
        'id': id,
        'name': name,
        'password': password,
        'number': number
    }
    result = user.insert_one(post_user)
    print('One post: {0}'.format(result.inserted_id))


def verify_user(u_id, password):
    db = setConn()

    user = db.User
    user_details = user.find_one({'id': u_id})
    pswd = user_details['password']

    if pswd == password:
        return [True, user_details['name']]
    else:
        return [False, "NULL"]


def insert_customer(name, number, product):
    db = setConn()

    customer = db.Customer
    post_customer = {
        'name': name,
        'number': number,
        'product': product
    }
    # result = customer.insert_one(post_customer)

    customer.update({"number": number}, {"$set": post_customer}, upsert=True)
    # print('One post: {0}'.format(result.inserted_id))


def insert_messageTemplate(id, first_message, positive, negative):
    db = setConn()

    message = db.MessageTemplate
    post_message = {
        'id': id,
        'first_message': first_message,
        'positive': positive,
        'negative': negative
    }
    result = message.insert_one(post_message)
    print('One post: {0}'.format(result.inserted_id))


def insert_messageTemplateC(cust_number, first_message, positive, negative):
    db = setConn()

    message = db.MessageTemplate
    post_message = {
        'id': cust_number,
        'first_message': first_message,
        'positive': positive,
        'negative': negative
    }
    # result = message.insert_one(post_message)
    message.update({"id": cust_number}, {"$set": post_message}, upsert=True)
    # print('One post: {0}'.format(result.inserted_id))


def get_customer_product(phone):
    db = setConn()

    customer = db.Customer
    customer_details = customer.find_one({'number': phone})

    return customer_details['product']


def get_message_template(u_id):
    db = setConn()

    message = db.MessageTemplate
    message_details = message.find_one({'id': "admin"})

    return [message_details['first_message'], message_details['positive'], message_details['negative']]


def get_message_templateC(u_id):
    db = setConn()

    message = db.MessageTemplate
    message_details = message.find_one({'id': u_id})

    return [message_details['first_message'], message_details['positive'], message_details['negative']]
