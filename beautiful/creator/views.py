from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import ReviewForm
from .models import Review, Item
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def creator_main(request, creatorname=None, content_pk=None):
    # list of creator is needed for rendering the nav-bar
    # creator with no youtube_content will be not displayed
    creator_list = User.objects.filter(
                    profile__is_creator=True).exclude(
                    Youtube_Content__isnull=True).order_by('pk')

    # user selects which creator page one will browse
    if creatorname is None:
        creator = creator_list.first()
    else:
        creator = get_object_or_404(User, username=creatorname)

    # default video is first video
    if content_pk is None:
        youtube_content = creator.Youtube_Content.first()
    else:
        youtube_content = get_object_or_404(
            creator.Youtube_Content,
            pk=content_pk
        )
        # get the first item from the video in default
    try:
        item = youtube_content.item.first()
    except IndexError:
        item = youtube_content.item.none()

    ctx = {
        'creator_list': creator_list,
        'creator': creator,
        'youtube_content': youtube_content,
        'form': ReviewForm(),
        'item': item,
    }
    return render(request, 'creator/creator_page.html', ctx)


def review_board(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    ctx = {
        'item': item,
        'form': ReviewForm(),
        }
    if request.method == 'POST' and request.is_ajax():
        return render(request, 'creator/review.html', ctx)


def create_review(request, item_pk):
    if request.method == 'POST' and request.is_ajax():
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            review = form.save(commit=False)
            review.Item = get_object_or_404(Item, pk=item_pk)
            review.author = request.user
            review.save()
        return render(request, 'creator/review_form.html', {'review': review, })
    else:
        HttpResponse(status=400)


def delete_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    item = review.Item
    review.delete()
    try:
        content = review.Item.youtube_content_set.all()[0]
        creator = content.creator

        return redirect(reverse('creator:creator_page',
                                kwargs={'creatorname': creator,
                                        'content_pk': content.pk}))
    except IndexError:
        return redirect(reverse('review:item_review', kwargs={'item_pk': item.pk}))
