from django.shortcuts import render
#dev_4
def main_page(request):
    return render(request, 'main.html')


