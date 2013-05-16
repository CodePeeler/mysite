from django.http import HttpResponse
#from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from polls.models import Poll
from django.http import Http404

def indexx(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = Context({'latest_poll_list': latest_poll_list, })   
    context = {'latest_poll_list': latest_poll_list}	
    #return HttpResponse(template.render(context))
    return render(request, 'polls/index.html', context)
   
	
def detail(request, poll_id):
    #try:
        #poll = Poll.objects.get(pk=poll_id)
    #except Poll.DoesNotExist:
        #raise Http404
    #return render(request, 'polls/details.html', {'poll': poll})
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/details.html', {'poll': poll})
	
def results(request, poll_id):
	return HttpResponse("You're looking at the resutls of poll %s." % poll_id)
	

def votes(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)
	
def custom_404_view(request):
    return HttpResponse("You messed up Error 404 page not found")
