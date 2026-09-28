from django import forms

from .models import ContactRequest, Product


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'phone', 'email', 'product', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'name'}),
            'phone': forms.TextInput(attrs={'autocomplete': 'tel', 'inputmode': 'tel'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'email'}),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Tipul lucrării, dimensiuni aproximative, localitatea…',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(is_published=True)
        self.fields['product'].empty_label = 'Nu știu încă / altceva'
