from django.shortcuts import render

from beautywiki.models import TroubleWiki


def wikimain(request):
    return render(request, 'beautywiki/beauty_wiki.html')


def trouble_wiki(request):
    trouble_lists = TroubleWiki.objects.all()

    return render(request, 'beautywiki/trouble_wiki.html', {
        'trouble_lists': trouble_lists,
    })

