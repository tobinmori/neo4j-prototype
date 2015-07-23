from py2neo import Graph
from py2neo.ext.ogm import Store

from models import Series, Episode, Organization, Actor

graph = Graph('http://neo4j:password@127.0.0.1:7474/db/data/')
store = Store(graph)

series = ["Downton Abbey", "Daniel Tiger", ]


downton = Series(name="Downton Abbey")

episode1 = Episode(name="Ep1")

episode2 = Episode(name="Ep2")


bbc = Organization(name="BBC")

hbo = Organization(name="HBO")


actor1 = Actor(name="Bob")
actor2 = Actor(name="Mary")
actor3 = Actor(name="Mark")

store.relate(downton, "HAS_EPISODE", episode1)
store.relate(downton, "HAS_EPISODE", episode2)
store.relate(downton, "PRODUCED_BY", bbc)
store.relate(downton, "DISTRIBUTED_BY", hbo)
store.relate(downton, "ACTED_IN", actor1)
store.relate(downton, "ACTED_IN", actor2)
store.relate(downton, "ACTED_IN", actor3)

store.save(downton)
