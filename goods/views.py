from django.http import Http404
from django.shortcuts import render

from goods.constants import MAX_GOODS_PER_PAGE as M_GOODS
from goods.database import DATABASE


def index(request):
    goods = DATABASE.get('goods', [])[:M_GOODS]
    return render(request, 'goods/index.html', {'goods': goods})


def categories(request):
    return render(request, 'goods/categories.html', {'categories': DATABASE.get('categories', [])})


def goods_by_category(request, category_slug):
    categories = DATABASE.get('categories', [])
    category = next((item for item in categories if item.get('slug') == category_slug), None)
    if category is None:
        raise Http404()

    goods = DATABASE.get('goods', [])
    goods = [item for item in goods if item.get('category_id') == category.get('id')]

    return render(request, 'goods/goods_by_category.html', {'category': category, 'goods': goods})


def good_detail(request, good_id):
    goods = DATABASE.get('goods', [])
    good = next((item for item in goods if item.get('id') == good_id), None)

    if good is None:
        raise Http404()

    return render(request, 'goods/good_detail.html', {'good': good})
