from info.models import Info
from django.core.context_processors import request

def info(request):
	print "Hello World"
	info = Info.objects.all()
	return {"info": info}
