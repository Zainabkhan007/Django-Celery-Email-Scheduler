from  django.template import Context
from  django.template.loader import render_to_string
from  django.core.mail import EmailMessage
from django.conf import settings

def send_email_review(name,email,reviews):
    #here context is a dictionary which have variables
    context={
        "name":name,
        "email":email,
        "reviews":reviews
    }

    email_subject="Thanks for the review"
    email_body=render_to_string("email_message.txt",context)

    email=EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL,[email, ],
    )
    return email.send(fail_silently=False) #error configuration