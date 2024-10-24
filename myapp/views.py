from django.shortcuts import redirect, render
from myapp.forms import Myform,Eventform
import calendar
from calendar import HTMLCalendar
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from myapp.models import Event,Venue
def home(request):
    content='''<html>
<head>
<style>
  h1 {color:red;}
  p {color:blue;}
</style>
</head>
<body>

<h1>SAI kRISHNA</h1>


</body>
</html>
'''
    return HttpResponse(content)

def sayhi(request):
    return HttpResponse("Hello little Lemon")
def bharu(Request):
    conn='''<html><body><h1>Bhargavi</h1></body></html>'''
    return HttpResponse(conn)


def temp(request):
    path=request.path
    met=request.method
    msg=f'''
<br>path:{path}
<br>method:{met}
<br>scheme:{request.scheme}
<br>Address:{request.META['REMOTE_ADDR']}
<br>user-agent:{request.META['HTTP_USER_AGENT']}
<br>path-info:{request.path_info}

        '''
    return HttpResponse(msg)

def men(request,dish):
    item={
        'pasta':'pasta is green in colour',
        'venela':'venela is white in colour',
        'choco':'choclate is dark in colour'
    }
    c=f'''
<body><h1>{dish}</h1></body>'''

    return HttpResponse(c+item[dish])

def num(request,n):
    return HttpResponse(n)

def index(request):
    form=Myform()
    
    if request.method=='POST':
        form=Myform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'index.html',{'form':form})

def cal(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
    month=month.capitalize()
    month_num=list(calendar.month_name).index(month)
    month_number=int(month_num)

    calen=HTMLCalendar().formatmonth(year,month_number)
    # c=HTMLCalendar().format
    
    return render(request,'events/home.html',{'year':year,
             'month':month,
             'mn':month_num,
             'cal':calen,})

def event_list(request):
    event=Event.objects.all().order_by('name')
    return render(request,'events/event_list.html',{'eventss':event})

def addVenue(request):
    submited=False
    if request.method=='POST':
        form=Myform(request.POST)
        if form.is_valid():
            form.save()
            submited=True
            return HttpResponse('<h1>Venue Added Successfully..<h1/>')
    else:
        form=Myform
        if submited in request.GET:
            submited=True
    return render(request,'events/add_venue.html',{'form':form,'submited':submited})
def addEvent(request):
    submited=False
    if request.method=='POST':
        form=Eventform(request.POST)
        if form.is_valid():
            form.save()
            submited=True
            return HttpResponseRedirect('events')
    else:
        form=Eventform
        if submited in request.GET:
            submited=True
    return render(request,'events/add_event.html',{'form':form,'submited':submited})

def venue_list(request):
    if request.method=='POST':
        # Fetches the requested value
        search=request.POST['se']
        venue_obj=Venue.objects.filter(name__contains=search)
        return render(request,'events/venue_list.html',{'search':search,'obj':venue_obj})
    # In case we didn't enter anything in the search bar
    else:
        return render(request,'events/venue_list.html',{ })
    
from django.core.paginator import Paginator
def list_venues(request):
	#venue_list = Venue.objects.all().order_by('?')
	venue_list = Venue.objects.all()

	# Set up Pagination
	p = Paginator(Venue.objects.all(), 3)
	page = request.GET.get('page')
	venues = p.get_page(page)
	nums = "a" * venues.paginator.num_pages
	return render(request, 'events/venue.html', 
		{'venue_list': venue_list,
		'venues': venues,
		'nums':nums}
		)
def show_venue(request,index):
    venue_obj=Venue.objects.filter(name__contains=index)
    return render(request,'events/show_venue.html',{'obj':venue_obj})
def update_venue(request,index):
    venue_obj=Venue.objects.get(pk=index)
    form=Myform(request.POST or None,instance=venue_obj)
    if form.is_valid():
        form.save()
        return redirect('cal')
    return render(request,'events/update_venue.html',{'obj':venue_obj,'form':form})

def update_event(request,index):
    event_obj=Event.objects.get(pk=index)
    form=Eventform(request.POST or None,instance=event_obj)
    if form.is_valid():
        form.save()
        return redirect('check')
    return render(request,'events/update_event.html',{'obj':event_obj,'form':form})

def delete_event(request,index):
    event=Event.objects.get(pk=index)
    event.delete()
    return redirect('check')
def delete_venue(request,index):
    venue=Venue.objects.get(pk=index)
    venue.delete()
    return redirect('show-v')

