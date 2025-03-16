from django.shortcuts import render, HttpResponseRedirect, reverse


# Create your views here.

def request_1(request):
    if request.method == 'POST':
        pass
        # database
        # return HttpResponseRedirect(reverse())


def request_3(request):
    return render(request, 'main_2.html')