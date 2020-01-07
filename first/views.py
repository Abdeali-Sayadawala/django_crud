from django.shortcuts import render, redirect
from first.models import Note
from first.forms import NoteForm

# Create your views here.
def read(request):
    note = Note.objects.all()
    return render(request, 'show.html', {'note' : note})

def create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/read")
    else:
        form = NoteForm()
    return render(request, 'form.html', {'form' : form})

def edit(request, id):
    note = Note.objects.get(id=id)
    return render(request, "edit.html", {'note' : note})

def update(request, id):
    note = Note.objects.get(id=id)
    form = NoteForm(request.POST, instance=note)
    if form.is_valid():
        form.save()
        return redirect("/read")
    return render(request, "edit.html", {'note' : note})

def destroy(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect("/read")
    