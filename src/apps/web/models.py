from django.db import models
from filebrowser.fields import FileBrowseField
from ckeditor.fields import RichTextField

# Create your models here.

class ModelExample(models.Model):

    img_example = FileBrowseField('Imagen Label',
                                max_length=200, blank=True,
                                extensions=['.jpg', '.png', '.gif'],
                                directory='img_example')

    rich_example = RichTextField("Example", blank=True)

    class Meta:
        verbose_name = "Model Exmaple"
        verbose_name_plural = "Model Examples"

    def __unicode__(self):
        return u"Model Example"


class Mensaje(models.Model):
    user = models.ForeignKey('auth.User', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    mensaje = RichTextField("Mensaje")
    activo = models.BooleanField(default=False)

