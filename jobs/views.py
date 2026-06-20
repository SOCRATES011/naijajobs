from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import JobForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def homepage(request):
    featured = Job.objects.filter(is_active=True).order_by('-date_posted')[:6]
    return render(request, 'jobs/homepage.html', {'featured': featured})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import JobForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

def job_list(request):
    q = request.GET.get('q', '')
    category = request.GET.get('category', 'All')
    jobs = Job.objects.filter(is_active=True)
    if q:
        jobs = jobs.filter(Q(title__icontains=q) | Q(company__icontains=q))
    if category and category != 'All':
        jobs = jobs.filter(category=category)
    paginator = Paginator(jobs, 9)
    page = request.GET.get('page')
    jobs_page = paginator.get_page(page)

    # Pass a categories list to the template
    categories = ['All', 'Tech', 'Design', 'Marketing', 'Finance', 'Legal']

    context = {
        'jobs': jobs_page,
        'q': q,
        'category': category,
        'categories': categories,
    }
    return render(request, 'jobs/job_list.html', context)


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.owner = request.user
            job.save()
            messages.success(request, 'Job posted successfully.')
            return redirect('jobs:my_listings')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form})

@login_required
def my_listings(request):
    jobs = Job.objects.filter(owner=request.user)
    return render(request, 'jobs/my_listings.html', {'jobs': jobs})

def about(request):
    return render(request, 'jobs/about.html')

# Authentication views
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('jobs:homepage')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'jobs/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('jobs:homepage')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'jobs/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('jobs:homepage')
