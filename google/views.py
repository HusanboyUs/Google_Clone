import tkinter
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
import requests
# Create your views here.
def homePage(request):
    return render(request, 'index.html')

def viewPage(request):
    if request.method=='POST':
        search=request.POST['search']
        url = 'https://www.ask.com/web?q='+search
        res=requests.get(url)
        soup=bs(res.text, 'lxml')
        result_listings = soup.find_all('div', {'class': 'PartialSearchResults-item'})
        final_result=[]
        for result in result_listings:
            result_title=result.find(class_='PartialSearchResults-item-title').text
            result_url=result.find('a').get('href')
            result_description=result.find(class_='PartialSearchResults-item-abstract').text
            reslt_test='Working'
            final_result.append((result_title,result_url,result_description,reslt_test))
        context={
            'final_result':final_result
        }
        
        return render(request, 'view.html',context )
    else:
        return render(request, 'view.html')
