from flask import Flask,request,g
#from flask_apscheduler import APScheduler
from flask_socketio import SocketIO,emit
#import sqlite3
import json
#from flask_mongoengine import MongoEngine

app = Flask(__name__)
#scheduler = APScheduler()
app.config['SECRET_KEY'] = '_madam_'
socketio = SocketIO(app)



    

@app.route('/pair', methods=['POST'])
def rider():
    data = request.json
    x = json.loads(data)
    #riders.append(x)
    #return data
    communicate(x)
    return data



@socketio.on('message')
def communicate(d):
	data = [d['rider'], d['driver'], d['fare']]
    
	socketio.emit('message', data, namespace='/communication')


        #drivers.remove(driverr)
        #riders.remove(rider)



if __name__ == '__main__':
    #scheduler.add_job(id='Schedule task', func=match_rider_driver, trigger = 'interval', seconds = 5)
    #scheduler.start()
    #app.run()
    socketio.run(app,port=6000)






'''
@socketio.on('message' , namespace='/communication')
def handle_message(data):
    print('received fare : ' + str(data) + ' Taka')'''
