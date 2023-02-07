from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment, CommentDisc, Discussion
from .forms import CommentForm, ContactForm, DiscussionForm, CommentFormDisc
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView
from django.template.loader import render_to_string
from django.db.models import Q
from django.core.paginator import Paginator


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


def discussion_list(request):
    q = request.GET.get('q')
    discussions = Discussion.objects.all().order_by('-date_created')
    if q:
        discussions = Discussion.objects.filter(Q(title__icontains=q) | Q(description__icontains=q)).order_by('-date_created')
    
    paginator = Paginator(discussions, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'discussion_list.html', {'page_obj': page_obj})


def discussion_detail(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    comments = discussion.comments.all()
    if request.method == 'POST':
        form = CommentFormDisc(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.discussion = discussion
            comment.author = request.user
            parent_id = request.POST.get('parent_id')
            if parent_id:
                comment.parent = CommentDisc.objects.get(id=parent_id)
            comment.save()
            return redirect('discussion_detail', pk=discussion.pk)
    else:
        form = CommentFormDisc()
    return render(request, 'discussion_detail.html', {'discussion': discussion, 'comments': comments, 'form': form})


def discussion_create(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.author = request.user
            discussion.save()
            return redirect('discussion_detail', pk=discussion.pk)
    else:
        form = DiscussionForm()
    return render(request, 'discussion_create.html', {'form': form})

def delete_comment(request, pk):
    comment = get_object_or_404(CommentDisc, pk=pk)
    if request.user == comment.author:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.WARNING, 'You can only delete your own comment!')


    return redirect('discussion_detail', pk=comment.discussion.pk)

def edit_comment(request, pk):
    comment = get_object_or_404(CommentDisc, pk=pk)
    if request.user != comment.author:
        return redirect('discussion_detail', pk=comment.discussion.pk)
    if request.method == 'POST':
        form = CommentFormDisc(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your comment has been successfully edited.')
            return redirect('discussion_detail', pk=comment.discussion.pk)
    else:
        form = CommentFormDisc(instance=comment)
    return render(request, 'edit_comment_disc.html', {'form': form})

