from py2neo import Node, Relationship, Graph, watch

watch("httpstream")
graph = Graph('http://127.0.0.1:7474/db/data/')
alice = Node("Person", name="Alice")
bob = Node("Person", name="Bob")
alice_knows_bob = Relationship(alice, "KNOWS", bob)
graph.create(alice_knows_bob)

#x = graph.find_one("Person",property_key="Alice")
#print x
#y= x.next()

