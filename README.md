# ride_sharing_app step 4

--- Geo distribute of server ---

Prerequisites- 

-- Nginx

-- MongoDb

-- Docker 

-- python3


1. Edit /etc/hosts

  -> create fake dns for dhaka server and chittagong server and also for communication servers
  
2. Containerize
  
  -> from docker-compose.yml file's path run-> sudo docker build
  
  -> then, sudo docker-compose up
  
3. Run Client

  Prerequisites - socketio, requests
  
  -> sudo pip install python-socketio
  
  -> sudo pip install requests
  
  Create virtual environment if not present
  
  -> python3 -m venv env
  
  Activate virtual environment
  
  -> . env/bin/activate
  
  Now run client-dhaka
  
  -> python3 client.py
  
  and finally run client-chittagong
  
  -> python3 client-chittagong.py
  
  
  
Details about step 4 is available at - https://rafed.github.io/courses/distributed-systems/lab/microservices/#step-4-geo-distribute-the-app
