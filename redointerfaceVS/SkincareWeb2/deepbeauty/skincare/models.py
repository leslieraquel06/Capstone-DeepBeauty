from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_prodtype = models.CharField(max_length=200)
    item_skintype = models.CharField(max_length=200)
    item_ingre = models.CharField(max_length=1000)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://i.postimg.cc/Y0tXM2bT/default-product-image.pngk")
    item_img = models.ImageField(upload_to='Images/',default="Images/None/Noimg.jpg")

class Post(models.Model):
    names = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering =('-created_at',)

    def __str__(self):
        return self.content