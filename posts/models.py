from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=120)
    #author = models.ForeignKey(User,name='posts')
    content = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
        
    class Meta:
    	ordering = ('created_date',)

    

