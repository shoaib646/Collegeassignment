from django import forms
from .models import FishMarketModel



class FishMarketForm(forms.ModelForm):
    class Meta:
        model = FishMarketModel
        fields = '__all__'

        widgets : {
            'weight' : forms.NumberInput(attrs={'class': 'form-control','placeholder': 'e.g 6145'}),
            'length1' : forms.NumberInput(attrs={'class': 'form-control','placeholder': 'e.g 6145'}),
            'length2' : forms.NumberInput(attrs={'class': 'form-control','placeholder': 'e.g 6145'}),
            'length3' : forms.NumberInput(attrs={'class': 'form-control','placeholder': 'e.g 6145'}),
            'height' : forms.NumberInput(attrs={'class': 'form-control','placeholder': 'e.g 6145'}),
            'width' : forms.NumberInput(attrs={'class': 'form-control','placeholder': 'e.g 6145'}),
        }
