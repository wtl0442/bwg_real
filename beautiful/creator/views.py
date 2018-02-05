from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.


def creator_main(request, creatorname, content_pk='#'):
    creator_list = User.objects.filter(is_staff=True)
    creator = get_object_or_404(User, username=creatorname)
    if content_pk == '#':
        # default video is first video
        youtube_content = creator.Youtube_Content.first()
    else:
        youtube_content = get_object_or_404(
            creator.Youtube_Content,
            pk=content_pk
        )
    ctx = {
        'creator_list': creator_list,
        'creator': creator,
        'youtube_content': youtube_content,
    }
    return render(request, 'creator/creator_page.html', ctx)