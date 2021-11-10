from django.contrib.auth.models import User

def project_context(request):

    context = {
        'ne': User.objects.first(),
    }
    return context