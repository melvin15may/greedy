from django.shortcuts import render, redirect, get_object_or_404
from models import Bookmark
from forms import BookmarkForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from django.contrib.auth.models import User

# Create your views here.

def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    context = {'bookmarks': bookmarks}
    return render(request, 'game/bookmark_list.html', context)

def bookmark_user(request, username):
	user = get_object_or_404(User, username=username)
	if request.user == user:
		bookmarks = user.bookmarks.all()
	context = {'bookmarks': bookmarks, 'owner': user}
	return render(request, 'game/bookmark_user.html', context)

def bookmark_search(request):
	key=request.GET.get('key', '')
	bookmarks = Bookmark.objects.all().filter(title=key) | Bookmark.objects.all().filter(tags__name=key)
	bookmarks = bookmarks.distinct() 
	context = {'bookmarks': bookmarks}
	return render(request, 'game/bookmark_search.html', context)

@login_required
def bookmark_create(request):
	if request.method == 'POST':
		form = BookmarkForm(data=request.POST)
		if form.is_valid():
			form.save(owner=request.user)
			return redirect('game_bookmark_user', username=request.user.username)
	else:
		form = BookmarkForm()
	return render(request, 'game/form.html', {'form': form, 'create': True})

@login_required
def bookmark_edit(request, pk):
	bookmark = get_object_or_404(Bookmark, pk=pk)
	if bookmark.owner != request.user and not request.user.is_superuser:
		raise PermissionDenied
	if request.method == 'POST':
		form = BookmarkForm(instance=bookmark, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('game_bookmark_user', username=request.user.username)
	else:
		form = BookmarkForm(instance=bookmark)
	return render(request, 'game/form.html', {'form': form, 'create': False, 'bookmark': bookmark})