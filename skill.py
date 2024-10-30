class Skill:
    def __init__(self, name, skill_type, power, cost):
        self.name = name
        self.skill_type = skill_type # 예: 공격, 방어, 회복
        self.power = power # 스킬의 힘
        self.cost = cost # 소모 스태미나 등
    def apply(self, user, target):
        # 스킬 사용 효과 적용
