from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import sys

def judge(request):

    if request.method == "POST":
        Code = request.POST['code']
        Input = request.POST['input']
        #print(Code, Input , Output)
        y = Input
        Input = Input.replace("\n"," ").split(" ")
        def input():
            a = Input[0]
            del Input[0]
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(Code)
            sys.stdout.close()
            sys.stdout=orig_stdout
            Output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            Output = e
        print(Output)
        return render(request ,  'judge/judge.html', {"code": Code, "input": y, "output":Output})
    return render(request ,  'judge/judge.html')