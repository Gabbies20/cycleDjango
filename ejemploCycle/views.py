from django.shortcuts import render

# Create your views here.
def my_view (request):
    items = ['Item1', 'Item2', 'Item3', 'Item4', 'Item5']
    return render(request, 'my_template.html',{'items':items})
