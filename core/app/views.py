from django.shortcuts import render

from glob import iglob
import os.path
import json

import pymongo
from pymongo import MongoClient


from .forms import EmpresaForm


client = MongoClient('localhost', 27017)
db = client['hackaton']
# Create your views here.


def home(request):
	return render(request, 'app_templates/home.html')






def teste(request):

	#iglob(os.path.expanduser('~/Tweets/*.txt'))


	for fname in iglob(os.path.expanduser('~/Tweets/*.txt')):
		with open(fname) as fin:
			tweet = json.load(fin)
			
			tweets = db.tweets
			tweets.insert_one(tweet).inserted_id

			'''for tweet in fin:
													print(tweet)'''

	return render(request, 'app_templates/home.html')





def cadastroEmpresa(request):
	if request.method == "POST":

		form = EmpresaForm(request.POST)

		if form.is_valid():

			print ("PRaga deu")


	else: 

		form = EmpresaForm()
	
	context = {
    	'form': form
	}

	return render(request, 'app_templates/forms.html', context)
    



