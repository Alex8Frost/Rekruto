from django.shortcuts import render

# Create your views here.
def input_text(request):
    return render(request, 'index.html')

def print_text(request):
    name = request.GET['name']
    message = request.GET['message']
    context = {'name': name, 'message': message}
    return render(request, 'hello.html', context)
