from db.neo import neo4jConnector
from animals import Animal
from db.configs import settings
from typing import Literal

class Relationships:
    driver = neo4jConnector
    database = settings.NEO4J_DATABASE

    def add_animal(cls, animal:Animal) -> None: 
        query = (
            "CREATE (a:Animal { _id: $id, name: $name, age: $age, gender: $gender, job: $job, personality: $personality }) "
        )
        with cls.driver.session() as session:
            session.run(
                query, id=str(animal._id), name=animal.name, age=animal.age, gender=animal.gender, job=animal.job, personality=animal.personality,
                database_=cls.database
            )
            

    def init_relationship(cls, animal1:Animal, animal2:Animal) -> None:
        query = (
            "MATCH (a1: Animal { _id: $id1 }), (a2: Animal { _id: $id2 })"
            "CREATE (a1)-[:Friend { value:0 }] -> (a2)"
            "CREATE (a1)-[:Romance { value:0 }] -> (a2)"
            "CREATE (a1)-[:Commerce { value:0 }] -> (a2)"

            "CREATE (a2)-[:Friend { value:0 }] -> (a1)"
            "CREATE (a2)-[:Romance { value:0 }] -> (a1)"
            "CREATE (a2)-[:Commerce { value:0 }] -> (a1)"
        )
        with cls.driver.session() as session:
            session.run(
                query, id1=str(animal1._id), id2=str(animal2._id)
            )


    def update_relationship_unidirectional(cls, animal1:Animal, animal2:Animal, rs:dict) -> None:
        check_query = (
            f"MATCH (a1: Animal {{ _id: $id1 }})-[r:Friend]->(a2: Animal {{ _id: $id2 }}) "
            "RETURN r"
        )

        with cls.driver.session() as session:
            result = session.run(
                check_query, id1=str(animal1._id), id2=str(animal2._id)
            )
            relationships_exist = result.single()

            if not relationships_exist:
                print(f"{animal1.name} and {animal2.name} do not know each other!")
                cls.init_relationship(animal1, animal2)

            for r in rs.items():
                update_query = (
                    f"MATCH (a1: Animal {{ _id: $id1 }})-[r:{r[0]}]->(a2: Animal {{ _id: $id2 }})"
                    "SET r.value = $new_value"
                )
                session.run(update_query, id1=str(animal1._id), id2=str(animal2._id), new_value=r[1])


    def update_relationship_bidirectional(cls, animal1:Animal, animal2:Animal, r:tuple) -> None:
        cls.update_relationship_unidirectional(animal1, animal2, r)
        cls.update_relationship_unidirectional(animal2, animal1, r)
    
    
if __name__ == "__main__":
    relationships = Relationships()
    darry = Animal(name="Darry", age=23, gender="Male", job="Shopkeeper", personality=["Shy"])
    luna = Animal(name="Luna", age=26, gender="Female", job="Doctor", personality=["Independent", "Smart"])
    relationships.add_animal(darry)
    relationships.add_animal(luna)
    relationships.update_relationship_bidirectional(darry, luna, {"Romance": 20, "Friend":100})
    relationships.driver.close()
