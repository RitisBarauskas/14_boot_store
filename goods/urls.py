from django.urls import path

from goods.views import index, categories, goods_by_category, good_detail, CategoryCreate, GoodCreate, profile

app_name = 'goods'

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('categories/create/', CategoryCreate.as_view(), name='category_create'),
    path('categories/<slug:category_slug>/', goods_by_category, name='goods_by_category'),
    path('goods/create/', GoodCreate.as_view(), name='good_create'),
    path('goods/<int:good_id>/', good_detail, name='good_detail'),
    path('profile/', profile, name='profile'),
]
