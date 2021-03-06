from django.http import HttpResponse,request
from django.contrib.auth import authenticate,login,get_user_model
from django.shortcuts import render,redirect
from .forms import ContactForm

def home_page(request):

    print(request.session.get("first_name","unknows")) #get
    context = {
        "title" : " The Face ",
        "content" : "eShopOnline",
    }
    #neu dang nhap vao thi se hien
    if request.user.is_authenticated:
        context["premium_content"] = "YEAHHHH"
    return render(request, "home_page.html",context)

def about_page(request):
    context = {
        "title": "about world",
    }
    return render(request, "home_page.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title" : "contact world",
        "content" : "day la contact",
        "form"    : contact_form,
        # dan sang view.html
        "brand" : "new Brand name",
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method=="POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    return render(request, "contact/view.html",context)



def home_page_old(request):
    html_ = """
    <!doctype html>
    <html lang="en">
      <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">
    
        <title>Hello, world!</title>
      </head>
      <body>
        <div class='text-center'>
        <h1>Hello, world!</h1>
        </div>
    
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js" integrity="sha384-a5N7Y/aK3qNeh15eJKGWxsqtnX/wWdSZSKp+81YjTmS15nvnvxKHuzaWwXHDli+4" crossorigin="anonymous"></script>
      </body>
    </html>
    """
    return HttpResponse(html_)