from django import forms
from django_filters import FilterSet, ChoiceFilter, DateFilter
from .models import Post


class PostsFilter(FilterSet):
    title = ChoiceFilter(choices=[(post.title, post.title) for post in Post.objects.all()], label='Title',
                         empty_label='Select title', widget=forms.Select(attrs={'class': 'form-control'}))
    location = ChoiceFilter(choices=[(post.location, post.location) for post in Post.objects.all()], label='Location',
                            empty_label='Select location', widget=forms.Select(attrs={'class': 'form-control'}))
    salary = ChoiceFilter(choices=[(post.salary, post.salary) for post in Post.objects.exclude(salary__exact='').all()],
                          label='Salary', empty_label='Select salary',
                          widget=forms.Select(attrs={'class': 'form-control'}))

    date_posted = DateFilter(field_name='date_posted', lookup_expr='gte', label='Date posted',
                             widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['title', 'location', 'salary', 'date_posted']
