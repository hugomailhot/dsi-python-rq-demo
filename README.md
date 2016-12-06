# How to make this work

## On the master server

1. Install redis-server if you don't have it already:
   `sudo apt-get install redis-server`
2. Ensure that redis-server is running:
   `start service redis-server`
3. Execute the script that generates and enqueues jobs
   `python3 enqueue_jobs.py`

## On the worker server
Start a worker, and ensure it listens to the Redis queue on the master server by using the configuration file:  
`rq worker -c worker_conf.py`

#### worker_conf.py
This file must contain the following line:  
`REDIS_URL = 'redis://<master server ip>:<redis listening port>'`
The default listening port for Redis is 6379, so most often to connect to a server with IP 123.123.123.1 you would have:  
`REDIS_URL = 'redis://123.123.123.1:6379'`

