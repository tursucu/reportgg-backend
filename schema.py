from mutations import LeagueExp

import graphene


class Mutation(graphene.ObjectType):
    leagueExp = LeagueExp.Field()


class Query(graphene.ObjectType):
    none = graphene.String()


schema = graphene.Schema(query=Query, mutation=Mutation)
