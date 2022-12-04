# import os
# from celery import Celery
# from celery.schedules import crontab
#
#
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')
#
# app = Celery('NewsPortal')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
# app.conf.beat_schedule = {
#     'action_every_week': {
#         'task': 'news.tasks.add',
#         'schedule': 10,
#
#     },
# }
# app.conf.beat_schedule = {
#     'action_every_week': {
#         'task': 'action',
#         'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
#         # 'args': (agrs),
#     },
# }
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')

app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'when_creating_post': {
        'task': 'news.tasks.notify_about_new_post',
        'schedule': 30,
        'args': ("some_arg"),
    },
}
#  каждый понедельник в 8
# app.conf.beat_schedule = {
#     'when_week': {
#         'task': 'news.tasks.notify_weekly',
#         'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
#         # 'args': (agrs),
#     },
# }
app.conf.beat_schedule = {
    'when_week': {
        'task': 'news.tasks.notify_weekly',
        'schedule': 30,
        # 'args': ("some_arg"),
    },
}