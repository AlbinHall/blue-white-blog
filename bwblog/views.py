from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        messages.add_message(request, messages.INFO, 'Successful Comment Request!')
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()
            
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# got help from Tutor at code institute with DeleteCommentView


class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'confirm_delete.html'

    def post(self, request, pk, slug, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.name == request.user.username:
            comment.delete()
            messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
        else:
            messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class UpdateCommentView(UpdateView):
    model = Comment
    template_name = 'edit_comment.html'
    fields = ("body", )

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")

        return render(
            request,
            "edit_comment.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, pk, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=pk)
        comment_form = CommentForm(data=request.POST)

        if comment.name == request.user.username:
            messages.add_message(request, messages.SUCCESS, 'You have now updated your comment!')
        else:
            messages.add_message(request, messages.ERROR, 'You can only upadte your own comment!')
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
