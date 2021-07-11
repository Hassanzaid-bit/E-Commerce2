from celery.decorators import task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from .models import Order

logger = get_task_logger(__name__)



@task(name="Send order created email")
def order_created(order_id):
    logger.info("Sent feedback email")
    """
    Task to send an e-mail notification when an order is successfully created
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order no. {order_id}'
    message = f'Dear {order.first_name}, \n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message, 
                          'hzaid.hz@gmail.com',
                          [order.email])
    logger.info("Sent feedback email")

    return mail_sent