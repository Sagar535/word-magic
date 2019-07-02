from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'home.html', {'count': 0, 'word_dict': {}})

def count(request):
	print("Inside the count")
	words = request.GET["full_text"]
	count = len(words)
	word_dict = {}
	for c in words:
		if c in word_dict:
			word_dict[c] += 1
		else:
			word_dict[c] = 1
	return render(request, 'home.html', {
		'count': count, 
		'words': words, 
		"word_dict": word_dict
		})
 