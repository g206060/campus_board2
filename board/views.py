from django import forms
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Board, Post, GradeTag, DepartmentTag, TypeTag, CustomUser

from .forms import PostCreateForm


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 6
    
    # get_context_data関数をオーバーライド
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        # 2つ目のモデルを指定
        ctx["board"] = Board.objects.all()
        ctx["gradetags"] = GradeTag.objects.all()
        ctx["departmenttags"] = DepartmentTag.objects.all()
        ctx["typetags"] = TypeTag.objects.all()
        ctx['search_form'] = PostSearchFormTop(self.request.GET)
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
        if self.request.GET.get('gradetags'):
            queryset = queryset.filter(
                gradetags=self.request.GET.get('gradetags')
            )
        if self.request.GET.get('departmenttags'):
            queryset = queryset.filter(
                departmenttags=self.request.GET.get('departmenttags')
            )
        if self.request.GET.get('typetags'):
            queryset = queryset.filter(
                typetags=self.request.GET.get('typetags')
            )
            
        return queryset
        
class PostSearchFormTop(forms.Form):
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
    gradetags = forms.fields.ChoiceField(
        label='学年',
        choices=(
            ('', '未設定'),
            ('1', '1学年'),
            ('2', '2学年'),
            ('3', '3学年'),
            ('4', '4学年'),
        ),
        required=False,
        widget=forms.widgets.Select
    )
    departmenttags = forms.fields.ChoiceField(
        label='学科',
        choices=(
            ('', '未設定'),
            ('1', '機械工学コース'),
            ('2', '電気電子通信工学コース'),
            ('3', 'システム情報工学コース'),
            ('4', '生命環境科学コース'),
            ('5', '建築・土木工学コース'),
            ('6', '感性デザイン学科'),
            ('7', '大学院'),
        ),
        required=False,
        widget=forms.widgets.Select
    )
    typetags = forms.fields.ChoiceField(
        label='種別',
        choices=(
            ('', '未設定'),
            ('', '--全般--'),
            ('1', '連絡事項'),
            ('', '--アルバイト--'),
            ('2', '長期'),
            ('3', '短期'),
        ),
        required=False,
        widget=forms.widgets.Select
    )
    
class KyoumuView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'board_kyoumu.html'
    paginate_by = 6
    
    # get_context_data関数をオーバーライド
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        # 2つ目のモデルを指定
        ctx["board"] = Board.objects.all()
        ctx["gradetags"] = GradeTag.objects.all()
        ctx["departmenttags"] = DepartmentTag.objects.all()
        ctx["typetags"] = TypeTag.objects.all()
        ctx['search_form'] = PostSearchFormDetail(self.request.GET)
        return ctx

    queryset = Post.objects.filter(board=1).order_by('-started_at')
    
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        if self.request.GET.get('gradetags'):
            queryset = queryset.filter(
                gradetags=self.request.GET.get('gradetags')
            )
        if self.request.GET.get('departmenttags'):
            queryset = queryset.filter(
                departmenttags=self.request.GET.get('departmenttags')
            )
        if self.request.GET.get('typetags'):
            queryset = queryset.filter(
                typetags=self.request.GET.get('typetags')
            )
            
        return queryset
        
class PostSearchFormDetail(forms.Form):
    gradetags = forms.fields.ChoiceField(
        label='学年',
        choices=(
            ('', '未設定'),
            ('1', '1学年'),
            ('2', '2学年'),
            ('3', '3学年'),
            ('4', '4学年'),
        ),
        required=False,
        widget=forms.widgets.Select
    )
    departmenttags = forms.fields.ChoiceField(
        label='学科',
        choices=(
            ('', '未設定'),
            ('1', '機械工学コース'),
            ('2', '電気電子通信工学コース'),
            ('3', 'システム情報工学コース'),
            ('4', '生命環境科学コース'),
            ('5', '建築・土木工学コース'),
            ('6', '感性デザイン学科'),
            ('7', '大学院'),
        ),
        required=False,
        widget=forms.widgets.Select
    )
    typetags = forms.fields.ChoiceField(
        label='種別',
        choices=(
            ('', '未設定'),
            ('', '--全般--'),
            ('1', '連絡事項'),
            ('', '--アルバイト--'),
            ('2', '長期'),
            ('3', '短期'),
        ),
        required=False,
        widget=forms.widgets.Select
    )

class GakuseiView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'board_gakusei.html'
    paginate_by = 6
    
    # get_context_data関数をオーバーライド
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        # 2つ目のモデルを指定
        ctx["board"] = Board.objects.all()
        ctx["gradetags"] = GradeTag.objects.all()
        ctx["departmenttags"] = DepartmentTag.objects.all()
        ctx["typetags"] = TypeTag.objects.all()
        ctx['search_form'] = PostSearchFormDetail(self.request.GET)
        return ctx

    queryset = Post.objects.filter(board=2).order_by('-started_at')
    
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        if self.request.GET.get('gradetags'):
            queryset = queryset.filter(
                gradetags=self.request.GET.get('gradetags')
            )
        if self.request.GET.get('departmenttags'):
            queryset = queryset.filter(
                departmenttags=self.request.GET.get('departmenttags')
            )
        if self.request.GET.get('typetags'):
            queryset = queryset.filter(
                typetags=self.request.GET.get('typetags')
            )
            
        return queryset

