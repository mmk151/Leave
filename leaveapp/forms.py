from django import forms
class applyo(forms.Form):
    class Meta:
        models=apply
    Name = forms.CharField(max_length=55, blank=False)
    Department = forms.CharField(max_length=25, blank=False)
    Rollno = forms.CharField(max_length=8, blank=False, unique=True)
    Reason = forms.CharField(max_length=150, blank=False)
    FromDate = forms.DateTimeField(blank=False)
    ToDate = forms.DateTimeField(blank=False)
    email = forms.EmailField(max_length=50, blank=False)