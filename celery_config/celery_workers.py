import os

from celery import Celery
import time

def make_celery(app):
    celery = Celery(
        app,
        backend= 'amqp://localhost:5672',
        broker= 'amqp://localhost:5672',

        # backend=os.environ.get('CELERY_BACKEND'),
        # broker=os.environ.get('CELERY_BROKER'),
        include=['celery_config.celery_workers' ]
    )
    return celery


celeryapp = make_celery(__name__)
# celeryapp.autodiscover_tasks(force=True)
print(celeryapp.tasks)
@celeryapp.task(name="task1")
def hello_world(date):
    time.sleep(5)
    print(date)

