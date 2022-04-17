from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import PostForm
from django.views import generic

# Create your views here.
from .models import Post


# ---------------------------------------POST_LIST_VIEW---------------------------------------#
# ----------------------------------------functional----------------------------------------#
# def post_list_view(request):
#     # posts_list = Post.objects.all()
#     posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html', {'posts_list': posts_list})

# ----------------------------------------class_based----------------------------------------#
class PostListView(generic.ListView):
    # model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


# ===================================================================================================


# ---------------------------------------POST_DETAIL_VIEW---------------------------------------#
# ----------------------------------------functional----------------------------------------#
# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except ObjectDoesNotExist:
#     #     post = None
#     #     print('excepted')
#     return render(request, 'blog/post_detail.html', {'post': post})

# ----------------------------------------class_based----------------------------------------#
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# ===================================================================================================


# ---------------------------------------POST_CREATE_VIEW---------------------------------------#
# ----------------------------------------functional----------------------------------------#

# def post_create_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_create.html', {'form': form})

# if request.method == 'POST':
#     user=User.objects.all()[0]
#     title = request.POST.get('title')
#     text = request.POST.get('text')
#     Post.objects.create(
#         title=title,
#         text=text,
#         author=user,
#         status='pub',
#     )
# else:
#     print('GET request')
# return render(request, 'blog/post_create.html')


# ----------------------------------------class_based----------------------------------------#

class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'


# ===================================================================================================
# ---------------------------------------POST_UPDATE_VIEW---------------------------------------#
# ----------------------------------------functional----------------------------------------#
#
# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         print('hello')
#         form.save()
#         return redirect('posts_list')
#     return render(request, 'blog/post_create.html', {'form': form})

# ----------------------------------------class_based----------------------------------------#


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'


# ===================================================================================================
# ---------------------------------------POST_DELETE_VIEW---------------------------------------#
# ----------------------------------------functional----------------------------------------#
def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts_list')

    return render(request, 'blog/post_delete.html', {'post': post})


# ----------------------------------------class_based----------------------------------------#
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')

