from shop.models import Section


def add_default_data(request):
    sections = Section.objects.all().order_by('title')
    return {'sections': sections}