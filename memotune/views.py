from django.shortcuts import render
from memotune.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    if request.method == 'POST':
        if request.is_ajax():
            points = request.POST.get('points')
            high_score = User.high_score
            if points > high_score:
                high_score = points
                User.save()
            elif request.POST.get('square'):
                pass
            elif request.POST.get('message') == 'next':
                pass
            elif request.POST.get('message') == 'back':
                pass

                return render(request, 'research.html')
    else:
        return render(request, 'introduction.html')

def start(request):
    return render(request, 'start.html')
        
def register(request):

    registered = False

    if request.method == 'POST':
        # attempt to get form information
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # Provide blank forms
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
    
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                return render(request, 'base.html', {"message" : "inactive"})
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'base.html', {"message" : "invalid"})
    else:
        return render(request, 'login.html', {})
        
def profile(request):        
    render(request, 'profile.html')
    
def leaderboards(request):
    if request.method == 'POST':
        score = request.POST.get('score')
    render(request, 'leaderboards.html')
        
def research(request):
    render(request, 'research.html')
            