from store.models import Category


def store_website(request):
    Categories = Category.objects.order_by('order')
    return {
        'categories': Categories
    }
