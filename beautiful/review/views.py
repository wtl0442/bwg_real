from django.shortcuts import render
from creator.models import Item
from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string

# Create your views here

# popularity depends on the 'number of reviews' on each item


def review_list(request):
    item_in_order = Item.objects.annotate(
                    num_reviews=Count('item_review')).order_by(
                    '-num_reviews')
    top_three = item_in_order[:3]
    rest_item = item_in_order[3:13]
    ctx = {
        'top_three': top_three,
        'rest_item': rest_item,
    }
    return render(request, 'review/review_list.html', ctx)


def load_more_review(request, review_count):
    if request.method == 'POST' and request.is_ajax():
        item_in_order = Item.objects.annotate(
                        num_reviews=Count('item_review')).order_by(
                        '-num_reviews')
        more_item = item_in_order[review_count: review_count+10]

        if more_item:
            html = render_to_string(
                    'review/load_review.html',
                    {'more_item': more_item, 'review_count': review_count}
                )
            return JsonResponse({'status': True, 'html': html})
        else:
            return JsonResponse({'status': False})
    else:
        return HttpResponse(status=405)
