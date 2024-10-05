from django.forms import ModelForm

from goods.models import Category, Good


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class GoodForm(ModelForm):
    class Meta:
        model = Good
        exclude = ('created_at', 'updated_at')
