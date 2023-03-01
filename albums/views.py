from django.shortcuts import render, redirect
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
