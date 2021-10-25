from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.models import ModelForm

from .models import Message


class MessageForm(ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))
    helper.form_method = 'POST'

    class Meta:
        model = Message
        fields = '__all__'
