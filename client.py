import requests
import socketio
import time
import random
import json

sio = socketio.Client()
sio.connect('http://localhost:8000',namespaces=['/communication'])


def send_ratings(driver_name):
    ratings_data = random.randrange(1,5)
    rating = {
        'name': driver_name,
        'rating':ratings_data
        
    }
    r = requests.post("http://localhost:8000/rating", json=json.dumps(rating))


@sio.event(namespace='/communication')
def message(data):
    fare = round(data[2],2)
    print(data[0]+ ' is assigned to '+data[1] + '.\n'  +
          ' Total fare '+ str(fare) +' Taka\n')

    #sio.emit('message', data[2], namespace='/communication')
    send_ratings(data[1])



id = 101

while True:
    x1 = random.randrange(4000)
    y1 = random.randrange(4000)
    x2 = random.randrange(4000)
    y2 = random.randrange(4000)

    rider_data = {'name': 'r' + str(id),  # rider id starts with r
                  'location': [x1, y1],
                  'destination': [x2, y2]}
    r = requests.post("http://localhost:8000/rider", json=json.dumps(rider_data))

    x3 = random.randrange(4000)
    y3 = random.randrange(4000)
    carnum = random.randrange(15600000)

    driver_data = {'name': 'd' + str(id),  # driver id starts with d
                   'car_number': carnum,
                   'location': [x3, y3]}
    r = requests.post("http://localhost:8000/driver", json=json.dumps(driver_data))

    time.sleep(1)
    id += 1



