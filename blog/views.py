from django.shortcuts import render

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# import forms

# from braces.views import (
#     AjaxResponseMixin,
#     JSONResponseMixin,
#     LoginRequiredMixin,
#     SuperuserRequiredMixin,
#     )

from .models import Post

class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_createview.html"
    fields = ('titel', 'text')
    success_url = reverse_lazy('list')

class PostListView(ListView):
    model = Post
    template_name = "blog/post_listview.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detailview.html"
    

class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_updateview.html"
    fields = ('titel', 'text')
    success_url = reverse_lazy('list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_deleteview.html"
    success_url = reverse_lazy('list')

def index(request):
    object_list = Post.objects.all()
    recent = object_list
    return render(request, "blog/post_listview.html", {'object_list':object_list, 'recent':recent})

# def test(request):
#     post = Post.object.get(pk=request.DATA)  # post.pk
#     comment_list = Comment.objects.get(post=post.pk)
#     comment_form = forms.CommentForm() # new instance the CommentForm
#     return render(request, 'blog/post_detailview.html', {'post':post, 'comment_list':comment_list, 'comment_form':comment_form})

# Todo: import form


# class AjaxPhotoUploadView(LoginRequiredMixin,
#                     SuperuserRequiredMixin,
#                     JSONResponseMixin,
#                     AjaxResponseMixin,
#                     CreateView):
#     """
#     View for uploading photos via AJAX.
#     """
#     def post_ajax(self, request, *args, **kwargs):
#         try:
#             album = Album.objects.get(pk=kwargs.get('pk'))
#         except Album.DoesNotExist:
#             error_dict = {'message': 'Album not found.'}
#             return self.render_json_response(error_dict, status=404)

#         uploaded_file = request.FILES['file']
#         Photo.objects.create(album=album, file=uploaded_file)

#         response_dict = {
#             'message': 'File uploaded successfully!',
#         }

#         return self.render_json_response(response_dict, status=200)
