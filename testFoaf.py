import csv
import readFoaf
from rdflib.namespace import FOAF, RDF
from rdflib import Graph, Literal, URIRef

with open('Test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    g = Graph()
    for row in reader:
        subject = URIRef(row['Subject'])
        if row['Predicate'] == "type":
            if row['Object'] == "person":
                g.add((subject, RDF.type, FOAF.person))
        else:
            if row['Predicate'] == "name":
                name = Literal(row['Object'])
                g.add((subject, FOAF.name, name))
            if row['Predicate'] == "homepage":
                homepage = Literal(row['Object'])
                g.add((subject, FOAF.homepage,homepage))

g.serialize(destination='out.turtle', format='turtle')
readFoaf.printPersons()
readFoaf.printPersonNames()
readFoaf.printPersonHomepages()

