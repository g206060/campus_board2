from django import forms
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import ListView

from .models import Board, Post

from .forms import PostCreateForm


class IndexView(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 3
    
    # get_context_data関数をオーバーライド
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        # 2つ目のモデルを指定
        ctx["board"] = Board.objects.all()
        ctx['search_form'] = PostSearchForm(self.request.GET)
        return ctx
        
    queryset = Post.objects.order_by(
        '-started_at'
    )
    
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        if self.request.GET.get('board'):
            queryset = queryset.filter(
                board=self.request.GET.get('board')
            )
            
        return queryset
        
class PostSearchForm(forms.Form):
    board = forms.fields.ChoiceField(
        label='掲示板',
        choices=(
            ('', '未設定'),
            ('1', '教務課'),
            ('2', '学生課'),
            ('3', '学生支援担当'),
            ('4', 'アルバイト'),
            ('5', '学友会'),
            ('6', '就職課'),
        ),
        required=False,
        widget=forms.widgets.Select
    )
    
class KyoumuView(generic.ListView):
    model = Post
    template_name = 'board_kyoumu.html'
    paginate_by = 3
    
    # get_context_data関数をオーバーライド
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        # 2つ目のモデルを指定
        ctx["board"] = Board.objects.all()
        ctx['search_form'] = PostSearchForm(self.request.GET)
        return ctx

    queryset = Post.objects.filter(
        board=1
    )

class ArubaitoView(generic.ListView):
    model = Post
    template_name = 'board_arubaito.html'
    paginate_by = 3
    
    # get_context_data関数をオーバーライド
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        # 2つ目のモデルを指定
        ctx["board"] = Board.objects.all()
        ctx['search_form'] = PostSearchForm(self.request.GET)
        return ctx

    queryset = Post.objects.filter(
        board=4
    )
    

class DetailView(generic.DetailView):
    model = Post
    slug_field = "post_title"
    slug_url_kwarg = "post_title"
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
    
class PostCreateView(generic.CreateView):
    model = Post
    template_name = "post_create.html"
    form_class = PostCreateForm
    success_url = reverse_lazy('board:index')
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)
        
    def form_invalid(self, form):
        return super().form_invalid(form)
    
class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostCreateForm
    
    def get_success_url(self):
        return reverse_lazy('board:post_detail', kwargs={'pk': self.kwargs['pk']})
        
    def form_valid(self, form):
        # messeges.success(self.request, '掲示を更新しました。')
        return super().form_valid(form)
        
    def form_invalid(self, form):
        # messeges.error(self.request, '掲示の更新に失敗しました。')
        return super().form_invalid(form)

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('board:index')
    
    def delete(self, request, *args, **kwargs):
        # messages.success(self.request, '掲示を削除しました。')
        return super().delete(request, *args, **kwargs)