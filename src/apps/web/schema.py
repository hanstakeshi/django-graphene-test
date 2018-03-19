import graphene

from graphene_django.types import DjangoObjectType

# Filter Graph
from graphene_django.filter import DjangoFilterConnectionField
from . import models
import json


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
# class MensajeTypeMutation(graphene.ObjectType):
#     mensaje = graphene.String()

# Mutation
class CrearMensaje(graphene.Mutation):
    class Input:
        mensaje = graphene.String()

    form_errors = graphene.String()
    mensaje = graphene.Field(lambda: MensajeType)

    def mutate(self, args, mensaje):
        resultado = models.Mensaje.objects.create(mensaje=mensaje)
        return CrearMensaje(mensaje=resultado, form_errors=None)

class Mutation(graphene.AbstractType):
    crear_mensaje = CrearMensaje.Field()


class Query(graphene.AbstractType):
    filter_messages = DjangoFilterConnectionField(MensajeTypeFilter)
    all_messages = graphene.List(MensajeType)

    def resolve_all_messages(self, args):
        return models.Mensaje.objects.all()