from django.db import models
from django.contrib.auth.models import User

from rest_framework import serializers


class News(models.Model):
    class Meta:
        verbose_name_plural = "News"
    
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=254)
    message = models.TextField()
    image = models.ImageField(upload_to="img/news", max_length=254, blank=True, null=True)
    author = models.ForeignKey(User)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title + self.date.strftime(" (%d/%m/%Y %H:%M)")

    def save(self, *args, **kwargs):
        add_image = False
        if self.image:
            if not self.pk:
                add_image = True
            else:
                orig = News.objects.get(pk=self.pk)
                if orig.image != self.image:
                    orig.image.delete()
                    add_image = True
        else:
            if self.pk:
                orig = News.objects.get(pk=self.pk)
                self.image = orig.image

        if add_image:
            extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", self.image.name) 
            self.image.name = text.slugify(self.title) + "." + extension

        super(News, self).save(*args, **kwargs)

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News

    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())