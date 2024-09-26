from django.shortcuts import render, get_object_or_404

from goods.constants import MAX_GOODS_PER_PAGE as M_GOODS
from goods.models import Good, Category


def index(request):
    goods = Good.objects.all()[:M_GOODS]
    return render(request, 'goods/index.html', {'goods': goods})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'goods/categories.html', {'categories': categories})


def goods_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    goods = category.goods.all()

    return render(request, 'goods/goods_by_category.html', {'category': category, 'goods': goods})


def good_detail(request, good_id):
    good = get_object_or_404(Good, id=good_id)

    return render(request, 'goods/good_detail.html', {'good': good})
