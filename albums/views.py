from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm

# Create your views here.


def list_albums(request):
    albums = Album.objects.all()
    # goes to the DB and gets all instances of
    # the model Album (django ORM) = a query
    return render(request, 'albums/index.html', {'albums': albums})
    # pass data to the template using the context dictionary {'albums': albums}


def add_album(request):
    if request.method == 'POST':
        new_album = AlbumForm(request.POST)
        if new_album.is_valid():
            new_album.save()
            return redirect('home')
    form = AlbumForm()
    return render(request, 'albums/add_album.html', {'form': form})


def album_details(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_details.html', {'album': album})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        edited_album = AlbumForm(request.POST, instance=album)
        if edited_album.is_valid():
            edited_album.save()
            return redirect('home')
        form = AlbumForm(instance=album)
        return render(request, 'albums/edit_album.html', {'form': form, 'pk': pk})


def remove_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
    return render(request, 'albums/remove_album.html')
