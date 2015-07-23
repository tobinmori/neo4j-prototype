from bulbs.neo4jserver import Graph, Config, NEO4J_URI
import pdb

pdb.set_trace()
print NEO4J_URI
config = Config('http://neo4j:password@127.0.0.1:7474/db/data/', "neo4j", "password")
g = Graph(config)


james = g.vertices.create(name="James")
#julie = g.vertices.create(name="Julie")
james.save()
#julie.save()
#g.edges.create(james, "knows", julie)