class ShienView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'board_shien.html'
    paginate_by = 6
    
    # get_context_data関数をオーバーライド
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        # 2つ目のモデルを指定
        ctx["board"] = Board.objects.all()
        ctx["gradetags"] = GradeTag.objects.all()
        ctx["departmenttags"] = DepartmentTag.objects.all()
        ctx["typetags"] = TypeTag.objects.all()
        ctx['search_form'] = PostSearchFormDetail(self.request.GET)
        return ctx

    queryset = Post.objects.filter(board=3).order_by('-started_at')
    
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        if self.request.GET.get('gradetags'):
            queryset = queryset.filter(
                gradetags=self.request.GET.get('gradetags')
            )
        if self.request.GET.get('departmenttags'):
            queryset = queryset.filter(
                departmenttags=self.request.GET.get('departmenttags')
            )
        if self.request.GET.get('typetags'):
            queryset = queryset.filter(
                typetags=self.request.GET.get('typetags')
            )
            
        return queryset

class ArubaitoView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'board_arubaito.html'
    paginate_by = 6
    
    # get_context_data関数をオーバーライド
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        # 2つ目のモデルを指定
        ctx["board"] = Board.objects.all()
        ctx["gradetags"] = GradeTag.objects.all()
        ctx["departmenttags"] = DepartmentTag.objects.all()
        ctx["typetags"] = TypeTag.objects.all()
        ctx['search_form'] = PostSearchFormDetail(self.request.GET)
        return ctx

    queryset = Post.objects.filter(board=4).order_by('-started_at')
    
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        if self.request.GET.get('gradetags'):
            queryset = queryset.filter(
                gradetags=self.request.GET.get('gradetags')
            )
        if self.request.GET.get('departmenttags'):
            queryset = queryset.filter(
                departmenttags=self.request.GET.get('departmenttags')
            )
        if self.request.GET.get('typetags'):
            queryset = queryset.filter(
                typetags=self.request.GET.get('typetags')
            )
            
        return queryset

class GakuyuView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'board_gakuyu.html'
    paginate_by = 6
    
    # get_context_data関数をオーバーライド
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        # 2つ目のモデルを指定
        ctx["board"] = Board.objects.all()
        ctx["gradetags"] = GradeTag.objects.all()
        ctx["departmenttags"] = DepartmentTag.objects.all()
        ctx["typetags"] = TypeTag.objects.all()
        ctx['search_form'] = PostSearchFormDetail(self.request.GET)
        return ctx

    queryset = Post.objects.filter(board=5).order_by('-started_at')
    
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        if self.request.GET.get('gradetags'):
            queryset = queryset.filter(
                gradetags=self.request.GET.get('gradetags')
            )
        if self.request.GET.get('departmenttags'):
            queryset = queryset.filter(
                departmenttags=self.request.GET.get('departmenttags')
            )
        if self.request.GET.get('typetags'):
            queryset = queryset.filter(
                typetags=self.request.GET.get('typetags')
            )
            
        return queryset

class JobView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'board_job.html'
    paginate_by = 6
    
    # get_context_data関数をオーバーライド
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        # 2つ目のモデルを指定
        ctx["board"] = Board.objects.all()
        ctx["gradetags"] = GradeTag.objects.all()
        ctx["departmenttags"] = DepartmentTag.objects.all()
        ctx["typetags"] = TypeTag.objects.all()
        ctx['search_form'] = PostSearchFormDetail(self.request.GET)
        return ctx

    queryset = Post.objects.filter(board=6).order_by('-started_at')
    
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        if self.request.GET.get('gradetags'):
            queryset = queryset.filter(
                gradetags=self.request.GET.get('gradetags')
            )
        if self.request.GET.get('departmenttags'):
            queryset = queryset.filter(
                departmenttags=self.request.GET.get('departmenttags')
            )
        if self.request.GET.get('typetags'):
            queryset = queryset.filter(
                typetags=self.request.GET.get('typetags')
            )
            
        return queryset

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    slug_field = "post_title"
    slug_url_kwarg = "post_title"
    
class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "post_detail.html"
    
class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "post_create.html"
    form_class = PostCreateForm
    success_url = reverse_lazy('board:post_create')
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.user_name = self.request.user
        post.save()
        messages.success(self.request, "掲示が作成されました。")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, "掲示の作成に失敗しました。")
        return super().form_invalid(form)
    
class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostCreateForm
    
    def get_success_url(self):
        return reverse_lazy('board:post_detail', kwargs={'pk': self.kwargs['pk']})
        
    def form_valid(self, form):
        messages.success(self.request, "掲示を更新しました。")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, "掲示の更新に失敗しました。")
        return super().form_invalid(form)

class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('board:index')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "掲示を削除しました。")
        return super().delete(request, *args, **kwargs)
        
class MypageView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'mypage.html'
    paginate_by = 6
    
    # get_context_data関数をオーバーライド
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        # 2つ目のモデルを指定
        ctx["board"] = Board.objects.all()
        ctx["gradetags"] = GradeTag.objects.all()
        ctx["departmenttags"] = DepartmentTag.objects.all()
        ctx["typetags"] = TypeTag.objects.all()
        ctx['search_form'] = PostSearchFormTop(self.request.GET)
        return ctx
        
    queryset = Post.objects.order_by(
        '-started_at'
    )
    
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        current_user = self.request.user.username
        user_data = CustomUser.objects.get(username=current_user)
        if user_data:
            queryset = Post.objects.filter(user_name=user_data).all()
            queryset = queryset.order_by('-started_at')
        if self.request.GET.get('board'):
            queryset = queryset.filter(
                board=self.request.GET.get('board')
            )
        if self.request.GET.get('gradetags'):
            queryset = queryset.filter(
                gradetags=self.request.GET.get('gradetags')
            )
        if self.request.GET.get('departmenttags'):
            queryset = queryset.filter(
                departmenttags=self.request.GET.get('departmenttags')
            )
        if self.request.GET.get('typetags'):
            queryset = queryset.filter(
                typetags=self.request.GET.get('typetags')
            )
            
        return queryset
    