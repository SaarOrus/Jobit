from django import forms
from django_filters import FilterSet, ChoiceFilter, DateFilter
from .models import Post


class PostsFilter(FilterSet):
    title = ChoiceFilter(choices=[], label='Title', empty_label='Select title',
                         widget=forms.Select(attrs={'class': 'form-control'}))
    location = ChoiceFilter(choices=[], label='Location', empty_label='Select location',
                            widget=forms.Select(attrs={'class': 'form-control'}))
    salary = ChoiceFilter(choices=[], label='Salary', empty_label='Select salary',
                          widget=forms.Select(attrs={'class': 'form-control'}))

    date_posted = DateFilter(field_name='date_posted', lookup_expr='gte', label='Date posted',
                             widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['title'].extra['choices'] = self.get_title_choices()
        self.filters['location'].extra['choices'] = self.get_location_choices()
        self.filters['salary'].extra['choices'] = self.get_salary_choices()

    def get_title_choices(self):
        return [(post.title, post.title) for post in Post.objects.all()]

    def get_location_choices(self):
        return [(post.location, post.location) for post in Post.objects.all()]

    def get_salary_choices(self):
        return [(post.salary, post.salary) for post in Post.objects.exclude(salary__exact='').all()]

    class Meta:
        model = Post
        fields = ['title', 'location', 'salary', 'date_posted']