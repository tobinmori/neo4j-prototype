# neo4j-python-prototype

This is a prototype of python clients using neo4j.

There are a few possible approaches to writing a python client:

bulbs
neo4jrestclient
py2neo

In my experience, at the time of this writing - they all had limitations. E.g. py2neo's ogm doesn't support labels.

The restclient is full featured. . .but slow. 

If one is serious about speed you'd probably use a JVM lang and the gremlin query language. 

