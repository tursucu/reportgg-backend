from flask import Flask
from flask_graphql import GraphQLView
from mongoengine import connect
from schema import schema
from kogmaw import get_default_config, apply_settings
from kogmaw.core.staticdata.champion import Champion, Champions
from kogmaw.core.staticdata.rune import Rune, Runes
from kogmaw.core.staticdata.item import Item, Items
from kogmaw.core.staticdata.summonerspell import SummonerSpell, SummonerSpells
from kogmaw.core.staticdata.map import Map, Maps
from kogmaw.core.staticdata.realm import Realms
from kogmaw.core.staticdata.profileicon import ProfileIcon, ProfileIcons
from kogmaw.core.staticdata.language import Locales
from kogmaw.core.staticdata.languagestrings import LanguageStrings
from kogmaw.core.staticdata.version import Versions
from kogmaw.core.championmastery import ChampionMastery, ChampionMasteries
from kogmaw.core.league import LeagueSummonerEntries, League, ChallengerLeague, GrandmasterLeague, MasterLeague
from kogmaw.core.match import Match, Timeline
from kogmaw.core.summoner import Summoner
from kogmaw.core.status import ShardStatus
from kogmaw.core.spectator import CurrentMatch, FeaturedMatches
from kogmaw.core.champion import ChampionRotationData
import datetime

DB_URI = "mongodb+srv://report:report@cluster0.hl5ji.mongodb.net/reportgg?retryWrites=true&w=majority"

app = Flask(__name__)
app.debug = False

config = get_default_config()

config["pipeline"] = {
    "Cache": {
        "expirations": {ChampionRotationData: datetime.timedelta(hours=6),
                        Realms: datetime.timedelta(hours=6),
                        Versions: datetime.timedelta(hours=6),
                        Champion: datetime.timedelta(days=20),
                        Rune: datetime.timedelta(days=20),
                        Item: datetime.timedelta(days=20),
                        SummonerSpell: datetime.timedelta(days=20),
                        Map: datetime.timedelta(days=20),
                        ProfileIcon: datetime.timedelta(days=20),
                        Locales: datetime.timedelta(days=20),
                        LanguageStrings: datetime.timedelta(days=20),
                        SummonerSpells: datetime.timedelta(days=20),
                        Items: datetime.timedelta(days=20),
                        Champions: datetime.timedelta(days=20),
                        Runes: datetime.timedelta(days=20),
                        Maps: datetime.timedelta(days=20),
                        ProfileIcons: datetime.timedelta(days=20),
                        ChampionMastery: datetime.timedelta(days=7),
                        ChampionMasteries: datetime.timedelta(days=7),
                        LeagueSummonerEntries: datetime.timedelta(hours=6),
                        League: datetime.timedelta(hours=6),
                        ChallengerLeague: datetime.timedelta(hours=6),
                        GrandmasterLeague: datetime.timedelta(hours=6),
                        MasterLeague: datetime.timedelta(hours=6),
                        Match: datetime.timedelta(days=3),
                        Timeline: datetime.timedelta(days=1),
                        Summoner: datetime.timedelta(minutes=0.1),
                        ShardStatus: datetime.timedelta(hours=1),
                        CurrentMatch: datetime.timedelta(hours=0.5),
                        FeaturedMatches: datetime.timedelta(hours=0.5), }
    },
    "Mongo": {
        "package": "mongo-datastore"
    },
    "DDragon": {},
    "RiotAPI": {
        "api_key": "RGAPI-0fa59054-724e-463b-b67d-20e9e09b52e2"
    }
}
config["logging"] = {
    "print_calls": True,
    "print_riot_api_key": True,
    "default": "WARNING",
    "core": "WARNING"
}

apply_settings(config)
connect(host=DB_URI)

app.add_url_rule(
    '/api',
    view_func=GraphQLView.as_view('api', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run()
