# _*_ coding: utf-8 _*_

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response

def main_page(request):
	return render_to_response(
		'main_page.html',RequestContext(request)
	)
	
def user_page(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('Can not find username.')
		
	bookmarks = user.bookmark_set.all()
	
	template = get_template('user_page.html')
	variables = RequestContext(request, {
		'username': username,
		'bookmarks': bookmarks
	})
	output = template.render(variables)
	return HttpResponse(output)
	
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')