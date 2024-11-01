from django import forms
from .task import send_feedback_email_task

class ReviewForm(forms.Form):
    name=forms.CharField(
        label="FirstName", min_length=10,max_length=30,widget=forms.TextInput(
            attrs={"class": "h2 form-control mb-3",'placeholder':"Firstname","id":"form-firstname"}))
        
    
    email=forms.EmailField(
        label="Email", max_length=200,widget=forms.TextInput(
            attrs={"class": "form-control mb-3",'placeholder':"E-mail","id":"form-email"}))
        
    
    reviews=forms.CharField(
        label="Review", widget=forms.Textarea(
            attrs={"class": "form-control ",'rows':"5"}))


    #This is a task message created to send to Celery, where Celery will complete the email task explained in that message task, and the delay method is used to send the task message asynchronously, which will then be executed by Celery and the result will be sent back to Django or the client.    
    def send_email(self):
        send_feedback_email_task.delay(
            self.cleaned_data["name"],self.cleaned_data["email"],self.cleaned_data["reviews"]
        )