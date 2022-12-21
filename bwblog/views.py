from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, ContactForm
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView
from django.template.loader import render_to_string


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
        messages.add_message(request, messages.INFO, 'You have leaved a comment!')
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            parent_id = comment_form.cleaned_data['parent']
            if parent_id:
                comment.parent = Comment.objects.get(id=parent_id)
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

    def get_success_url(self):  # Got help with this function from tutor 'Ger' from code institute
        return reverse('post_detail', kwargs={'slug': self.object.post.slug})

    def get(self, request, slug, *args, **kwargs):
        return render(
            request,
            "edit_comment.html",
            {
                "comment_form": CommentForm()
            },
        )

    def put(self, request, pk, slug, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        comment_form = CommentForm(data=request.POST)
        if comment.name == request.user.username:
            if comment_form.is_valid():
                comment.save()
            else:
                comment_form = CommentForm()
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
   

def send_email(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            messages.add_message(request, messages.SUCCESS, 'Your email is now sent!')
            html = render_to_string('send_email_form.html', {
                'name': name,
                'email': email,
                'content': content,
            })

            send_mail(
                'Subject here',
                'Here is the message.',
                'albin@betterproduction.se',
                ['albin-hall1@hotmail.com'], html_message=html
                )           
            return redirect('send_email')
        else:
            form = ContactForm()
            messages.add_message(request, messages.ERROR, 'Enter a valid name!')



    return render(request, 'send_email.html', {
        'form': form
    })
    