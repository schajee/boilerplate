import time
from celery import shared_task
import channels.layers
from app.models import Task
from asgiref.sync import async_to_sync


@shared_task
def execute(task_id):
    channel_layer = channels.layers.get_channel_layer()
    task = Task.objects.get(pk=task_id)
    for i in range(10):
        time.sleep(1)
    task.done = True
    task.save()
    async_to_sync(channel_layer.group_send)(f'notify_{task.user.username}', {
        'type': 'message', 'value': f'Task executed'})
