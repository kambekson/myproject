from django.shortcuts import render

def register_view(request):
    return render (request,'users/register.html') 

def post_page(request, slug):
    post = post.objects.get(slug=slug)
    return render (request,'posts/post_page.html', {'post': post}) 
