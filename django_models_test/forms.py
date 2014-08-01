from django.forms import forms


class ImageForm(forms.Form):
    image_file = forms.FileField(
        label='Select image file'
    )