import graphene

from graphene_django.types import DjangoObjectType

from . import models


class MensajeType(DjangoObjectType):
    class Meta:
        model = models.Mensaje



class Query(graphene.AbstractType):
    all_messages = graphene.List(MensajeType)

    def resolve_all_messages(self, args):
        return models.Mensaje.objects.all()