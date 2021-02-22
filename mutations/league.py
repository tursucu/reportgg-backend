import graphene
from typing import Union
from kogmaw import LeagueEntries, Queue, Summoner, Region, Patch, Tier, Division, Season, Champions, MatchHistory


class LeagueExp(graphene.Mutation):
    class Arguments:
        queue = graphene.String()
        region = graphene.String(required=True)
        division = graphene.String(required=True)
        tier = graphene.String(required=True)

    status = graphene.Boolean()

    @classmethod
    def mutate(root, _, cls, region: Union[Region, str] = None, division: Union[Division, str] = None,
               tier: Union[Tier, str] = None, queue: Union[Queue, str] = None):
        if queue is None:
            entries_list = LeagueEntries(queue=Queue.ranked_solo_fives, region=region, tier=tier, division=division)
        else:
            entries_list = LeagueEntries(queue=queue, region=region, tier=tier, division=division)

        for entries in entries_list:
            print("Mutation Sorgu Name:", entries.summoner.name)
            match_history = MatchHistory(summoner=entries.summoner, queues={Queue.ranked_solo_fives})

        status = True

        return LeagueExp(status=status)
