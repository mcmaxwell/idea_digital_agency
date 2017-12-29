from info.models import Info
from django.core.context_processors import request

def info(request):
    info = Info.objects.all()
    return {"info": info}
