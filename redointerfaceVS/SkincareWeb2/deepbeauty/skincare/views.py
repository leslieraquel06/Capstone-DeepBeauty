from django import forms
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render
from .models import Item, Reply
from django.template import loader
from rest_framework import viewsets, generics
from .serializers import ItemSerializer, PostSerializer
from django.core.paginator import Paginator
from .models import Post, Reply
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

def quiz(request):
    return render(request, 'home/quiz.html')


def community(request):
    posts = Post.objects.order_by('-created_at')  # Order by created_at in descending order
    paginator = Paginator(posts, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj,
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

def save_reply(request):
    print("Request received:", request.POST)  # Print the received POST data
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            post_id = request.POST.get('post_id')
            content = request.POST.get('content')
            post = Post.objects.get(pk=post_id)
            reply = Reply(post=post, content=content)
            reply.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Bad request'})
                            
def detail (request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request, 'home/detail.html', context)

def quiz(request):
    experience_choices = Item.EXPERIENCE_CHOICES
    time_choices = Item.TIME_CHOICES
    skin_type_choices = Item.SKIN_TYPE_CHOICES
    
    context = {
        'experience_choices': experience_choices,
        'time_choices': time_choices,
        'skin_type_choices': skin_type_choices,
    }
    return render(request, 'home/quiz.html', context)

def quiz_results(request):
    if request.method == 'POST':
        experience = request.POST.get('experience')
        time = request.POST.get('time')
        skin_type = request.POST.get('skintype')

        # Fetching the morning and night routine steps based on the selected time
        morning_steps = Item.MORNING_STEPS.get(time, [])
        night_steps = Item.NIGHT_STEPS.get(time, [])

        # Fetching products based on the selected skin type and morning/night steps
        morning_products = Item.objects.filter(item_skintype=skin_type, item_prodtype='Moisturizer', item_name__in=morning_steps)
        night_products = Item.objects.filter(item_skintype=skin_type, item_prodtype='Moisturizer', item_name__in=night_steps)

        # Passing data to the template
        context = {
            'experience': experience,
            'time': time,
            'skin_type': skin_type,
            'morning_steps': morning_steps,
            'night_steps': night_steps,
            'morning_products': morning_products,
            'night_products': night_products,
        }

        return render(request, 'home/quiz_results.html', context)

    return render(request, 'home/quiz_results.html')