class Player:
    def __init__(self, name, job, skills, items):
        self.name = name
        self.job = job
        self.skills = skills
        self.items = items
        self.attributes = {'health': 100, 'stamina': 100, 'wealth': 0}
    def use_skill(self, skill_name, target):
        # 스킬 사용 로직
    def attack(self, target):
        # 기본 공격 로직
    def add_item(self, item):
        # 인벤토리에 아이템 추가
    def get_status(self):
        # 현재 상태 반환