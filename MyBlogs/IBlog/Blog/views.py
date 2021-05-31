from django.shortcuts import render
from Blog.models import Post
from  Blog.models import Category
# Create your views here.



def home(request):
    #load aal the post from the db
    posts = Post.objects.all()
    print(posts)

    cats = Category.objects.all()
    data = {
        'posts':posts,
         'cats':cats

    }
    return render(request,'home.html',data)


def post(request,url):
    post = Post.objects.get(url = url)
    cats = Category.objects.all()
    return render(request,'post.html',{'post':post,'cats':cats})


def category(request,url):
    cat= Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request,'category.html',{'cat':cat,'posts':posts})
