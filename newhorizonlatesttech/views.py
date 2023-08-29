from django.http import HttpResponse
from . import views
from django.shortcuts import render



def home(request):
    return render(request,'home.html')


def index(request):
    return render(request,'index.html')

# def index(request):    
#     Atext=request.GET.get('text','default')
#     rpu=request.GET.get('rpu','off') 
#     print(rpu)
#     print(Atext)
#     if rpu == "on" :  
#         punctuations = ''' ?  , : ,   ; ,% ^ <<,,,>>>..!!!| “ ”, _ - ( ), { },[ ] , @ ,*, \\\::"""'  ~ , / , , #,$, &  ''' 
#         analyzed=""
#         for I in Atext:
#             if I not in punctuations:
#                analyzed=analyzed+I 
#         data={'rpu': rpu , 'btext': analyzed }         
#         return render(request,'index.html',data)
#     else:
#         return HttpResponse(" sab ghalat kar diya khaotay tou hay hi AQAL say paidal ")     
    
    
    
   







# And here is my views.py file for the User folder:



# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# from django.contrib.auth.decorators import login_required


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your Account has been created you are now able to log in {username}!')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your Account has been updated!')
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
    
#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }
    
#     return render(request, 'users/profile.html', context)