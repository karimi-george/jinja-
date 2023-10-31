from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def blog(request):
    return render(request, 'blog.html')
def blogdetails(request):
    return render(request, 'blog-details.html')
def portfoliodetails(request):
    return render(request, 'portfolio-details.html')
def servicesdetails(request):
    return render(request, 'services-details.html')


