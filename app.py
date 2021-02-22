from flask import Flask
from flask_graphql import GraphQLView
from mongoengine import connect
from schema import schema
from kogmaw import get_default_config, apply_settings

DB_URI = "mongodb+srv://report:report@cluster0.hl5ji.mongodb.net/reportgg?retryWrites=true&w=majority"

app = Flask(__name__)
app.debug = True

config = get_default_config()

config["pipeline"] = {
    "Cache": {},
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
