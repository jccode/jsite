# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from polls.models import Poll, Choice

def index(request):
    """
    to index page
    """
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    
    # template = loader.get_template('polls/index.html')
    # context = Context({
    #     'latest_poll_list': latest_poll_list
    # })
    # return HttpResponse(template.render(context))

    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    """
    """
    # try:
    #     poll = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404

    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})


def results(request, poll_id):
    """
    
    Arguments:
    - `request`:
    - `poll_id`:
    """
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
    # return HttpResponse("You're looking at the results of poll %s." % poll_id)


def vote(request, poll_id):
    """
    
    Arguments:
    - `request`:
    - `poll_id`:
    """

    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice'"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
    

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by("-pub_date")[:5]

    
class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        
        Arguments:
        - `self`:
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())


    
class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'
