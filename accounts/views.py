from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect('blog:index')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
