from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from models import Post
from forms import BlogPostForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, "blog/home.html")

def post_list(request):
    #GET request checks if there is any additional queries in the string.
    #GET is the HTTP method to access the query.
    #get is the python method to find the dictionary values.
    #'false' here is just the answer to the question in the event that there isn't something to show ie when the question is asked 'is there something here?' , we need an answer, so False is a friendly way to show this
    top = request.GET.get('top', False)
    if top:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:3]
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blog/blogtests.html",{'posts':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "blog/blogdetail.html", {'post': post})

def top_5(request):
    top5 = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:3]
    return render (request, "blog/top5.html", {'top5': top5} )

def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
           # return render (request, "blogtest.html")
            return redirect('blog.views.post_detail', id = post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/blogpostform.html', {'form':form})

def edit_post(request,pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method =="POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, id=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/blogpostform.html',{'form':form})