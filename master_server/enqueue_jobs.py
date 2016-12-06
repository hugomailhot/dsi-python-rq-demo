# !/usr/bin/env python
# encoding: utf-8

from redis import Redis
from rq import Queue
from toy_example_module import wait_and_square
import random


# This creates a queue in the local Redis database
# with default port and no password
q = Queue(connection=Redis())


# This loop keeps the total job enqueued at 10
while True:
    if len(q) < 10:
        job = q.enqueue(wait_and_square, random.randint(0, 1000))

        # job.result will contain the result after the remote worker
        # is done executing it. Here we don't use it.
