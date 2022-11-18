#https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application
# https://www.tutorialspoint.com/flask/flask_variable_rules.htm

from nameEntry import nameEntry
from nameMap import nameMap
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross domain requests


@app.route("/name/<name>/<type>")
def main(name,type):
    folder = "namedata/"
    femaleMap=nameMap(folder+'dist.female.first')
    maleMap=nameMap(folder+'dist.male.first')
    lastMap=nameMap(folder+'dist.all.last')

    if type=="Female":
      data=femaleMap.lookup10(name)
    elif type=="Male":
      data=maleMap.lookup10(name)
    else:
      data=lastMap.lookup10(name)
    #print(data)
    return data

@app.route("/name")
def about():
  return "namelookup/name/type"
