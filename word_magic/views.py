from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
	return render(request, 'home.html', {'count': 0, 'word_dict': {}})

def count(request):
	original_text = request.GET["full_text"]
	words = clean_words(original_text)
	count = len(words)
	word_dict = {}
	for c in words:
		if c in word_dict:
			word_dict[c] += 1
		else:
			word_dict[c] = 1
	return render(request, 'home.html', {
		'count': count, 
		'words': original_text, 
		"word_dict": word_dict
		})
 
def clean_words(word_to_be_cleaned):
	pattern = re.compile(r'\s+')
	ws_removed =  re.sub(pattern, '', word_to_be_cleaned)
	return ws_removed.lower()

def simple(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response
