from db.neo import neo4j_connection
from animals.animals import Animal
from db.appConfigs import settings
from db.userConfigs import user_credentials
from errors.animalError import *

class Relationships:
    driver = neo4j_connection
    database = settings.NEO4J_DATABASE_NAME

    def _load_all(cls) -> None:
        query = (
            "MATCH (a:Animal) RETURN a"
        )
        with cls.driver.session() as session:
            results = session.run(
                query, userID=user_credentials.USERID, database_=cls.database
            )
            for r in results:
                node = dict(r["a"])
                animal = Animal(**node)
                print(animal)
        pass

    def add_animal(cls, animal:Animal) -> None: 
        query = (
            "CREATE (a:Animal { userID: $userID, animalID: $animalID, name: $name, age: $age, gender: $gender, job: $job, personality: $personality, relations: $relations, self_perception: $self_perception, memory: $memory, profile: $profile }) "
        )
        with cls.driver.session() as session:
            session.run(
                query, 
                userID=user_credentials.USERID, 
                animalID=str(animal.animalID), 
                name=animal.name, 
                age=animal.age, 
                gender=animal.gender, 
                job=animal.job, 
                personality=animal.personality,
                relations=animal.relations,
                self_perception=animal.self_perception,
                memory=animal.memory,
                profile=animal.profile,
                database_=cls.database
            )

    def init_relationship(cls, animal1:Animal, animal2:Animal) -> None:
        query = (
            "MATCH (a1: Animal { userID: $userID, animalID: $animalID1 }), "
            "(a2: Animal { userID: $userID, animalID: $animalID2 }) "
            
            "CREATE (a1)-[:Friend { value: 0, note: '尚未建立友情' }] -> (a2) "
            "CREATE (a1)-[:Romance { value: 0, note: '尚未建立浪漫情感' }] -> (a2) "
            "CREATE (a1)-[:Commerce { value: 0, note: '尚未建立商业往来' }] -> (a2) "
            "CREATE (a1)-[:Blood { value: 0, note: '无血缘关系' }] -> (a2) "
            
            "CREATE (a2)-[:Friend { value: 0, note: '尚未建立友情' }] -> (a1) "
            "CREATE (a2)-[:Romance { value: 0, note: '尚未建立浪漫情感' }] -> (a1) "
            "CREATE (a2)-[:Commerce { value: 0, note: '尚未建立商业往来' }] -> (a1)"
            "CREATE (a1)-[:Blood { value: 0, note: '无血缘关系' }] -> (a2) "
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
                raise AnimalsNotKnowEachOtherError(f"{animal1.name} and {animal2.name} do not know each other!")

            for relation_type, content in rs.items():
                update_query = (
                    f"MATCH (a1: Animal {{ userID: $userID, animalID: $animalID1 }})"
                    f"-[r:{relation_type}]->"
                    f"(a2: Animal {{ userID: $userID, animalID: $animalID2 }}) "
                    "SET r.value = $new_value, r.note = $note"
                )
                session.run(
                    update_query,
                    userID=user_credentials.USERID,
                    animalID1=str(animal1.animalID),
                    animalID2=str(animal2.animalID),
                    new_value=content["value"],
                    note=content["note"]
                )
    
