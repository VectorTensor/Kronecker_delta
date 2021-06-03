from django import forms

CHART_CHOICES = (
  ('#1','Bar Chart'),
  ('#2','Pie Chart'),
  ('#3','Line Chart'),
)

class SalessSearchForm(forms.Form):
  date_form = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
  date_to = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
  chart_type = forms.ChoiceField(choices=CHART_CHOICES)
