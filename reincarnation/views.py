from django.shortcuts import render

def post_list(request):
    return render(request, 'reincarnation/post_list.html', {})
