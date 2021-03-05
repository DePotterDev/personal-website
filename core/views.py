from django.shortcuts import render, redirect
import requests
from .forms import ContactForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import Blog


def home(request):
    """ 
    Home Page

    GET API GitHub
    1) repos per page = 5
    2) sorted by last updated
    """
    response = requests.get('https://api.github.com/users/depotterdev/repos?per_page=5&sort=updated')
    repo = response.json()

    """ Contact Form """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = request.POST['contact_name']
            from_email = request.POST['contact_email']
            message = request.POST['message']
            html_message = render_to_string('contact_template.txt', {'from_email': from_email, 'message': message, 'subject': subject})
            plain_message = strip_tags(html_message)
            try:
                send_mail('Message from : ' + subject, plain_message, from_email, ['email@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')

    context = {'repo': repo, 'range': range(4), 'form': ContactForm}
    return render(request, 'home.html', context)


def blog(request):
    """ Blog """
    blog = Blog.objects.order_by('-updated_at')
    # FILTER OPTIONS ON LANGUAGES
    python_count = Blog.objects.filter(language='python').count()
    javascript_count = Blog.objects.filter(language='javascript').count()
    react_count = Blog.objects.filter(language='react').count()
    django_count = Blog.objects.filter(language='django').count()
    other_count = Blog.objects.filter(language='other').count()
    python = Blog.objects.filter(language='python')
    javascript = Blog.objects.filter(language='javascript')
    react = Blog.objects.filter(language='react')
    django = Blog.objects.filter(language='django')
    other = Blog.objects.filter(language='other')

    latest = Blog.objects.order_by('-created_at')[:5]

    context = {
        'blogs': blog,
        'python': python,
        'javascript': javascript,
        'react': react,
        'django': django,
        'other': other,
        'pc': python_count,
        'jc': javascript_count,
        'rc': react_count,
        'dc': django_count,
        'oc': other_count,
        'latest': latest
        }
    return render(request, 'blog.html', context)


def blog_language(request, language):
    """ Filter blog posts on language """
    blog = Blog.objects.filter(language=language)
    current_language = language
    # FILTER OPTIONS ON LANGUAGES
    python_count = Blog.objects.filter(language='python').count()
    javascript_count = Blog.objects.filter(language='javascript').count()
    react_count = Blog.objects.filter(language='react').count()
    django_count = Blog.objects.filter(language='django').count()
    other_count = Blog.objects.filter(language='other').count()
    python = Blog.objects.filter(language='python')
    javascript = Blog.objects.filter(language='javascript')
    react = Blog.objects.filter(language='react')
    django = Blog.objects.filter(language='django')
    other = Blog.objects.filter(language='other')

    latest = Blog.objects.order_by('-created_at')[:5]

    context = {
        'language': current_language,
        'blogs': blog,
        'python': python,
        'javascript': javascript,
        'react': react,
        'django': django,
        'other': other,
        'pc': python_count,
        'jc': javascript_count,
        'rc': react_count,
        'dc': django_count,
        'oc': other_count,
        'latest': latest
        }
    return render(request, 'blog-language.html', context)


def blog_post(request, slug):
    """ Blog Post """
    post = Blog.objects.get(slug=slug)

    # FILTER OPTIONS ON LANGUAGES
    python_count = Blog.objects.filter(language='python').count()
    javascript_count = Blog.objects.filter(language='javascript').count()
    react_count = Blog.objects.filter(language='react').count()
    django_count = Blog.objects.filter(language='django').count()
    other_count = Blog.objects.filter(language='other').count()
    python = Blog.objects.filter(language='python')
    javascript = Blog.objects.filter(language='javascript')
    react = Blog.objects.filter(language='react')
    django = Blog.objects.filter(language='django')
    other = Blog.objects.filter(language='other')

    latest = Blog.objects.order_by('-created_at')[:5]

    context = {
        'post': post,
        'python': python,
        'javascript': javascript,
        'react': react,
        'django': django,
        'other': other,
        'pc': python_count,
        'jc': javascript_count,
        'rc': react_count,
        'dc': django_count,
        'oc': other_count,
        'latest': latest
        }
    return render(request, 'blog-post.html', context)

