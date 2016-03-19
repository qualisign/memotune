from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        if request.is_ajax():
            if request.POST.get('go'):
                pass
            elif request.POST.get('square'):
                pass
            elif request.POST.get('message') == 'next':
                pass
            elif request.POST.get('message') == 'back':
                pass
            elif request.POST.get('message') == 'ready':       
                pass
    else:                
        return render(request, 'introduction.html')

def start(request):
    return render(request, 'start.html')

def profile(request):
    return render(request, 'profile.html')

def leaderboards(request):
    return render(request, 'leaderboards.html')

def research(request):
    return render(request, 'research.html')



            
        
            