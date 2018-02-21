from creator.models import Brand
from accounts.models import SkinType


def brand(request):
    return {
        'brands': Brand.objects.all(),
    }


def skintype(request):
    return {
        'skin_types': SkinType.objects.all(),
    }
