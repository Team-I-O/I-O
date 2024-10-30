class Item:
    def __init__(self, name, item_type, effect):
        self.name = name
        self.item_type = item_type # 예: 회복, 공격 강화, 방어
        self.effect = effect # 아이템의 효과
    def use(self, target):
        # 아이템 사용 효과 적용