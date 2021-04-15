from flask import Flask,request,g
#from flask_apscheduler import APScheduler
#from flask_socketio import SocketIO,emit
#import sqlite3
import json
from flask_mongoengine import MongoEngine

app = Flask(__name__)
#scheduler = APScheduler()
app.config['SECRET_KEY'] = '_madam_'
#socketio = SocketIO(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'ratings',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)

#riders = []
#drivers = []

class DriverRating(db.Document):
	name = db.StringField()
	rating = db.StringField()

def insertVaribleIntoTable(rating, name):
    #conn = sqlite3.connect('./ratings.db')
    #cursor = conn.cursor()
    #cursor.execute('''INSERT INTO ratings(name, rating) VALUES (?, ?)''', (name, str(rating)))

    #conn.commit()
    DriverRating(name=name, rating=rating).save()
    print("Records inserted........")
    #nam = request.args.get(name)
    #user = DriverRating.objects(name=nam).first()
    #if not user:
    #    print('not found')
    #else:
    #    print(name)
    #cursor.execute('select * from ratings')

    #conn.close()
    
    
@app.route('/rating', methods=['POST'])
def ratings():
    data = request.json
    x = json.loads(data)
    name = x['name']
    rating = str(x['rating'])
    insertVaribleIntoTable(rating, name)
    return data
    

if __name__ == '__main__':
	app.run(debug=True, port=7000)
	
	
'''

sudo rm /var/lib/mongodb/mongod.lock

sudo mongod --repair

sudo service mongodb start

sudo service mongodb status

'''


