from django.forms import forms, ModelForm

from .models import Test, WaveDate


class WaveDateForm(ModelForm):
	class Meta:
		model = WaveDate
		exclude = ('test_no',)


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'