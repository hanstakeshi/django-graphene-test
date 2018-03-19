import graphene

from graphene_django.types import DjangoObjectType

# Filter Graph
from graphene_django.filter import DjangoFilterConnectionField
from . import models
import json


# @@@ Consulta Simple @@@
class MensajeType(DjangoObjectType):
    class Meta:
        model = models.Mensaje
    """
    Syntaxis:

    {
      allMessages{
        mensaje, id
      }
    }
    """
# Este bloque va directo a la clase Query


# @@@ Consulta filtrada @@@
class MensajeTypeFilter(DjangoObjectType):
    class Meta:
        model = models.Mensaje
        filter_fields = {'mensaje': ['icontains']}
        interfaces = (graphene.relay.Node, )
    """
    Syntaxis:

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

# @@@ Mutation @@@
# Simple
class CrearMensaje(graphene.Mutation):
    class Arguments:
        mensaje = graphene.String()

    form_errors = graphene.String()
    mensaje = graphene.Field(lambda: MensajeType)

    @staticmethod
    # Parameters for 2.0 graphene-django
    def mutate(self, info, mensaje):
        resultado = models.Mensaje.objects.create(mensaje=mensaje)
        return CrearMensaje(mensaje=resultado, form_errors="Creado correctamente")



# Dictionary
class MensajeInput(graphene.InputObjectType):
    mensaje = graphene.String()
    activo = graphene.Boolean()

class CrearMensajeDict(graphene.Mutation):
    class Arguments:
        datos_mensaje = MensajeInput()

    mensaje = graphene.Field(MensajeType)

    @staticmethod
    def mutate(self, info, datos_mensaje=None):
        mensaje = models.Mensaje.objects.create(mensaje=datos_mensaje.mensaje,
                                                activo=datos_mensaje.activo)
        return CrearMensajeDict(mensaje=mensaje)

    """
    Syntaxis
    mutation{
        crearMensajeDict(datosMensaje:{mensaje:"prueba17", activo:false}){
        mensaje{
            id, mensaje, creationDate, activo
            }
        }
    }
    """


class Mutation(graphene.AbstractType):
    crear_mensaje = CrearMensaje.Field()
    crear_mensaje_dict = CrearMensajeDict.Field()
    """
    Syntaxis:

    mutation{
      crearMensaje(mensaje:"texto"){
        mensaje{
          id, creation_date, etc
        }
      }
    }
    """

# @@@ Query @@@
class Query(graphene.AbstractType):
    filter_messages = DjangoFilterConnectionField(MensajeTypeFilter)
    all_messages = graphene.List(MensajeType)

    def resolve_all_messages(self, args):
        return models.Mensaje.objects.all()