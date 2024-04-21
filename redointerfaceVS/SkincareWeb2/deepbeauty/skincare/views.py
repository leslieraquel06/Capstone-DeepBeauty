from django.shortcuts import redirect, render
from .models import Item
from django.template import loader
from rest_framework import viewsets, generics
from .serializers import ItemSerializer, PostSerializer
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm


    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class MoistViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(item_prodtype='Moisturizer')
    serializer_class = ItemSerializer

class SunViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(item_prodtype='Sunblock')
    serializer_class = ItemSerializer

class ItemSearchAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        item_prodtype = self.request.query_params.get('item_prodtype')
        item_name = self.request.query_params.get('item_name')

        if item_prodtype:
            queryset = queryset.filter(item_prodtype__icontains=item_prodtype)
        if item_name:
            queryset = queryset.filter(item_name__icontains=item_name)

        return queryset 


# Create your views here.
def index(request):
    item_prodtype = request.GET.get('item_prodtype')
    item_name = request.GET.get('item_name')

    item_list = Item.objects.all()

    if item_prodtype:
        item_list = item_list.filter(item_prodtype__icontains=item_prodtype)
    if item_name:
        item_list = item_list.filter(item_name__icontains=item_name)

    paginator = Paginator(item_list, 6)
    page = request.GET.get('page')
    item_list = paginator.get_page(page)

    context = {
        'item_list': item_list,
        'item_prodtype': item_prodtype,
        'item_name': item_name
    }
    return render(request, 'home/product.html', context)

def home(request):
    return render(request, 'home/home.html')

def community(request):
    posts = Post.objects.order_by('-created_at')  # Order by created_at in ascending order
    context = {
        'posts': posts,
        'form': PostForm(),  
    }
    return render(request, 'home/community.html', context)


def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community')  # Redirect back to the community page after saving the post
    else:
        form = PostForm()

    posts = Post.objects.order_by('-created_at')  # Order by created_at in ascending order
    return render(request, 'home/createpost.html', {'posts': posts, 'form': form})

def quiz(request):
    return render(request, 'home/quiz.html')

def detail (request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request, 'home/detail.html', context)