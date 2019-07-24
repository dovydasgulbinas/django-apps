from django import forms



class BandcampForm(forms.Form):
    # https://github.com/django/django/tree/master/django/forms/templates/django/forms/widgets
    album_url = forms.URLField()
