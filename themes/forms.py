from django import forms


class ThemeDownloadForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(
        max_length=60,
        help_text='Your download link will be sent via this email.'
    )
