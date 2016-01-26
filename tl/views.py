
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Test, WaveDate
from .forms import TestForm, WaveDateForm


# Create your views here.

def home(request):
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'tl/home.html')


def newtest(request):
    if request.method == 'POST':
        test_form = TestForm(request.POST)
        wavedate_form = WaveDateForm(request.POST)
        if test_form.is_valid():
        	test = test_form.save()
        	test.save()

        	if wavedate_form.is_valid():
        		wave = wavedate_form.save(commit=False)
        		wave.test_no = test.test_no
        		wave.save()

    else:
        test_form = TestForm()
        wavedate_form = WaveDateForm()

    return render(request, 'tl/newtest.html', {'test_form': test_form, 'wavedate_form': wavedate_form})



def modifytest(request):
    return HttpResponse("This is the page to modify an existing test.") 