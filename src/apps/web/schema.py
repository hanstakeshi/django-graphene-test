import graphene

from graphene_django.types import DjangoObjectType

# Filter Graph
from graphene_django.filter import DjangoFilterConnectionField
from . import models


# @@@ Consulta General @@@
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

    Al usar filter, tambien puedes usar los parametros 
    tales como first, last, before, after 
    query{
        filterMessages(first:4){
            edges{
                nodes{
                    id, mensaje
                    }
                }
            }
        }

    """

# @@@ Mutation @@@

# Simple Mutation
class CrearMensaje(graphene.Mutation):
    class Arguments:
        mensaje = graphene.String()

    form_errors = graphene.String()
    mensaje = graphene.Field(lambda: MensajeType)

    # Parameters for 2.0 graphene-django
    @staticmethod
    def mutate(self, info, mensaje):
        resultado = models.Mensaje.objects.create(mensaje=mensaje)
        return CrearMensaje(mensaje=resultado, form_errors="Creado correctamente")

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

# Dictionary Mutation
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

# Getting simple objects

# @@@ Core Mutation @@@
class Mutation(graphene.AbstractType):
    crear_mensaje = CrearMensaje.Field()
    crear_mensaje_dict = CrearMensajeDict.Field()


# @@@ Core Query @@@
class Query(graphene.AbstractType):

    # consulta general
    all_messages = graphene.List(MensajeType)

    # consulta filtrada
    def resolve_all_messages(self, args):
        return models.Mensaje.objects.all()

    # consulta simple con argumento
    mensaje = graphene.Field(MensajeType,
                             id=graphene.Int())

    def resolve_mensaje(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return models.Mensaje.objects.get(pk=id)
        return None

    filter_messages = DjangoFilterConnectionField(MensajeTypeFilter)
