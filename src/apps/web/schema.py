import graphene

from graphene_django.types import DjangoObjectType

# Filter Graph
from graphene_django.filter import DjangoFilterConnectionField
from . import models


class MensajeType(DjangoObjectType):
    class Meta:
        model = models.Mensaje
        filter_fields = {'mensaje': ['icontains']}
        interfaces = (graphene.relay.Node, )


class Query(graphene.AbstractType):
    all_messages = DjangoFilterConnectionField(MensajeType)
