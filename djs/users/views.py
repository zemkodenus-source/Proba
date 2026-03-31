from django.shortcuts import render, redirect
from .models import Users , coment
from .forms import commentForms
from django.views.generic import DetailView , UpdateView , DeleteView

def users_hub(request):
    users_comment = coment.objects.using('local_data').all()
    return render(request , 'users/comment.html' , {'users_comment' : users_comment})

def users_register(request):
    return render(request , 'users/register.html')

def users_list(request):
    users = Users.objects.using('default').all()
    return render(request , 'users/users_list.html' , {'users' : users})

class commentDetailView(DetailView):
    model = coment
    template_name = 'users/comment_view.html'
    context_object_name = 'comments'

class commentUpdateView(UpdateView):
    model = coment
    template_name = 'users/update_comment.html'

    form_class = commentForms

class commentDeleteView(DeleteView):
    model = coment
    template_name = 'users/delete_comment.html'
    success_url = '/users'


def add_comment(request):
    error = ''
    if request.method == 'POST':
        form = commentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_hub')
        else:
            error = 'Неправильно заповнено дані'

    form = commentForms

    data = {
        'form' : form ,
        'error' : error
    }
    return render(request , 'users/add_comment.html' , data)