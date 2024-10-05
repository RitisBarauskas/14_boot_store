from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from goods.constants import MAX_GOODS_PER_PAGE as M_GOODS
from goods.models import Good, Category
from goods.forms import GoodForm, CategoryForm


def index(request):
    goods = Good.objects.all()[:M_GOODS]
    return render(request, 'goods/index.html', {'goods': goods})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'goods/categories.html', {'categories': categories})


def goods_by_category(request, category_slug):
    category = get_object_or_404(Category.objects.select_related('author'), slug=category_slug)
    goods = category.goods.all()

    return render(request, 'goods/goods_by_category.html', {'category': category, 'goods': goods})


def good_detail(request, good_id):
    good = get_object_or_404(Good.objects.select_related('creator'), id=good_id)

    return render(request, 'goods/good_detail.html', {'good': good})


@login_required
def profile(request):
    goods = request.user.goods.all()
    return render(request, 'goods/profile.html', {'goods': goods})


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'goods/category_create.html'
    success_url = reverse_lazy('goods:categories')


class GoodCreate(LoginRequiredMixin, CreateView):
    model = Good
    form_class = GoodForm
    template_name = 'goods/good_create.html'

    def get_success_url(self):
        return reverse_lazy('goods:goods_by_category', kwargs={'category_slug': self.object.category.slug})
