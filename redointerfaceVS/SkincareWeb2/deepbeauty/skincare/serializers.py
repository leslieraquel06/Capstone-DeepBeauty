from rest_framework import serializers
from .models import Item, Post

class ItemSerializer(serializers.ModelSerializer):
    # Assuming 'item_img' is the correct field name
    item_img = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'item_desc', 'item_prodtype', 'item_skintype', 'item_ingre', 'item_price', 'item_image', 'item_img']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'names', 'content', 'created_at']
