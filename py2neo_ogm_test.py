from py2neo import Graph
from py2neo.ext.ogm import Store

"""
PROBLEM

OGM does not support Labels. . .

"""


class Person(object):

    def __init__(self, email=None, name=None, age=None):
        self.email = email
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

graph = Graph('http://127.0.0.1:7474/db/data/')
store = Store(graph)

alice = Person("ttmori@pbs.org", "Tobin", 34)
store.save_unique("People", "email", alice.email, alice)

bob = Person("bob@example.org", "Bob", 66)
carol = Person("carol@example.net", "Carol", 42)
jenny = Person("jenny@example.net", "Jenny", 43)
edgar = Person("edgar@example.net", "Edgar", 44)
mike = Person("mike@example.net", "Mike", 45)
store.relate(alice, "LIKES", bob)     # these relationships are not saved
store.relate(alice, "LIKES", carol)   # until `alice` is saved
store.relate(alice, "LIKES", jenny)   # until `alice` is saved
store.relate(alice, "LIKES", edgar)   # until `alice` is saved
store.relate(alice, "LIKES", mike)   # until `alice` is saved
store.save(alice)

friends = store.load_related(alice, "LIKES", Person)
print "Alice likes {0}".format(" and ".join(str(f) for f in friends))

'''MATCH (you )-[:LIKES]->(yourFriends)
RETURN you, yourFriends'''
