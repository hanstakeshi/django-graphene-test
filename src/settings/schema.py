import graphene

import apps.web.schema

class Mutation(apps.web.schema.Mutation, graphene.ObjectType):
    pass

class Query(
    apps.web.schema.Query,
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

