from django import forms
from .models import Package

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ["package_name", "destination", "duration", "price"]
        widgets = {
            "package_name": forms.TextInput(attrs={"placeholder": "Enter package name"}),
            "destination": forms.TextInput(attrs={"placeholder": "Enter destination"}),
            "duration": forms.TextInput(attrs={"placeholder": "Example: 5 Days / 4 Nights"}),
            "price": forms.TextInput(attrs={"placeholder": "Example: ₹15,000"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if not cleaned_data.get(field):
                self.add_error(field, "This field is required.")
        return cleaned_data
