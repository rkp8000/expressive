import random
from django.shortcuts import render

from .models import Term


def index(request):
    term = random.choice(Term.objects.all())
    context = {'term': term}
    return render(request, 'lexicon/index.html', context)
