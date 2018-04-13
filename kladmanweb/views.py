from django.shortcuts import render
from kladmanweb.models import GeoTag, KladMan
import uuid
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# from kladmanweb.textprocessor import create_img


@csrf_exempt
def process_data(request):
    if request.POST:
        ahash = str(uuid.uuid4().hex)
        # create_img(request.POST.get('title'), ahash)
        GeoTag.objects.update_or_create(
            title=request.POST.get('title'),
            kladman=request.POST.get('kladman'),
            longitude=request.POST['longitude'],
            latitude=request.POST['latitude'],
            height=request.POST.get('height'),
            hash=ahash
        )
        return JsonResponse({'url': 'https://asergey.me/kladman/data/?hash={}'.format(ahash)})

    elif request.GET:
        ahash = request.GET.get('hash')
        if ahash:
            geotag = GeoTag.objects.filter(hash=ahash).first()
            if geotag:
                return JsonResponse(
                    {'latitude': geotag.latitude, 'longitude': geotag.longitude, 'height': geotag.height,
                     'title': geotag.title})
    return HttpResponse(status=400)
