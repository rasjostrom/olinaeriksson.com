from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

from .models import Photo

# Create your views here.

class PhotoListView(ListView):
    model = Photo
    paginate_by = 16
    template_name = "gallery/photo_listview.html"


class PhotoCreateView(CreateView):
    model = Photo
    template_name = "gallery/photo_createview.html"
    fields = ['img', 'text']
    success_url = reverse_lazy('photo-list')
