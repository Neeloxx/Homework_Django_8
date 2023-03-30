from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from .models import Post


class PostFilter(FilterSet):
    date = DateFilter(field_name='post_time_in', widget=DateInput(attrs={'type': 'date'}), label='search by date',
                      lookup_expr='date__gte')

    class Meta:
        model = Post

        fields = {

            'title': ['icontains'],

            'author__user': ['exact'],

        }
