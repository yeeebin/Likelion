from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .form import PostForm

def post_list(request): 
    posts = Post.objects.all() #post모델에 대한 쿼리셋 생성
    return render(request, 'blog/post_list.html', {'posts': posts}) #render 함수는 HTML템플릿을 사용하여 HTTP응답 생성

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post}) #pk는 게시물의 기본 키, get_object_or_404()는 객체가 존재하지 않을 때 HTTP 404 오류 페이지 반환

def post_new(request):
    if request.method == 'POST': #요청이 POST메서드로 전송되었는지 확인
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm() #빈 PostForm 생성
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

