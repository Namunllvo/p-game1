# import Tower # 몬스터
import test

import random, time

# instance = test.Player
# print(instance.rest)


# if (Monster.hp == 0):
#     get_reward = random.choice()
def reward():
    while True:
        print("몬스터 처치 성공! \n다음 층으로 올라갑니다.\n올라가기 전에 보상을 선택해 주세요.")
        print('1. 체력회복 2. 마나회복 3. 경험치 획득 4. 아이템 획득 5.???(랜덤)')
        # a = '1. 체력회복 2. 마나회복 3. 경험치 획득 4. 아이템 획득 5.???(랜덤)'
        # select_num = int(input(a))

        select = int(input("→   "))
        # reward_list = ['체력회복', '마나회복', '경험치획득', '아이템획득']
        # choice = reward_list(select())
        # print(choice)

        # print(f"선택된 보상은 {select} 입니다.")

        if (select == 1):
            # Monster.hp 50% 회복
            print()
            print(f"name님의 체력이 50% 회복되었습니다.\n 현재 HP self.hp/self.max_hp")
            time.sleep(2)

            # return hp_charge
            # charge = crt.Player()
            # charge.name()

            break

        elif (select == 2):
            # Player.power 100% 회복
            print(f"name님의 마나가 전체 회복되었습니다.\ 현재 마나 self.mana/100")
            time.sleep(2)

            break
            # return test.py의 Player.power = max_hp

        elif (select == 3):
            # Player.경험치 40 획득(몬스터 3마리 잡고 올라갈때 경험치 40만큼 부여 -> )
            print(f"name님은 경험치 40만큼 획득했습니다.\ 현재 HP self.hp/self.max_h")
            time.sleep(2)

            break
            # return test.py의 self.experience += 40

        elif (select == 4):
            # 아이템 획득
            # 아이템 시스템으로 연결
            print(f"name님의 획득한 아이템(이름) 회복/획득했습니다.\ 현재 HP or mana or 경험치 self.h/self.max_hp")
            # 아이템 함수 호출
            time.sleep(2)

            break
            # return item.py의 item 선택으로 연결

        # elif (select == 5):
        #     reward_list = ['체력회복', '마나회복', '경험치획득', '아이템획득']
        #     choice = random.choice(reward_list)
        #     print(choice)
        #     print(type(choice))
        #     print(f"선택된 보상은 {choice} 입니다.")
        #     time.sleep(2)
        #
        #     # return select == num
        #
        #     # return select == (num)
        else:
            print("적용되지 않은 값입니다. \n다시선택해주세요")
            time.sleep(1)

            break

        # return 선택된 num값의 if 문으로

# print("몬스터 처치 성공! \n다음 층으로 올라갑니다.\n올라가기 전에 보상을 선택해 주세요")

# while True:
#     print("몬스터 처치 성공! \n다음 층으로 올라갑니다.\n올라가기 전에 보상을 선택해 주세요.")
#     print('1. 체력회복 2. 마나회복 3. 경험치 획득 4. 아이템 획득 5.???(랜덤)')
#     # a = '1. 체력회복 2. 마나회복 3. 경험치 획득 4. 아이템 획득 5.???(랜덤)'
#     # select_num = int(input(a))
#
#     select = int(input("→   "))
#     # reward_list = ['체력회복', '마나회복', '경험치획득', '아이템획득']
#     # choice = reward_list(select())
#     # print(choice)
#
#     print(f"선택된 보상은 {select} 입니다.")
#
#     if (select == 1):
#         # Monster.hp 50% 회복
#         print()
#         print(f"name님의 체력이 50% 회복되었습니다.\ 현재 HP self.hp/self.max_hp")
#         time.sleep(2)
#
#         break
#         # return
#
#     elif (select == 2):
#         # Player.mana 100% 회복
#         print(f"name님의 마나가 전체 회복되었습니다.\ 현재 마나 self.mana/100")
#         time.sleep(2)
#
#         break
#         # return
#
#     elif (select == 3):
#         # Player.경험치 40 획득(몬스터 3마리 잡고 올라갈때 경험치 40만큼 부여 -> )
#         print(f"name님은 경험치 40만큼 획득했습니다.\ 현재 HP self.hp/self.max_h")
#         time.sleep(2)
#
#         break
#         # return
#
#     elif (select == 4):
#         # 아이템 획득
#         # 아이템 시스템으로 연결
#         print(f"name님의 획득한 아이템(이름) 회복/획득했습니다.\ 현재 HP or mana or 경험치 self.h/self.max_hp")
#         time.sleep(2)
#
#         break
#         # return
#
#     elif (select == 5):
#         reward_list = ['체력회복', '마나회복', '경험치획득', '아이템획득']
#         choice = random.choice(reward_list)
#         print(choice)
#         print(f"선택된 보상은 {choice} 입니다.")
#         time.sleep(2)
#
#         break
#         # return
#
#         # return select == (num)
#     else:
#         print("적용되지 않은 값입니다. \n다시선택해주세요")
#         time.sleep(1)
#
#     continue
#
#     # return 선택된 num값의 if 문으로

# 보상시스템
# 몬스터를 사냥하고 나오는 보상으로
# 플레이어를 강하게 만들거나
# 스토리 진행이 가능하게 만들어보세요.
# 1. 몬스터 사냥에 성공 시 다음중
# 하나 또는 전부를 획득합니다.
# ex) 체력 50% 회복, 마나 전부 회복,
#     경험치 획득, 아이템 획득 등
# 2. 획득한 보상을 바탕으로 플레이어가
# 강해지며 스토리에 따라 게임을 진행할 수 있습니다.
# while문을 돌리고 종료후
# 다음 단계로 턴하기
