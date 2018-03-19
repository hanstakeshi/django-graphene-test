import graphene

import apps.web.schema


class Query(
	apps.web.schema.Query,
	graphene.ObjectType):
	pass

schema = graphene.Schema(query=Query)

