from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [
	{
		'author': 'CoreyMS',
		'title':  'Blog Post 1',
		'content': 'First post comment',
		'date_posted' : 'Wed 13-05-2020 1:30PM IST'
	},
	{
		'author': 'MacMalem',
		'title':  'Blog Post 2',
		'content': 'Second post comment',
		'date_posted' : 'Wed 15-05-2020 1:30PM IST'
	},
	{
		'author': 'Sweet Julie',
		'title':  'Blog Post 3',
		'content': 'Third post comment',
		'date_posted' : 'Wed 23-05-2020 1:30PM IST'
	}

]

def home(request):
	context = {
		'posts':Post.objects.all()
	}
	return render(request,'blog/home.html',context)

def about(request):
	return render(request,'blog/about.html',{'title':'About'})