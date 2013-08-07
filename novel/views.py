# Create your views here.
from django.template import RequestContext
from novel_request_form import NovelRequestForm
from django.shortcuts import render_to_response
from django.http import HttpResponse
from novel.models import NovelRequests

def request_novel(request):
    email = request.COOKIES.get('email') 
    form = NovelRequestForm({'email': email}) 
    sent = False
    form_recieved = None
    if request.method == 'POST': 
        form_recieved = NovelRequestForm(request.POST) 
        if form_recieved.is_valid(): 
            novel = NovelRequests(**form_recieved.cleaned_data)
            novel.save()
            sent = True
            form = NovelRequestForm({'email': form_recieved.cleaned_data['email']}) 
        else:
            form = form_recieved
    response = render_to_response('novel/request_novel.html', 
                                  {'form': form,  
                                   'sent': sent,
                                   'form_recieved': form_recieved }, 
                                  context_instance=RequestContext(request))
    if sent:
        response.set_cookie('email', form_recieved.cleaned_data['email']) 
    return response

    
    

