import graphene

from graphene_django.types import DjangoObjectType

# Filter Graph
from graphene_django.filter import DjangoFilterConnectionField
from . import models


# Consulta Simple
class MensajeType(DjangoObjectType):
    class Meta:
        model = models.Mensaje
    """
    {
      allMessages{
        mensaje, id
      }
    }
    """

# Consulta filtrada
class MensajeTypeFilter(DjangoObjectType):
    class Meta:
        model = models.Mensaje
        filter_fields = {'mensaje': ['icontains']}
        interfaces = (graphene.relay.Node, )
    """
    {
      filterMessages(mensaje_Icontains:"1"){
        edges{
          node{
            id, mensaje
          }
        }
      }
    }

    """

class Query(graphene.AbstractType):
    filter_messages = DjangoFilterConnectionField(MensajeTypeFilter)
    all_messages = graphene.List(MensajeType)

    def resolve_all_messages(self, args):
        return models.Mensaje.objects.all()