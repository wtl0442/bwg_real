from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from creator.models import Item
from .models import Review
from .forms import ReviewForm
# Create your views here.


def board(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ReviewForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        review = form.save(commit=False)
        review.Item = item
        review.author = request.user
        review.save()
        return redirect(reverse('review:review_board', kwargs={'pk': pk}))
    ctx = {
        'item': item,
        'form': form,
    }
    return render(request, 'review/review_board.html', ctx)


def revise_review(request, pk):
    item = get_object_or_404(Item, item_review__pk=pk)
    review = get_object_or_404(Review, pk=pk)
    form = ReviewForm(request.POST or None, instance=review)
    if request.method == 'POST' and form.is_valid():
        review = form.save(commit=False)
        review.save()
        return redirect(reverse('review:review_board', kwargs={'pk': item.pk}))
    ctx = {
        'item': item,
        'form': form,
    }
    return render(request, 'review/review_board.html', ctx)