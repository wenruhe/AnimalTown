from db.neo import neo4j_connection
from animals.animals import Animal
from db.appConfigs import settings
from db.userConfigs import user_credentials
from errors.animalError import *

class Relationships:
    driver = neo4j_connection
    database = settings.NEO4J_DATABASE_NAME

    def add_animal(cls, animal:Animal) -> None: 
        query = (
            "CREATE (a:Animal { userID: $userID, animalID: $animalID, name: $name, age: $age, gender: $gender, job: $job, personality: $personality }) "
        )
        with cls.driver.session() as session:
            session.run(
                query, userID=user_credentials.USERID, animalID=str(animal.animalID), name=animal.name, age=animal.age, gender=animal.gender, job=animal.job, personality=animal.personality,
                database_=cls.database
            )

    def init_relationship(cls, animal1:Animal, animal2:Animal) -> None:
        query = (
            "MATCH (a1: Animal { userID: $userID, animalID: $animalID1 }), (a2: Animal { userID: $userID, animalID: $animalID2 })"
            "CREATE (a1)-[:Friend { value:0 }] -> (a2)"
            "CREATE (a1)-[:Romance { value:0 }] -> (a2)"
            "CREATE (a1)-[:Commerce { value:0 }] -> (a2)"

            "CREATE (a2)-[:Friend { value:0 }] -> (a1)"
            "CREATE (a2)-[:Romance { value:0 }] -> (a1)"
            "CREATE (a2)-[:Commerce { value:0 }] -> (a1)"
        )
        with cls.driver.session() as session:
            session.run(
                query, userID=user_credentials.USERID, animalID1=str(animal1.animalID), animalID2=str(animal2.animalID),
            )


    def update_relationship_unidirectional(cls, animal1:Animal, animal2:Animal, rs:dict) -> None:
        check_query = (
            f"MATCH (a1: Animal {{ userID: $userID, animalID: $animalID1 }})-[r:Friend]->(a2: Animal {{ userID: $userID, animalID: $animalID2 }}) "
            "RETURN r"
        )

        with cls.driver.session() as session:
            result = session.run(
                check_query, userID=user_credentials.USERID, animalID1=str(animal1.animalID), animalID2=str(animal2.animalID)
            )
            relationships_exist = result.single()

            if not relationships_exist:
                # >>>>>>这个需要商议是raise error还是直接修改<<<<<<<<
                raise AnimalsNotKnowEachOtherError(f"{animal1.name} and {animal2.name} do not know each other!")
                cls.init_relationship(animal1, animal2)

            for r in rs.items():
                update_query = (
                    f"MATCH (a1: Animal {{ userID: $userID, animalID: $animalID1 }})-[r:{r[0]}]->(a2: Animal {{ userID: $userID, animalID: $animalID2 }})"
                    "SET r.value = $new_value"
                )
                session.run(update_query, userID=user_credentials.USERID, animalID1=str(animal1.animalID), animalID2=str(animal2.animalID), new_value=r[1])


    def update_relationship_bidirectional(cls, animal1:Animal, animal2:Animal, r:tuple) -> None:
        cls.update_relationship_unidirectional(animal1, animal2, r)
        cls.update_relationship_unidirectional(animal2, animal1, r)
    
