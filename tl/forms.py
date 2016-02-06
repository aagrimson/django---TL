#from django.forms import forms, ModelForm
from django import forms
from .models import Test, WaveDate



class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['test_no', 'type', 'test_name', 'test_desc', 'sponsor', 'merch_group', 'success_metric', 'success_desc', 'success_value', 'test_type']
        labels = {'test_no': 'Test Number',
                  'type': 'Test Type',
                  'test_name': 'Test Name',
                  'test_desc': 'Test Description',
                  'sponsor': 'Sponsor',
                  'merch_group': 'Merchandise Group',
                  'success_metric': 'Success Metric',
        }


class WaveDateForm(forms.ModelForm):
	class Meta:
		model = WaveDate
		fields = ['wave_no', 'wave_value','pre_start','pre_end','post_start','post_end']
		wigets = {'pre_start': forms.SelectDateWidget}


SUPER_CATEGORY_CHOICES = (
	(1, 'CONSUMER HEALTH CARE'),
	(2, 'BEAUTY CARE'),
	(3, 'GENERAL MERCHANDISE'),
	(4, 'EDIBLES'),
	(5, 'GREETING CARDS'),
	(6, 'PHOTO'),
	(7, 'PERSONAL CARE'),
)



class ProductForm(forms.Form):
    super_category_tier1 = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, label='Super Category', choices=SUPER_CATEGORY_CHOICES, required=False)
    category_tier1 = forms.IntegerField(label='Category', required=False)
    sub_category_tier1 = forms.IntegerField(label='Sub Category', required=False)
    segment_tier1 = forms.IntegerField(label='Segment', required=False)
    sku_tier1 = forms.IntegerField(label = 'SKU', required=False)
    group_tier1 = forms.BooleanField(label = 'Group Tier 1 Products', required=False)
    
    super_category_tier2 = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, label='Super Category', choices=SUPER_CATEGORY_CHOICES, required=False)
    category_tier2 = forms.IntegerField(label='Category', required=False)
    sub_category_tier2 = forms.IntegerField(label='Sub Category', required=False)
    segment_tier2 = forms.IntegerField(label='Segment', required=False)
    sku_tier2 = forms.IntegerField(label = 'SKU', required=False)

class StoreForm(forms.Form):
	store_list = forms.FileField()