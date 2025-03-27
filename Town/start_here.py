from animals.relation import Relationships
from animals.animals import Animal

if __name__ == "__main__":
    relationships = Relationships()
    # darry = Animal(name="Darry", age=23, gender="Male", job="Shopkeeper", personality=["Shy"])
    # luna = Animal(name="Luna", age=26, gender="Female", job="Doctor", personality=["Independent", "Smart"])
    # relationships.add_animal(darry)
    # relationships.add_animal(luna)
    # relationships.init_relationship(darry, luna)
    # relationships.update_relationship_bidirectional(darry, luna, {"Romance": 20, "Friend":100})
    relationships._load_all()
    relationships.driver.close()