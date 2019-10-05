from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseForbidden
from django.utils.text import slugify



from account.models import Profile
from blog.models import Post, Comment, Reaction
from blog.forms import PostCreationForm, EditPostForm, CommentForm, ReactForm

def home(request):
    template_name = 'blog/home.html'
    posts = Post.objects.filter(publish_status='publish')
    now = datetime.datetime.now()
    context = { 'posts': posts, 'now': now }
    return render(request, template_name, context)

def authors(request):
    template_name = 'blog/authors.html'
    authors = User.objects.all()
    context = { 'authors': authors }
    return render(request, template_name, context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            # obj.slug = slugify(obj.post_title)
            obj.save()
            messages.success(request, f'Post Creation Successful.')
            if obj.publish_status=='publish':
                return redirect('published_post', username=request.user.username)
            else:
                return redirect('saved_post', username=request.user.username)


    else:
        form = PostCreationForm()
    template_name = 'blog/createPost.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)

def published_post(request, username):
    obj = User.objects.get(username=username)
    id = obj.id
    banner = obj.profile.blog_banner
    posts = Post.objects.filter(user=id).filter(publish_status='publish')
    template_name = 'blog/publishedPost.html'
    now = datetime.datetime.now()
    context = { 
        'posts': posts, 
        'now': now,
        'author': obj,
        'banner': banner 
        }
    return render(request, template_name, context)

@login_required
def saved_post(request, username):
    if request.user.username == username:
        obj = User.objects.get(username=username)
        id = obj.id
        username = username
        banner = obj.profile.blog_banner
        posts = Post.objects.filter(user=id).filter(publish_status='draft')
        template_name = 'blog/savedPost.html'
        now = datetime.datetime.now()
        context = { 
            'author': obj,
            'posts': posts, 
            'now': now,
            'username': username,
            'banner': banner 
        }
        return render(request, template_name, context)
    else:
        return HttpResponseForbidden()

def post_detail(request,username,slug):
    id = User.objects.get(username=username).id
    post = Post.objects.filter(user=id).filter(slug=slug)
    post = post[0]
    now = datetime.datetime.now()
    comments = Comment.objects.filter(post=post.id)
    template_name = 'blog/postDetail.html'

    try:
        reactinstance = Reaction.objects.get(post=post)
    except:
        reactinstance = None

    if request.method == 'POST':
        if reactinstance:
            r_form = ReactForm(request.POST, instance=reactinstance)
        else:
            r_form = ReactForm(request.POST)
    
        c_form = CommentForm(request.POST)

        if r_form.is_valid():
            react = r_form.cleaned_data['react']

            try:
                r_inst = Reaction.objects.filter(post=post).filter(user=request.user)
            
            except:
                r_inst = None

            if r_inst:
                Reaction.objects.filter(user=request.user).filter(post=post).update(react=react)
            else:
                Reaction.objects.create(react=react, post=post, user=request.user)

            return redirect('post_detail', username=username, slug=post.slug)

        if c_form.is_valid():
            obj = c_form.save(commit=False)
            obj.post = post
            obj.user = request.user
            obj.save()
            messages.success(request, f'Successfully commented.')
            
            return redirect('post_detail', username=username, slug=post.slug)

    else:
        if reactinstance:
            r_form = ReactForm( instance=reactinstance)
        else:
            r_form = ReactForm()
        c_form = CommentForm()
    


    react_instance = Reaction.objects.filter(post=post)
    likes = react_instance.filter(react='like').count()
    dislikes = react_instance.filter(react='dislike').count()
    noreacts= react_instance.filter(react='noreact').count()

    # likes = react_instance.total_like()
    # dislikes = react_instance.total_dislikes()
    # noreacts = react_instance.total_no_react()

    context = { 
        'post': post, 
        'now': now , 
        'comments': comments, 
        'c_form': c_form, 
        'r_form': r_form,
        'likes': likes,
        'dislikes': dislikes,
        'noreacts': noreacts
        }
    return render(request, template_name, context)

@login_required
def edit_post(request,username,slug):
    if request.user.username == username:
        post_instance = Post.objects.get(slug=slug)
        if request.method=='POST':
            form = EditPostForm(request.POST,
                                request.FILES,
                                instance=post_instance)
            if form.is_valid():
                form.save()
                slug=post_instance.slug
                messages.success(request, f"Post updated successfully")
                return redirect('post_detail', username=username, slug=slug)

        else:
            form = EditPostForm(instance=post_instance)

    else:
        return HttpResponseForbidden()

    template_name='blog/editPost.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)

@login_required
def delete_post(request, username, slug):
    if request.user.username == username:
        id = User.objects.get(username=username).id
        post = Post.objects.filter(user=id).filter(slug=slug)
        post = post[0]
        template_name='blog/deletePost.html'
        context = { 'post_title': post.post_title }
        if request.method == 'POST':
            post.delete()
            messages.success(request, f'Your Post has been deleted.')
            return redirect('home')
        return render(request, template_name, context)
    else:
        return HttpResponseForbidden()

