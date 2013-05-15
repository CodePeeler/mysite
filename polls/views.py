from django.http import HttpResponse

def indexx(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	return HttpResponse("<h2>Hello, world.</h2><br /> You're at the poll index.")
	
def detail(request, p_id):
	return HttpResponse("You're looking at poll %s." % p_id)
	
def results(request, poll_id):
	return HttpResponse("You're looking at the resutls of poll %s." % poll_id)
	

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)
