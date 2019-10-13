from django.shortcuts import render, redirect
from .forms import CommentAddForm



# def addcomment(request):
#     if request.method == 'POST':
#         form = CommentAddForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user.userprofile
#             comment.post = request.post.id
#             comment.save()
#             return redirect(request.post)
#         else:
#             return render(request, 'blogengine/post.html', context={'form': form})
#     else:
#         return render(request, 'blogengine/post.html')


