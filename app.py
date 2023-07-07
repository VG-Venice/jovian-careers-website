from flask import Flask, render_template, jsonify
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

load_dotenv()

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Francisco, USA',
  'salary': '$150,000'
}]

dbUser = os.environ['DBUSERNAME'].strip()
dbPwd = os.environ['PASSWORD'].strip()
dbHost = os.environ['HOST'].strip()
dbName = os.environ['DATABASE'].strip()

dbConnectionStr = f"mysql+pymysql://{dbUser}:{dbPwd}@{dbHost}/{dbName}?ssl_ca=cacert.pem"

app.config['SQLALCHEMY_DATABASE_URI'] = dbConnectionStr
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(dbConnectionStr)


@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
