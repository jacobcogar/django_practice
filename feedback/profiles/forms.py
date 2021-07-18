from django import forms

class ProfileForm(forms.Form):
    user_image = forms.ImageField() # Changed to ImageField from FormField