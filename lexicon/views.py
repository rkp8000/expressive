import random
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Term


class Index(generic.ListView):
    model = Term
    template_name = 'lexicon/index.html'

    def get_queryset(self):
        return Term.objects.order_by('term_text')


class TermDetail(generic.DetailView):
    model = Term
    template_name = 'lexicon/term_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TermDetail, self).get_context_data(**kwargs)
        kwargs = self.kwargs

        if 'show_example_sentences' in kwargs \
                and kwargs['show_example_sentences'] == 'show_example_sentences':
            context['show_example_sentences'] = True
        else:
            context['show_example_sentences'] = False

        return context


def random_term(request):
    term = random.choice(Term.objects.all())
    return HttpResponseRedirect(reverse('lexicon:term_detail', args=(term.id,)))


def add_sentence(request, term_id):
    term = get_object_or_404(Term, pk=term_id)
    kwargs = {'pk': term_id}
    try:
        term.sentence_set.create(sentence_text=request.POST['sentence_text'])
        kwargs['show_example_sentences'] = 'show_example_sentences'
    except:
        pass
        kwargs['show_example_sentences'] = 'error'

    return HttpResponseRedirect(
        reverse('lexicon:term_detail_add_sentence', kwargs=kwargs))
