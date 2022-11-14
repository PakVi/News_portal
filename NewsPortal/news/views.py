from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .filters import PostFilter
from django.shortcuts import render
from .forms import PostForm
from django.urls import reverse, reverse_lazy



# Create your views here.
# def default(request):
#     posts=Post.objects.all()
#     return render(request, 'default.html', context={'posts':posts})

class PostsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context




class PostsDetail(DetailView):
    model = Post
    template_name = 'news_id.html'
    context_object_name = 'posts'





# def index(request):
#     search=Post.objects.all()
#     return render(request, 'search.html', context={'search':search})

class SearchList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'search.html'
    context_object_name = 'posts'
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context



def create_post(request):
    if request.method == "POST":
        form =PostForm(request.POST)
        form.save()

    form = PostForm()
    return render(request, 'create.html', {'form':form})




class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['pk']})

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')



