from animals.relation import Relationships
from animals.animals import Animal
import sys
print(sys.path)
if __name__ == "__main__":
    relationships = Relationships()
    darry = Animal(
        name="Darry", 
        age=23, 
        gender="男", 
        job="杂货店老板", 
        personality=["内向羞涩", "细腻温柔", "责任感强", "浪漫", "小小的自卑感"],
        self_perception="""
            Darry 是一只性格内向的小鹿，做事认真，习惯独处。他细心、有责任感，总希望把事情做到最好，但常常因为优柔寡断而错失时机。他不擅长表达情绪，也害怕成为众人关注的焦点。面对突发状况时容易紧张，说话前会反复组织语言。他知道自己有些胆小，但也渴望能慢慢变得更坚定可靠。
        """,
        profile="""
            Darry 经营着父亲留下的杂货店，每天清晨都会提前到店打扫，细致擦拭木制货架，让每个角落保持整洁。他对分类有执念，货品摆放一丝不乱，总会记住常客的喜好，在他们光顾前就准备好可能需要的物品。他说话语气轻柔，眼神容易闪躲，不擅长与顾客长时间对视，但始终保持礼貌和耐心。
        """
    )
    luna = Animal(
        name="Luna", 
        age=26, 
        gender="女", 
        job="外科医生", 
        personality=["冷静理性", "自律严谨", "内心温柔", "独立坚强"],
        self_perception="""
            Luna 是一只冷静、专业的女性小鹿，她以严谨和高标准要求自己，希望能成为值得信赖的医生。她习惯独立思考，不轻易依赖他人，也不轻易表露情绪。虽然外表看起来冷淡，但她内心其实关心他人，只是不习惯用语言表达。她认为专注与能力比亲切更重要，有时会因为专注于工作而忽视他人的感受。
        """,
        profile="""
            Luna 是镇上的外科医生，拥有一间整洁的诊所。她行事干练，说话简洁明确，动作迅速利落。她每天都会按时整理医疗记录，定期打理器械，对诊疗流程一丝不苟。她不喜欢被打扰，工作时神情专注，让人有些难以靠近。偶尔深夜下班时，会独自坐在诊所后院的长椅上，静静看星星放松自己。
        """
    )
    relationships.add_animal(darry)
    relationships.add_animal(luna)
    relationships.init_relationship(darry, luna)
    relationships.update_relationship_unidirectional(darry, luna, {
            "Friend": {
                "value": 40,
                "note": "他一直很尊敬 Luna，虽然不常说话，但每次见面他都小心翼翼地想表现得得体。"
            },
            "Romance": {
                "value": 10,
                "note": "他默默喜欢着她，总是提前准备好她可能需要的东西，却从未鼓起勇气真正表达。"
            },
            "Commerce": {
                "value": 40,
                "note": "他希望能让 Luna 满意地购物，会不自觉地根据她的喜好调整商品陈列。"
            }
        }
    )
    relationships.update_relationship_unidirectional(luna, darry, {
            "Friend": {
                "value": 40,
                "note": "她觉得 Darry 是个可靠但有些拘谨的人，虽然不常交流，但在需要帮助时总能指望得上他。"
            },
            "Romance": {
                "value": 10,
                "note": "她察觉到 Darry对她有些特别的关心，但并未多作回应，只是以医生的专业保持适当距离。"
            },
            "Commerce": {
                "value": 40,
                "note": "她偶尔会去 Darry 的店里采购一些日常用品。"
            }
        }
    )
    relationships._load_all()
    relationships.driver.close()