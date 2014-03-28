from django.shortcuts import render
from django.http import HttpResponse
from dogapp.models import Person, Dog
# Create your views here.
	
def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 100:
			errors.append('Please enter at most 100 characters.')
		else:
			dogs = Dog.objects.filter(dogName__icontains=q)
			return render(request, 'search_results.html',
				{'dogs': dogs, 'query': q})
	return render(request, 'search_results.html', {'errors': errors})

def listall(request):
	dogs = Dog.objects.all()
	return render(request, 'listall.html', {'dogs' : dogs})
	
def addNew(request):
	return render(request, 'addNew.html')
	