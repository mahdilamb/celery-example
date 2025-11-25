"""Module containing celery tasks that are available as a worker"""

import logging
import os
import socket
from celery import Celery

REDIS_ADDR = f"redis://{os.environ['REDIS_HOST']}:{os.environ['REDIS_PORT']}/0"
RABBIT_MQ_ADDR = f"pyamqp://{os.getenv('RABBIT_MQ_USER', 'guest')}:{os.getenv('RABBIT_MQ_PASSWORD', 'guest')}@{os.environ['RABBIT_MQ_HOST']}:{os.environ['RABBIT_MQ_PORT']}//"


def __is_rabbit_mq_running(host: str, port: int):
    """Check whether a port is open."""
    try:
        with socket.create_connection((host, port), timeout=5):
            return True
    except OSError:
        return False


if __is_rabbit_mq_running("localhost", port=5672):
    logging.info("Running with rabbit-mq as broker; redis as backend.")
    app = Celery(__name__, broker=RABBIT_MQ_ADDR, backend=REDIS_ADDR)
else:
    logging.info("Running with redis as backend and broker.")
    app = Celery(__name__, broker=REDIS_ADDR, backend=REDIS_ADDR)


### Worker tasks ###


@app.task
def add(x: int, y: int):
    return x + y
