from ast import Expression
import django_filters
from .models import Project


#Filter to sort through projects on project list page
class project_filter(django_filters.FilterSet):
#whether to display in ascending or descending order
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )

    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Project
        #title must contain, other must match exactly
        fields = {
            'title': ['icontains'],
            'conceptual': ['exact'], 
            'technical': ['exact'], 
            'programming': ['exact'], 
            'lecture': ['exact'], 
            'status': ['exact'],
            'date': ['exact'],
        }
    
    #if ascending is selected return projects in ascending order if no return descending (-title)
    def filter_by_order(self, queryset, name, value):
        expression = 'title' if value == 'ascending' else '-title'
        return queryset.order_by(expression)