from django.shortcuts import render

# Create your views here.
def search(request):
    query = request.GET.get('q')
    results = searchapp.objects.filter(name__icontains=query) # replace YourModel and name with your model and field
    return render(request, 'search.html',{'name':'Jineet'})