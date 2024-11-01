from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    image=models.ImageField(upload_to="avatars/",null=True,blank=True)
    displayname=models.CharField(max_length=200,null=True,blank=True)


    def __str__(self):
        return str(self.user)
    
    @property
    def name(self):
        if self.displayname:  #It means that if a display name exists, it will display the display name; otherwise, it will display the username only.
            return self.displayname
        return self.user.username 

    @property
    def image(self):
        if self.image:
            return self.image.url
        else:
            return f"{settings.STATIC_URL}images/avatar.svg"    


class MessageBoard(models.Model):
    subscribers=models.ManyToManyField(User,related_name="messageboard",blank=True)

    def __str__(self):
            return str(self.id)

class Messages(models.Model):
    messageboard=models.ForeignKey(MessageBoard,on_delete=models.CASCADE,related_name="messages")
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="messages")
    body=models.CharField(max_length=2000)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created']


    def __str__(self):
        return str (self.author.username)