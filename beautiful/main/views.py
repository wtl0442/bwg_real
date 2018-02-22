from django.shortcuts import render
from django.http import JsonResponse
from .forms import SubscribeForm
from .models import SubscribedEmail

from post.models import Tag, Post
from beautywiki.models import TroubleWiki
from django.db.models import Count
from creator.models import Item, Category


def showMain(request):
    # 태그 부분
    tags = list(Tag.objects.all())
    length = len(tags) - 1
    hot_tags = []
    for i in range(length):
        for j in range(length - i):
            if tags[j].post_set.count() < tags[j + 1].post_set.count():
                tags[j], tags[j + 1] = tags[j + 1], tags[j]
    for k in range(0, 5):
        hot_tags.append(tags[k].name)
    # 게시글 부분
    hot_posts = Post.objects.annotate(num_comments=Count('comment')).order_by('-num_comments')[:5]
    # 금주의 피부백서
    this_wiki = TroubleWiki.objects.get(pk=1)
    recommendation = {i.name: list(item_rank(i.name)) for i in Category.objects.all()}
    return render(request, 'main/main.html', {
        'hot_tags': hot_tags,
        'hot_posts': hot_posts,
        'this_wiki': this_wiki,
        'form': SubscribeForm(),
        'recommendation': recommendation,
    })


def item_rank(category):
    cateogrized_list = Item.objects.filter(category__name=category)
    item_in_order = cateogrized_list.annotate(
                    num_reviews=Count('item_review')).order_by(
                    '-num_reviews')
    top_three = item_in_order[:3]

    return top_three


def subscribe_email(request):
    form = SubscribeForm(request.POST)
    data = {
        'success': False,
    }
    if form.is_valid():
        email = form.cleaned_data['email']
        _email, created = SubscribedEmail.objects.get_or_create(email=email)
        data['success'] = True
        data['created'] = created

    return JsonResponse(data)


def unsubscribe_email(request):
    form = SubscribeForm(request.POST)
    data = {
        'success': False,
    }
    if form.is_valid():
        email = form.cleaned_data['email']
        deleted_count = SubscribedEmail.objects.filter(email=email).delete()[0]
        data['success'] = True
        data['deleted'] = bool(deleted_count)

    return JsonResponse(data)
