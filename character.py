class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
    def take_damage(self, damage):
        # 피해를 입을 때의 처리
    def attack_player(self, player):
        # 플레이어 공격 로직