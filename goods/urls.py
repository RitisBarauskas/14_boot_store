from django.urls import path

from goods.views import index, categories, goods_by_category, good_detail

app_name = 'goods'

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('categories/<slug:category_slug>/', goods_by_category, name='goods_by_category'),
    path('goods/<int:good_id>/', good_detail, name='good_detail'),
]
