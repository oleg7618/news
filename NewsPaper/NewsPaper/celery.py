import os
from celery import Celery
from celery.schedules import crontab
from celery import shared_task
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPapper.settings')

app = Celery('NewsPapper')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'email_every_monday_8am': {
        'task': 'NewsPaper.tasks.send_posts_to_email_weekly',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        # 'args': (agrs),
    },
    # TEST TASK FOR DEBUG
    # 'test_task': {
    #     'task': 'NewsPaper.tasks.test_task',
    #     'schedule': 5,
    # }
}

app.autodiscover_tasks()
