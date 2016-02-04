
import os
import csv

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import UpdateView, DetailView, ListView

from .models import Test, WaveDate, Product, Store
from .forms import TestForm, WaveDateForm, ProductForm, StoreForm


# Create your views here.

def home(request):
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'tl/home.html')


class IndexView(ListView):
    template_name = 'tl/index.html'
    model = Test


# class DetailView(DetailView):
#     model = Test
#     template_name = 'tl/detail.html'


def DetailView(request, pk):
    test = get_object_or_404(Test, pk=pk)
    return render(request, 'tl/detail.html', {'test': test})


# class UpdateView(UpdateView):
#     model = Test
#     form_class = TestForm
#     template_name = 'tl/edit.html'


def UpdateView(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == 'POST':
        form = TestForm(request.POST, instance=test)
        if form.is_valid():
            test = form.save()
            test.save()
            #return redirect('tl/detail', pk=test.pk)
    else:
        form = TestForm(instance=test)
    return render(request, 'tl/edit.html', {'form': form})



def newtest(request):
    if request.method == 'POST':
        test_form = TestForm(request.POST)
        wavedate_form = WaveDateForm(request.POST)
        product_form = ProductForm(request.POST)
        store_form = StoreForm(request.POST, request.FILES) 

        if test_form.is_valid() and wavedate_form.is_valid() and product_form.is_valid() and store_form.is_valid():
            test = test_form.save()
            test.save()

            wave = wavedate_form.save(commit=False)
            wave.test_no = test.test_no
            wave.save()

            super_category_list = product_form.cleaned_data['super_category']
            for i in super_category_list:
                p1 = Product(test_no=test.test_no, product_no=i, product_level_no=2,product_tier=1, group_no=1)
                p1.save()

            category = product_form.cleaned_data['category']
            p2 = Product(test_no=test.test_no, product_no=category, product_level_no=3,product_tier=1, group_no=1)
            p2.save()

            sub_category = product_form.cleaned_data['sub_category']
            p3 = Product(test_no=test.test_no, product_no=sub_category, product_level_no=4,product_tier=1, group_no=1)
            p3.save()

            segment = product_form.cleaned_data['segment']
            p4 = Product(test_no=test.test_no, product_no=segment, product_level_no=5,product_tier=1, group_no=1)
            p4.save()

            store_list = store_form.cleaned_data['store_list']
            data = csv.DictReader(store_list)
            for row in data:
                Store.objects.create(
                test_no=test.test_no,
                location_id=row['location_id'],
                test_store=row['test_store'],
                pair=row['pair'])
    else:
        test_form = TestForm()
        wavedate_form = WaveDateForm()
        product_form = ProductForm()
        store_form = StoreForm() 

    return render(request, 'tl/newtest.html', {'test_form': test_form, 'wavedate_form': wavedate_form, 'product_form': product_form, 'store_form': store_form})