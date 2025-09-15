from django import forms

class CropInputForm(forms.Form):
    crop_name = forms.CharField(label="Crop Name", max_length=100)
    soil_type = forms.CharField(label="Soil Type", max_length=100)
