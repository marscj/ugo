from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.core.files.uploadedfile import UploadedFile

from middleware.viewsets import CustomModelViewSet
from .models import Category, Product, ProductVariant
from .serializers import CategorySerializer, ProductSerializer, ProductVariantSerializer

class CategoryView(CustomModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ProductView(CustomModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().cache()
 
class ProductVariantView(CustomModelViewSet):
    serializer_class = ProductVariantSerializer
    queryset = ProductVariant.objects.all().cache()

class ImageLoader(APIView):

    def post(self, request, *args, **kwargs):
        log.info('received POST to main multiuploader view')
        if request.FILES == None:
            return Response('Must have files attached!', status=400)

        #getting file data for farther manipulations
        file = request.FILES[u'files[]']
        wrapped_file = UploadedFile(file)
        filename = wrapped_file.name
        file_size = wrapped_file.file.size
        log.info ('Got file: "'+str(filename)+'"')

        #writing file manually into model
        #because we don't need form of any type.
        image = Image()
        image.title=str(filename)
        image.image=file
        image.save()
        log.info('File saving done')

        #getting url for photo deletion
        file_delete_url = '/delete/'
        
        #getting file url here
        file_url = '/'

        #getting thumbnail url using sorl-thumbnail
        # im = get_thumbnail(image, "80x80", quality=50)
        # thumb_url = im.url
        
        result = {
            "name":filename, 
            "size":file_size, 
            "url":file_url, 
        #    "thumbnail_url":thumb_url,
            "delete_url":file_delete_url+str(image.pk)+'/', 
            "delete_type":"POST",
        }
        return Response(response_data)