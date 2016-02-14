
import os
import csv

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import UpdateView, DetailView, ListView
from django.db import connection


from .models import Test, WaveDate, Product, Store
from .forms import TestForm, WaveDateForm, ProductForm, StoreForm, SponsorForm


# Create your views here.

def home(request):
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'tl/home.html')


class IndexView(ListView):
    template_name = 'tl/index.html'
    model = Test


def DetailView(request, pk):
    test = get_object_or_404(Test, pk=pk)
    #form = TestForm(instance=test)
    return render(request, 'tl/detail.html', {'test': test})


# class UpdateView(UpdateView):
#     model = Test
#     form_class = TestForm
#     template_name = 'tl/edit.html'


def UpdateView(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == 'POST':
        test_form = TestForm(request.POST, instance=test)

        if test_form.is_valid():
            test = test_form.save()
            return redirect('/tl/', pk=test.pk)
    else:
        test_form = TestForm(instance=test)
    return render(request, 'tl/edit.html', {'test_form': test_form})



def newtest(request):
    if request.method == 'POST':
        test_form = TestForm(request.POST)
        sponsor_form = SponsorForm(request.POST)
        wavedate_form = WaveDateForm(request.POST)
        product_form = ProductForm(request.POST)
        store_form = StoreForm(request.POST, request.FILES) 

        if test_form.is_valid() and wavedate_form.is_valid() and product_form.is_valid() and store_form.is_valid() and sponsor_form.is_valid():
            test = test_form.save()
            test.save()

            sponsor = sponsor_form.save(commit=False)
            sponsor.test_no = test.test_no
            sponsor.save()

            wave = wavedate_form.save(commit=False)
            wave.test_no = test.test_no
            wave.save()

            # Tier 1 Proudcts
            super_category_list = product_form.cleaned_data['super_category_tier1']
            if super_category_list:
                for i in super_category_list:
                    p1 = Product(test_no=test.test_no, product_no=i, product_level_no=2,product_tier=1, group_no=1)
                    p1.save()

            category = product_form.cleaned_data['category_tier1']
            if category:
                p2 = Product(test_no=test.test_no, product_no=category, product_level_no=3,product_tier=1, group_no=1)
                p2.save()

            sub_category = product_form.cleaned_data['sub_category_tier1']
            if sub_category:
                p3 = Product(test_no=test.test_no, product_no=sub_category, product_level_no=4,product_tier=1, group_no=1)
                p3.save()

            segment = product_form.cleaned_data['segment_tier1']
            if segment:
                p4 = Product(test_no=test.test_no, product_no=segment, product_level_no=5,product_tier=1, group_no=1)
                p4.save()

            sku = product_form.cleaned_data['sku_tier1']
            if sku:
                p5 = Product(test_no=test.test_no, product_no=sku, product_level_no=7,product_tier=1, group_no=1)
                p5.save()

            # Tier 2 Proudcts
            super_category_list = product_form.cleaned_data['super_category_tier2']
            if super_category_list:
                for i in super_category_list:
                    p1 = Product(test_no=test.test_no, product_no=i, product_level_no=2,product_tier=2, group_no=i)
                    p1.save()

            category = product_form.cleaned_data['category_tier2']
            if category:
                p2 = Product(test_no=test.test_no, product_no=category, product_level_no=3,product_tier=2, group_no=category)
                p2.save()

            sub_category = product_form.cleaned_data['sub_category_tier2']
            if sub_category:
                p3 = Product(test_no=test.test_no, product_no=sub_category, product_level_no=4,product_tier=2, group_no=sub_category)
                p3.save()

            segment = product_form.cleaned_data['segment_tier2']
            if segment:
                p4 = Product(test_no=test.test_no, product_no=segment, product_level_no=5,product_tier=2, group_no=segment)
                p4.save()

            sku = product_form.cleaned_data['sku_tier2']
            if sku:
                p5 = Product(test_no=test.test_no, product_no=sku, product_level_no=7,product_tier=2, group_no=sku)
                p5.save()


            # Load store list
            store_list = store_form.cleaned_data['store_list']
            data = csv.DictReader(store_list)
            for row in data:
                Store.objects.create(
                test_no=test.test_no,
                location_id=row['location_id'],
                test_store=row['test_store'],
                pair=row['pair'],
                wave_no=row['wave_no'])
    else:
        test_form = TestForm()
        wavedate_form = WaveDateForm()
        product_form = ProductForm()
        store_form = StoreForm() 
        sponsor_form = SponsorForm() 

    return render(request, 'tl/newtest.html', {'test_form': test_form, 
                                               'wavedate_form': wavedate_form, 
                                               'product_form': product_form, 
                                               'store_form': store_form,
                                               'sponsor_form': sponsor_form,
                                               })


def QueryView(request):
    cursor = connection.cursor()

    cursor.execute("SELECT location_key, SUM(spend) AS total_spend FROM item_fact_sample GROUP BY 1")

    context = cursor.fetchall()

    return render(request, 'tl/query.html', {'context': context})
