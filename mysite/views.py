from django.http import HttpResponse
from django.shortcuts import render_to_response
from forms import Ckeditor_test_form

def ckeditor_test(request):
	if 'title' in request.GET:
		q = request.GET['body']
		return render_to_response('article_show.html', {'body':q})
	else:
		form = Ckeditor_test_form()
		return render_to_response('ckeditor_test.html', {'form':form})

def display_meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))
import json
def ajax(request):
    """returns json response"""
    return HttpResponse(json.dumps({'foo': 'bar'}), mimetype='application/json')

from django.template import Context, Template
def index(request):
    """simple index page which uses jquery to make a single get request to /ajax, alerting the value of foo"""
    t = Template("""
    <!doctype html>
      <head>
       <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"></script>
       <script type="text/javascript">
         $.get('/py/ajax_echo/', function(data) {
           alert(data['foo']);
         });
       </script>
     </head>
    </html>""")
    return HttpResponse(t.render(Context()))
