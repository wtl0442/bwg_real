from django.shortcuts import render, get_object_or_404
from creator.models import Item, Brand, Category
from accounts.models import SkinType
from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from creator.forms import ReviewForm

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


def item_review(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    form = ReviewForm()
    ctx = {
        'item': item,
        'form': form,
    }
    return render(request, 'review/item_review.html', ctx)


def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


def search_item(request):
    skin_type_input = request.GET.get('skin-type')
    category_input = request.GET.get('category')
    brand_input = request.GET.get('brand')
    item_name_input = request.GET.get('item_name')

    skin_type = get_or_none(SkinType, name=skin_type_input)
    brand = get_or_none(Brand, name=brand_input)
    category = get_or_none(Category, name=category_input)
    item_name = item_name_input

    inputs = {'skin_type': skin_type, 'category': category,
              'brand': brand, 'name': item_name}
    parameter = {}
    if request.method == "GET":
        ctx = {
            'search_result': Item.objects.filter(category__name__icontains=kwargs)
        }
    else:
        for key, value in inputs.items():
            if value:
                parameter[key] = value

        ctx = {
            'search_result': Item.objects.filter(**parameter),
        }

    return render(request, 'review/search_result.html', ctx)
