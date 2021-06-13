from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Sale
from .forms import SalessSearchForm
import pandas as pd


# Create your views here.
def home_view(request):
  form = SalessSearchForm(request.POST or None)

  if request.method == 'POST':
    date_form = request.POST.get('date_form')
    date_to = request.POST.get('date_to')
    chart_type = request.POST.get('chart_type')
    print(date_form,date_to,chart_type)

    qs = Sale.objects.filter(created__date=date_form)
    obj = Sale.objects.get(id=2)
    
    df1 = pd.DataFrame(qs.values())
    print(df1)
    print("########")
    
  
  context = {
    
    'form' : form,
  }
  
  return render(request,'sales/home.html',context)


class SalesListView(ListView):
  model = Sale
  template_name = 'sales/main.html'
  

class SalesDetailView(DetailView):
  model = Sale
  template_name = 'sales/detail.html'


#def sales_list_view(request):
 # qs = Sale.objects.all()
 # return render(request,'sales/main.html',{
 #   'object_list':qs
 # })

#def sale_detail_view(request,pk):
 # obj = Sale.objects.get(pk=pk)
 
  #return render(request,'sales/detail.html',{
  #  'object':obj

 #})



