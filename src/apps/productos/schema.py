import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Producto, Categoria, Subcategoria


class SubcategoriaNode(DjangoObjectType):

    class Meta:
        model = Subcategoria


class CategoriaNode(DjangoObjectType):

    class Meta:
        model = Categoria
        filter_fields = {'nombre': ['icontains']}
        interfaces = (graphene.relay.Node, )
    full_name = graphene.String()
    hijos = graphene.List(SubcategoriaNode)

    def resolve_full_name(instance, info, **kwargs):
        return " ".join([instance.nombre, instance.codigo])

    def resolve_hijos(instance, info, **kwargs):
        id = instance.id
        categoria = Categoria.objects.get(id=id)
        return Subcategoria.objects.filter(categoria=categoria)


class Query(graphene.AbstractType):
    categoria = graphene.Field(CategoriaNode, id=graphene.Int())
    todas_categorias = graphene.List(CategoriaNode)

    def resolve_todas_categorias(self, args):
        return Categoria.objects.all()

    def resolve_categoria(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Categoria.objects.get(pk=id)
        return None

    filtro_categorias = DjangoFilterConnectionField(CategoriaNode)

