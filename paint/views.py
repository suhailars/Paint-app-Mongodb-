from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from paint.models import Image
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime
def home(request):
	if request.method=='GET':
		t = get_template('paintnew.html')
		html = t.render(Context({}))
		return HttpResponse(html)
@csrf_exempt
def save(request):
	iname=request.POST.get('name')
	idata=request.POST.get('data')
	p=Image(name=iname,data=idata)
	p.save()
	t = get_template('paintnew.html')
	html = t.render(Context({}))
	return HttpResponse(html)

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def gallery(request):
	posts=[dict(id=i.id,title=i.name) for i in Image.objects.order_by('id')]
	return render(request, 'gallery.html', {'posts': posts})
def load(request,imgname):
        data=Image.objects.filter(name=imgname)
        print data[0].id
	for i in Image.objects.filter(name=imgname):
		print i.id
	posts=[dict(id=i.id,title=i.name,imagedata=i.data) for i in Image.objects.filter(name=imgname)]
	return render(request,'picload.html',{'posts':posts})

