from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .admin import EventsAdmin
from .forms import PostForm, CommentForm, ReportForm, ContactForm, ReplyForm, EditProfileForm
from .models import Post, Comments, Reports, Events, SupportGroups, Resources, BlogPost
from django.contrib.admin.views.decorators import staff_member_required
import random

# Create your views here.
#1. views for resources
import random
from django.shortcuts import render
from .models import Post  # Ensure your Post model is correctly imported

def community_forum(request):
    # Sample quotes for inspiration
    quotes = [
        "Together we can make a difference.",
        "Speak out to change the world.",
        "Empowered communities bring change.",
        "Advocacy is the heart of transformation.",
        "Every voice matters in the fight against FGM.",
    ]

    # Sample advocacy tips
    advocacy_tips = [
        "Educate yourself about FGM and its impact.",
        "Engage with community leaders for support.",
        "Encourage dialogue and awareness campaigns.",
        "Be a voice of change in your community.",
        "Support survivors by connecting them to resources.",
    ]

    # Select a random quote to display
    random_quote = random.choice(quotes)

    # Fetch all posts to display in the forum
    posts = Post.objects.all().order_by('-created_at')  # Assuming Post has a 'created_at' field for sorting

    # Context to pass to the template
    context = {
        'random_quote': random_quote,
        'advocacy_tips': advocacy_tips,
        'posts': posts,
    }

    return render(request, 'web/forum.html', context)



def resource_detail(request, resource_id):
    resource = get_object_or_404(Resources, id=resource_id)
    return render(request, 'accounts/resource_detail.html', {'resource': resource})

def thank_you(request):
    return render(request, 'web/thank_you.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('community_forum')
    else:
        form = PostForm()
    return render(request, 'web/create_post.html', {'form': form})

@login_required
def reply_to_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.post = post
            reply.save()
            return redirect('community_forum')
    else:
        form = ReplyForm()
    return render(request, 'web/reply_to_post.html', {'form': form, 'post': post})


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = post.comments.all().order_by('-created_at')
    return render(request, 'web/post_detail.html', {'post': post, 'comments': comments})

def forum_home(request):
    posts = Post.objects.all()
    recent_posts = Post.objects.order_by('-created_at')[:5]  # Last 5 posts
    return render(request, 'forum/home.html', {'posts': posts, 'recent_posts': recent_posts})


#2. views for Comments
@login_required
def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'web/add_comment.html', {'form': form, 'post': post})

@login_required
def profile_view(request):
    # You can pass the user data to the template
    return render(request, 'web/profile.html', {'user': request.user})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'web/edit_profile.html', {'form': form})


# 3. views for ReportForm
@login_required
def submit_report(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "web/submit_report.html", {"success": True, "form": ReportForm()})
    else:
        form = ReportForm()
    return render(request, "web/submit_report.html", {"form": form})

#4. views for events
def events_view(request):
    events = Events.objects.all()
    return render(request, 'accounts/events.html', {'events': events})

#5. views for support_groups
def support_view(request):
    support_groups = SupportGroups.objects.all()
    return render(request, 'accounts/groups.html', {'support_groups': support_groups})

#6. views for Resources
def resources_view(request):
    resources = Resources.objects.all()
    return render(request, 'accounts/resources.html', {'resources': resources})

#4. VIEWS FOR EVENTS, SUPPORT GROUPS AND RESOURCES
def dashboard(request):
    events = Events.objects.all()
    support_groups = SupportGroups.objects.all()
    resources = Resources.objects.all()

    context = {'events': events, 'support_groups': support_groups, 'resources': resources}
    return render(request, 'accounts/dashboard.html', context)

#7. views for blogposts
def blog_view(request):
    blogs = BlogPost.objects.all()
    return render(request, 'accounts/blog/blogpost.html', {'blogs': blogs})

@staff_member_required()
def view_reports(request):
    reports = Reports.objects.all()
    return render(request, 'web/view_reports.html', {'reports': reports})

def home(request):
    return render(request, 'web/landing/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully')
            return redirect('contact')
        else:
            messages.error(request, 'please fill in the correct details')

    else:
        form = ContactForm()
    return render(request, 'accounts/contact.html', {'form': form})

def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(content__icontains=query)
    return render(request, 'forum/search.html', {'results': results})
