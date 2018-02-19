from django.shortcuts import render

from post.models import Tag, Post
from beautywiki.models import TroubleWiki
from django.db.models import Count


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
    return render(request, 'main/main.html', {
        'hot_tags': hot_tags,
        'hot_posts': hot_posts,
        'this_wiki': this_wiki,
    })

