
from rdflib.namespace import FOAF, RDF
from rdflib import Graph

def printPersons():
    g = Graph()
    result = g.parse('out.turtle', format='turtle')
    g = Graph()
    count = 0
    result = g.parse('out.turtle', format='turtle')
    for s,p,o in g:
        if p == RDF.type:
            if o == FOAF.person:
                print(s)

def printPersonNames():
    g = Graph()
    result = g.parse('out.turtle', format='turtle')
    for s,p,o in g:
        if p == RDF.type:
            if o == FOAF.person:
                person = g.qname(s)
                __printPersonName(s)

def printPersonHomepages():
    g = Graph()
    result = g.parse('out.turtle', format='turtle')
    for s,p,o in g:
        if p == RDF.type:
            if o == FOAF.person:
                person = g.qname(s)
                __printPersonHomepage(s)

def __printPersonHomepage(subject):
    g = Graph()
    result = g.parse('out.turtle', format='turtle')
    for s,p,o in g:
        if s == subject:
            if p == FOAF.homepage:
                print(o)

def __printPersonName(subject):
    g = Graph()
    result = g.parse('out.turtle', format='turtle')
    for s,p,o in g:
        if s == subject:
            if p == FOAF.name:
                print(o)

def getPersonName(subject, graph):
    for s,p,o in graph:
        if s == subject:
            if p == FOAF.name:
                return o

def countPersons():
    g = Graph()
    count = 0
    result = g.parse('out.turtle', format='turtle')
    for s,p,o in g:
        if p == RDF.type:
            if o == FOAF.person:
                count+=1

    return count


def countStatements():
    g = Graph()
    result = g.parse('out.turtle', format='turtle')
    return len(g)
