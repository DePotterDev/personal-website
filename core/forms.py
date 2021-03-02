from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-control col-lg'
        self.helper.label_class = 'form-label'
        self.helper.layout = Layout(
            'contact_name',
            'contact_email',
            'message',
        )