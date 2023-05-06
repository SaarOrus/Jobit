import django_filters
from .models import Post


class PostsFilter(django_filters.FilterSet):

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'location': ['iexact'],
            'salary': ['iexact'],
            'date_posted': ['date__iexact', 'date__gte', 'date__lte'],
        }
