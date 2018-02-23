from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post, Comment, Tag
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from django.views import generic


def post_list(request):
    posts = Post.objects.all().order_by('-pk')
    paginator = Paginator(posts, 15)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out o frange (9999), deliver last page of results
        posts = paginator.page(paginator.num_pages)

    ctx = {
        'posts': posts,
    }

    return render(request, 'post/post_list.html', ctx)


@login_required
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comment_form = CommentForm(request.POST or None)
    ctx = {
        'post': post,
        'comment_form': comment_form,
    }

    return render(request, 'post/post_detail.html', ctx)


@csrf_exempt
def comment_create(request, pk):
    if request.POST:
        post = Post.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return render(request, 'post/comment.html', {
                'comment': comment,
            })

    return HttpResponse(status=405)


def post_write(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        p = Post.objects.get(pk=post.pk)
        t_lists = post.hashtag.split(" ")
        for i in range(len(t_lists)):
            t1 = t_lists[i]
            if bool(Tag.objects.filter(name=t1)):
                already = Tag.objects.filter(name=t1)[0]
                p.tag.add(already)
            else:
                p.tag.add(Tag.objects.create(name=t1))
        return redirect('post:post_detail', post.pk)

    ctx = {
        'form': form,
    }

    return render(request, 'post/post_write.html', ctx)


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if request.method == 'POST' and form.is_valid():
        post = form.save()
        p = Post.objects.get(pk=post.pk)
        t_lists = post.hashtag.split(" ")
        for i in range(len(t_lists)):
            t1 = t_lists[i]
            if bool(Tag.objects.filter(name=t1)):
                already = Tag.objects.filter(name=t1)[0]
                p.tag.add(already)
            else:
                p.tag.add(Tag.objects.create(name=t1))

        return redirect('post:post_detail', post.pk)

    ctx = {
        'form': form,
    }

    return render(request, 'post/post_write.html', ctx)


def post_delete(request, pk):
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        post.delete()

        return redirect(reverse('post:post_list'))

    else:
        return HttpResponse(status=400)


def show_tag(request):
    all_tags = Tag.objects.all()
    ctx = {
        'tag_list': all_tags,
    }
    return render(request, 'post/tags.html', ctx)


def tag_post_list(request, kwargs):
    posts = Tag.objects.get(name=kwargs).post_set.all()
    ctx = {
        'tag_post_list': posts,
        'tag': kwargs,
    }
    return render(request, 'post/search_list.html', ctx)


def search_posts(request):
    kwargs = request.GET.get('search_word')
    results = Post.objects.filter(
        Q(title__icontains=kwargs) | Q(content__icontains=kwargs)
    )
    if results:
        return render(request, 'post/search.html', {
            'searched_posts': results,
        })
    else:
        return render(request, 'post/search.html', {
            'no_search_comment': '검색된 결과가 없습니다',
        })


class MyListView(generic.ListView):
    model = Post
    template_name = 'post/test_view.html'
    paginate_by = 5
    context_object_name = 'post'


class MyDetailView(generic.DetailView):
    model = Post
    template_name = 'post/test_detail_view.html'
    context_object_name = 'post'
