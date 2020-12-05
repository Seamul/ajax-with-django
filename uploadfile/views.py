from django.shortcuts import render,HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import logging

log = logging.getLogger(__name__)


class OverwriteStorage(FileSystemStorage):
    
    def get_available_name(self, name, max_length=None):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


# Create your views here.
def uploadFile(request):
    if request.method=="POST":
        weather_data_file = request.FILES.get('weather_data')
        print(weather_data_file.name)

        ext_weather_data = os.path.splitext(str(weather_data_file))[1]

        fs = OverwriteStorage(location=settings.MEDIA_ROOT)
        filename = fs.save(f'raw_weather_train{ext_weather_data}', weather_data_file)


    return render(request,'index.html')