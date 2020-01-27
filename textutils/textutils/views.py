from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	"""with open('text.txt') as f:
		data = f.read()
		return HttpResponse(data);"""
	return render(request,'index.html')
	#return HttpResponse("data");

def about(request):
	return HttpResponse("<h1>This is about Page</h1>");


def delete(request):
	get = request.POST.get('text','get default value if not Text');
	punc = request.POST.get('remove','off');
	upr = request.POST.get('uppercase','off');
	newl = request.POST.get('newline','off');
	rmvspc = request.POST.get('removespace','off');

	punch = ".,?!'\":;-@#$%^&*_()[]}{";
	data = process(get,punc,upr,newl,rmvspc);
	print(data)
	dct = {"purpose":punc,"analyzed_text":data};
	return render(request,'analyzed.html',dct);



def process(string,punc,upper,newline,extraspace):
	if punc == "on":
		strng=""
		for i in string:
			if i not in ".,?!'\":;-@#$%^&*_()[]}{":
				strng+=i
		string = strng
	if upper == "on":
		string = string.upper();
	if newline == "on":
		strs=""
		print(string)
		for i in string:
			if i != "\n" and i !="\r":
				strs+=i
		string = strs
		print(string)
	if extraspace == "on":
		strs = ""
		for i,val in enumerate(string):
			if not(string[i] == " " and string[i+1] == " "):
				strs += val
		string = strs

	return string;