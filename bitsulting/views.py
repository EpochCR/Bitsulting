from django.shortcuts import render_to_response, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from bitsulting.models import Question, Response, Category
from django.template import RequestContext
from django.contrib.auth.models import User
from bitsulting.forms import ResponseForm

import datetime
def view_home(request):
    return render(request, 'home.html', {'question': Question.objects.all()[:10]})

def view_question(request, slug):
    context = RequestContext(request)
        # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        response_form = ResponseForm(data=request.POST)

        # If the two forms are valid...
        if response_form.is_valid():
            # Save the user's form data to the database.
            response = response_form.save()
            response.save()

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print response_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        response_form = ResponseForm()

    return render_to_response(
            'view_question.html',
            {
                'question': get_object_or_404(Question, slug=slug),
                'response': Response.objects.all().filter(question=get_object_or_404(Question, slug=slug)),
                'response_form': response_form,
            },
            context)


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'view_category.html', {
        'category': category,
        'question': Question.objects.filter(category=category)[:10]
    })

def new_home(request):
        # Like before, get the request's context.
    context = RequestContext(request)
    return render(request, 'home.html', {'question': Question.objects.all()[:12]})