from django.shortcuts import redirect, render, get_object_or_404
from .forms import Postform, Commentform, FreePostForm, FreeCommentForm
from .models import Post, FreePost

def home(request):
    posts = Post.objects.filter().order_by('-date') # Post의 객체들을 date순으로 다 가져옴
    return render(request, 'index.html', {'posts': posts})

def postcreate(request):
    # request method가 POST일 경우 입력값 저장하고, GET 일 경우 form 입력 html 띄우기
    if request.method == 'POST' or request.method == 'FILES':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Postform()
    return render(request, 'post_form.html', {'form': form})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id) # Post 객체를 들고 올건데, Primary Key로 post_id를 이용하여 가져올거임
    comment_form = Commentform()
    return render(request, 'detail.html', {'post_detail': post_detail, 'comment_form': comment_form})

# 댓글 저장하는 기능
def new_comment(request, post_id):
    filled_form = Commentform(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False) # Foreign key 연결된 경우 commit = False
        finished_form.post = get_object_or_404(Post, pk = post_id) # 어느 게시글에 해당되는 정보인지 꼭 담아줘야됨.
        filled_form.save()
    return redirect('detail', post_id)

def freehome(request):
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'free_index.html', {'freeposts': freeposts})


def freepostcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user # User 객체를 author column에 담아주어야 함.
            unfinished.save()
            return redirect('freehome')
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form})


def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form': comment_form})


def new_freecomment(request, post_id):
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)