from django.shortcuts import render, redirect
import requests
from .forms import ContactForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

def home(request):
    """ Home Page """

    """ GET API GitHub """
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