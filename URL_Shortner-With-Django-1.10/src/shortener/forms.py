from django import forms


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit URL')

    def clean(self):
        cleaned_data = super()
