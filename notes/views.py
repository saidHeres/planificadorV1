from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from notes.models import Note

#Muestra notas
class HomePageView(ListView):
    template_name = "notes/home.html"
    model = Note


#Crear notas

class CreateNotaView(CreateView):
    template_name = "notes/nuevo.html"
    model = Note
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse_lazy('home')

    
#Actualizar notas

class UpdateNoteView(UpdateView):
    template_name = "notes/actualizar.html"
    model = Note
    fields = ['title', 'description']
    success_url = reverse_lazy('home')
    
#Eliminar Notas
    
class DeleteNoteView(DeleteView):
    template_name = 'notes/eliminar.html'
    model = Note
    success_url = reverse_lazy('home')