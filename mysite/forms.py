from django import forms
from ckeditor.widgets import CKEditorWidget



class Ckeditor_test_form(forms.Form):
	title = forms.CharField()
	body = forms.CharField(widget=CKEditorWidget())

