import requests

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

'''
for multi-level authorization 
'''
# def level_required(level=0):
#     def _inner1(function):
#         def _inner2(request, *args, **kwargs):
#             if request.user.profile.level < level:
#                 return render(request, 'dashboard/level_required.html',)
#             return function(request, *args, **kwargs)
#         return _inner2
#     return _inner1

def recaptcha_required(required_score=0.5):
    def _inner1(function):
        def _inner2(request, *args, **kwargs):
            if request.method == 'GET':
                return function(request, *args, **kwargs)
            data = {
                'response': request.POST.get('g-recaptcha-response',''),
                'secret': settings.RECAPTCHA_SECRET_KEY,
            }
            answer = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data).json()
            success = answer.get('success', False)
            score = answer.get('score', -0.1)
            try:
                score = float(score)
                if success == True and score > required_score:
                    return function(request, *args, **kwargs)
                else:
                    return redirect('home:robot_check_failed')
                #------end of else from success
            except Exception as e:
                return redirect('home:robot_check_failed')
        return _inner2
    return _inner1
#-------end of recaptcha required
