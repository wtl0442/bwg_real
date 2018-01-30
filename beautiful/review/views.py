from django.shortcuts import render
from .models import Item
# Create your views here.


def board(request, pk):
    item = Item.objects.get(pk=pk)
    ctx = {
        'item': item,
    }
    return render(request, 'review/review_board.html', ctx)