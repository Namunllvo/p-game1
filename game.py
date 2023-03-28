import random
import time


# 기본 Parents class
class TOON:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    # other=target
    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
            print(f"{self.name}의 승리!!!")
        elif self.hp <= 0:
            print(f"{self.name}님은 죽었습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}")


class Monster(TOON):
    def __init__(self, name, hp, power):
        self.type_ = "몬스터"
        super().__init__(name, hp, power)

class Player(TOON):
    def __init__(self, name, hp, power, m_power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.m_power = m_power
        super().__init__(name, hp, power)

    def M_attack(self, other):
        damage = random.randint(self.m_power - 2, self.m_power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
        elif self.hp <= 0:
            print(f"{self.name}님은 죽었습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} \n 파워 {self.power} 매직 파워{self.m_power}")


# ======================================

# 플레이어 속성
Muggle = Player("머글", 50, 20, 10)
Wizard = Player("해리포터", 70, 40, 50)

# ===========================================

# 몬스터 속성
fire_dragon = Monster("불", 30, 30)
ice_dragon = Monster("얼음", 30, 35)
pkc_dragon = Monster("피카츄", 50, 40)

Dragons = [fire_dragon, ice_dragon, pkc_dragon]

# ===================================================


# ==========================게임 진행===================================

# 플레이어 기본 정보 입력
print("플레이어 설정입니다")
ID = input("닉네임을 입력하세요: ")
print(type(ID))

while True:
    # 플레이어 공격 방법 선택
    # 1번을 입력받을 경우 일반
    # 2번을 입력받을 경우 마법
    print("공격방법을 선택하세요\n 1. ?? 2. ??? 종료하기. exit")
    action = input()

    if action == "exit":
        # 프로그램 종료
        print("프로그램이 종료됩니다")
        exit()

    elif action == "1":
        print(f"{ID}님은 {Muggle.name}을 선택하셨습니다.")
        Player.show_status(Muggle)
        time.sleep(2)

    elif action == "2":
        print(f"{ID}님은 {Wizard.name}를 선택하셨습니다.")
        Player.show_status(Wizard)
        time.sleep(2)


    else:
        print("적용되지 않은 공격방법입니다\n다시 선택해주세요.")
        time.sleep(2)

    # random.monster 호출
    # 몬스터는 fire, ice, pkc 랜덤지정
    random_m = random.choice(Dragons)
    print(f"{random_m} 속성 드래곤을 처치하십시오.")
    time.sleep(2)

    # show_status로 현재 상태 출력
    if (random_m == "불"):
        Monster.show_status(fire_dragon)
        time.sleep(2)

    elif (random_m == "얼음"):
        Monster.show_status(ice_dragon)
        time.sleep(2)
    elif (random_m == "피카츄"):
        Monster.show_status(pkc_dragon)
        time.sleep(2)

    else:
        continue

turns = 0
while A:

        if turns % 2 == 0:
            print(f"\n-------------<{ID}님 공격 시작>-----------")
            # 플레이어 턴
            # 플레이어 공격
            if action == 1:
                Muggle.attack()
                Muggle.show_status()

            elif action == 2:
                Wizard.M_attack()
                Wizard.show_status()

            elif Player.show_status(hp == 0):
                print("게임이 종료되었습니다.")

            break



        elif turns % 2 == 1:
            print(f"\n-----< {random_m} 속성 드래곤 공격 시작 >------")

            if (random_m == "불"):
                fire_dragon.attack()
                fire_dragon.show_status()


            elif (random_m == "얼음"):
                fire_dragon.attack()
                ice_dragon.show_status()


            elif (random_m == "피카츄"):
                fire_dragon.attack()
                pkc_dragon.show_status()

    # turns += 1

    # if Player.show_status(hp==0):
    #     print("게임이 종료되었습니다.")
    # else: Monster.show_status(hp==0):
    #     print("게임이 종료되었습니다")





