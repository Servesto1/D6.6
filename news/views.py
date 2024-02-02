from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .filetrs import PostFilter
from django.urls import reverse_lazy
from .forms import PostForm

class NewsList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = '-time_in'
    paginate_by = 10


class NewsDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class NewSearch(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'post_search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET,queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewsCreate(CreateView):
    permission_required='news.add_post'
    form_class = PostForm
    model = Post
    template_name = 'new_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == 'news/article/create/':
        post.article.news="AR"
        post.save()
        return super().form_valid(form)



 class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'new_edit.html'

class NewsDelete(DeleteView):
    model = Post
    template_name = 'new_delete.html'
    success_url = '/news/'