from django.shortcuts import render, get_object_or_404
from requests import post
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_like'))
    post.likeCount.add(request.user)
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))

    
class Home(ListView):
    model = Post 
    template_name = 'home.html'
    ordering = ['-id']

class Article(DetailView):
    model = Post
    template_name = 'article.html'

    def get_context_data(self, *args, **kwargs):

        context = super(Article, self).get_context_data()
        like = get_object_or_404(Post, id=self.kwargs['pk'])
        total_like = like.total_likes()
        context["total_likes"] = total_like
        return context

class AddPost(CreateView):
    model = Post
    template_name = 'addPost.html'
    fields = ('title', 'category', 'thumbnail', 'author', 'description', 'body')
 



class Edit(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['title', 'category', 'thumbnail',  'description', 'body']

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.id} )

class DeleteBlog(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url =reverse_lazy("home")