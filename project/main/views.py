from django.shortcuts import render, redirect
import datetime
from .models import Post, Author, Request
from .forms import AddPost, AddRequest

# Описание вьюшек!
# Create your views here.

# функция render отображает наши темплейты, первым параметром всегда передается request, чтобы он был доступен на разметке, вторым параметром передается название темплейта в кавычках.
# для отображения переменной t на экране, она будет передана в рендер третьим параметром, который называется context.По сути это словарь, значение ключа обязательно должно быть строковым.Context нужен для того чтобы к нему обратиться с разметки/темплейта/хтмл файла.

def test(request):
    t = datetime.date.today()
    return render(request, 'main_page.html', {'current_date':t})

def posts(request):
    posts = Post.objects.all() # переменной posts присвоили значение - все посты в таблице Post.
    return render(request, 'posts.html', {'posts': posts})

def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id) # Получаем объект поста по его id.
    except:
        title = ''
    return render(request, 'post.html', {'post': post})
    
def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            post_entry = Post()
            post_entry.author = Author.objects.all()[0]
            post_entry.issued = datetime.datetime.now()
            post_entry.title = form.cleaned_data['title']
            post_entry.content = form.cleaned_data['content']
            post_entry.image = form.cleaned_data['image']
            
            post_entry.save()
            return redirect('posts')
    else:
        form = AddPost()
    return render(request, 'add_post.html', {'form': form})



def add_request(request):
    if request.method == 'POST':
        form = AddRequest(request.POST, request.FILES)
        if form.is_valid():
            post_entry = Request()
            post_entry.email = form.cleaned_data['email']
            post_entry.name = form.cleaned_data['name']
            post_entry.message = form.cleaned_data['message']
            post_entry.phone_number = form.cleaned_data['phone_number']
            
            post_entry.save()
    else:
        form = AddRequest()
    return render(request, 'response_request.html', {'form': form})