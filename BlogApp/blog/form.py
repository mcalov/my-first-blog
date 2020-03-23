from django import forms

class SelectForm(forms.Form):
    firstname = forms.CharField(label="Searchterm", max_length=50)
    # image = forms.ImageField(max_length=100,allow_empty_file=True,required=True)
    image = forms.FileField()

class ImportForm(forms.Form):
    importFile = forms.FileField(label="Exelfile Upload", max_length=50)
    # image = forms.ImageField(max_length=100,allow_empty_file=True,required=True)



