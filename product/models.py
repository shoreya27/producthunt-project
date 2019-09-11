from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#product class

class Product(models.Model):
    #title
    title=models.CharField(max_length=20)
    #url
    url=models.URLField(max_length=20)
    #pub date
    publish_date=models.DateField()
    #votes_total
    votes_total=models.IntegerField(default=1)
    #image
    image=models.ImageField()
    #icon
    icon=models.ImageField(height_field=10,width_field=10)
    #body
    body=models.CharField(max_length=200)
    #hunter
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.publish_date.strftime('%b %e %Y')
