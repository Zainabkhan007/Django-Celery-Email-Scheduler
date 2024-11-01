#  So, here we define a task for Celery to run.

from celery import shared_task
from .email import send_email_review
from celery.utils.log import get_task_logger

logger=get_task_logger(__name__)

@shared_task(name="send_feedback_email_task")
def send_feedback_email_task(name,email,reviews):
    logger.info("Send review email ")
    return send_email_review(name,email, reviews)
