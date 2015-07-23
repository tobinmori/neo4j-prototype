from bulbs.neo4jserver import Graph, Config, NEO4J_URI
config = Config("http://127.0.0.1:7474/db/data/", "", "")
g = Graph(config)

james = g.vertices.create(name="James")
