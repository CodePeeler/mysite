from django.http import HttpResponseRedirect, HttpResponse
#from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Poll

class IndexView(generic.ListView):
    #We specify the template name in order not to use the default one
    template_name = 'polls/index.html'
    #we override the defalut context variable vlaue by specifing latest_poll_list
    context_object_name = 'latest_poll_list'
    
    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll	
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'    

def indexx(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
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
    #return render_to_response('polls/details.html', {'poll': poll})
    p = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': p})
	
def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
    #return HttpResponse("You're looking at the resutls of poll %s." % r)
	

def votes(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', { 'poll': p, 'error_message': "you didn't select a choice.", })
    else:
        selected_choice.votes += 1	
        selected_choice.save()
        #return HttpResponse("You're voting on poll %s." % poll_id)
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,) ))
		#By using redirect if the page is reloaded it won't update the database again!
        
	
def custom_404_view(request):
    return HttpResponse("You messed up Error 404 page not found")

