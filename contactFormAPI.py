from peewee import *
from flask import Flask
from flask import request
from flask import jsonify
import datetime
from playhouse.shortcuts import model_to_dict, dict_to_model
from flask import render_template

db = PostgresqlDatabase('contactbook', user='tonywu', password='',
                        host='localhost', port=5432)

def Connect():
  db.connect()
  print("Connecting to psql")
  return 0

Connect()

class BaseModel(Model):
  class Meta:
    database = db

class contactForm(BaseModel):
    name = CharField()
    phoneNumber = CharField()
    note = CharField()

db.create_tables([contactForm])
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/contactbook')
def contactbook():
  return jsonify(model_to_dict(contactForm.get()))

@app.route('/contactbook/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':
    if id:
        return jsonify(model_to_dict(contactForm.get(contactForm.id == id)))
    else:
        people_list = []
        for person in contactForm.select():
            people_list.append(model_to_dict(person))
        return jsonify(people_list)



app.run(port=3000, debug=True)

# def inputContactForm(InputtedName, InputtedPhoneNumber, InputtedNote):
#   newContact = contactForm(name = InputtedName, phoneNumber = InputtedPhoneNumber, note = InputtedNote)
#   newContact.save()
#   print("Saving contact to book, returning...")
#   return 0

# status = "running"
# while  status == "running":
#   toEnter = input("Would you like to enter a details to a contact book? (y/n) : ")
#   if toEnter == "n":
#     status = "notRunning"
#     changeStatus = input("To start application, enter any key: ")
#     if len(changeStatus) > 0:
#       status = "running"
#   elif toEnter == "y":
#     name = input("Enter full name: ")
#     phoneNumber = input("Enter person phone number: ")
#     note = input("Enter note about contact person: ")
#     inputContactForm(name,phoneNumber,note)

