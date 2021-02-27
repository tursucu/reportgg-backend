import graphene
from typing import Union
from kogmaw import LeagueEntries, Queue, Summoner, Region, Patch, Tier, Division, Season, Champions, MatchHistory, Match


class LeagueExp(graphene.Mutation):
    class Arguments:
        queue = graphene.String()
        region = graphene.String()
        division = graphene.String()
        tier = graphene.String()
        id = graphene.Int()

    status = graphene.Boolean()

    @classmethod
    def mutate(root, _, cls, region: Union[Region, str] = None, division: Union[Division, str] = None,
               tier: Union[Tier, str] = None, queue: Union[Queue, str] = None, id: int = None):
        summoner = Summoner(name="reportgg", region="EUW")
        print(summoner.account_id)
        match = Match(id=id, region=region)
        print(match.duration)
        """ if queue is None:
            entries_list = LeagueEntries(queue=Queue.ranked_solo_fives, region=region, tier=tier, division=division)
        else:
            entries_list = LeagueEntries(queue=queue, region=region, tier=tier, division=division)

        for entries in entries_list:
            print("Mutation Sorgu Name:", entries.summoner.name)
            match =MatchHistory(summoner=entries.summoner, queues={Queue.ranked_solo_fives})"""

        status = True

        return LeagueExp(status=status)
