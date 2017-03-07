from django.contrib import admin

from xpassion_image.models import Image

from image_cropping import ImageCroppingMixin

class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Image, ImageAdmin)
