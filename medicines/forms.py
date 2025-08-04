from django import forms
from .models import Medicine


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'description', 'batch_number', 'manufacturing_date', 'expiry_date', 'manufacturer', 'mrp', 'caution']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter medicine name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter medicine description',
                'rows': 3
            }),
            'batch_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter batch number'
            }),
            'manufacturing_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'expiry_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'manufacturer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter manufacturer name'
            }),
            'mrp': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter MRP',
                'step': '0.01'
            }),
            'caution': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter cautionary information',
                'rows': 3
            }),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        manufacturing_date = cleaned_data.get('manufacturing_date')
        expiry_date = cleaned_data.get('expiry_date')
        
        if manufacturing_date and expiry_date:
            if manufacturing_date >= expiry_date:
                raise forms.ValidationError("Expiry date must be after manufacturing date.")
        
        return cleaned_data
