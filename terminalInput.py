from rdflib.namespace import FOAF, RDF
from rdflib import Graph, Literal, URIRef
import readFoaf

def createPerson(g):
    print();
    print("Create a person");
    name = input("Insert a name:")
    subject = URIRef("http://example.org/people/" + name)
    g.add((subject, RDF.type, FOAF.person))
    literal = Literal(name)
    g.add((subject, FOAF.name, literal))
    print()
    print("¡Person created!")
    print()

def createProject(g):
    print();
    print("Create a project");
    name = input("Insert a project name:")
    subject = URIRef("http://example.org/projects/" + name)
    g.add((subject, RDF.type, FOAF.project))
    print()
    print("¡Proyect created!")
    print()

def createRelation(g):
    print();
    print("Create a relation");
    i = 0
    persons = []
    for s,p,o in g:
        if p == RDF.type:
            if o == FOAF.person:
                name = readFoaf.getPersonName(s,g)
                if name != None:
                    print(str(i+1)+")" + name)
                    persons.insert(i,name)
                i += 1
    personIndex = input("Select a person:")
    person1 =  persons[int(personIndex)-1]
    persons[int(personIndex)-1] = ""
    print();
    i = 1
    print("Remaining persons:")
    for person in persons:
        if person != "":
            print(str(i) + ")" + person)
            i += 1
    personIndex2 = input("Select a person:")
    if int(personIndex2) < int(personIndex):
        person2 = persons[int(personIndex2)-1]
    else:
        person2 = persons[int(personIndex2)]

    subj = URIRef("http://example.org/people/" + person1)
    obj = URIRef("http://example.org/people/" + person2)
    g.add((subj, FOAF.knows, obj))
    print()
    print("¡Relation created!")
    print()

g = Graph()
print("--------- Individual Insertion ---------");
print("1) Person");
print("2) Project");
print("3) Relation");
print("0) Exit");
print();
opt = input("Select an option:")
while opt != "0":
    if opt == "1":
        createPerson(g)
    if opt == "2":
        createProject(g)
    if opt == "3":
        createRelation(g)
    print();
    print("--------- Individual Insertion ---------");
    print("1) Person");
    print("2) Project");
    print("3) Relation");
    print("0) Exit");
    print();
    opt = input("Select an option:")
g.serialize(destination='termina_test_out.turtle', format='turtle')



