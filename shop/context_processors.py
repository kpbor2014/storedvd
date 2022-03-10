from shop.forms import SearchForm
from shop.models import Section


def add_default_data(request):
    sections = Section.objects.all().order_by('title')
    search_form = SearchForm()

    return {'sections': sections, 'search_form':search_form}