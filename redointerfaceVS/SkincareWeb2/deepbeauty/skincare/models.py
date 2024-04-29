from django.db import models

# Create your models here.
class Item(models.Model):
    SKIN_TYPE_CHOICES = (
        ('Dry', 'Dry'),
        ('Normal', 'Normal'),
        ('Oily', 'Oily'),
    )

    EXPERIENCE_CHOICES = (
        ('Beginner', 'Beginner'),
        ('Some Knowledge', 'Some Knowledge'),
        ('Advanced', 'Advanced'),
    )

    TIME_CHOICES = (
        ('10-15 minutes', '10 - 15 minutes'),
        ('20-35 minutes', '20 - 35 minutes'),
        ('Over 35 minutes', 'Over 35 minutes'),
    )

    MORNING_STEPS = {
        '10-15 minutes': ['Cleanser', 'Toner', 'Moisturizer', 'Sunscreen'],
        '20-35 minutes': ['Cleanser', 'Toner', 'Serum', 'Moisturizer', 'Sunscreen'],
        'Over 35 minutes': [ 'Mask','Cleanser', 'Toner', 'Serum', 'Moisturizer', 'Sunscreen']
    }

    NIGHT_STEPS = {
        '10-15 minutes': ['Cleanser', 'Toner', 'Eye cream', 'Moisturizer'],
        '20-35 minutes': ['Cleanser', 'Toner', 'Serum', 'Eye cream', 'Moisturizer'],
        'Over 35 minutes': ['Cleanser', 'Exfoliant', 'Toner', 'Serum', 'Eye cream', 'Moisturizer']
    }
    
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_prodtype = models.CharField(max_length=200)
    item_skintype = models.CharField(max_length=200)
    item_ingre = models.CharField(max_length=1000)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://i.postimg.cc/Y0tXM2bT/default-product-image.pngk")
    item_img = models.ImageField(upload_to='Images/', default="Images/None/Noimg.jpg")

class Post(models.Model):
    names = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering =('-created_at',)

    def __str__(self):
        return self.content

class Reply(models.Model):
    post = models.ForeignKey(Post, related_name='replies', on_delete=models.CASCADE)
    parent_reply = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.content
