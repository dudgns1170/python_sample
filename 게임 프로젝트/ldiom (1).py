import random
import os

print("사자성어 게임을 시작합니다!")
cnt =5
regame ='Y'

#정답
answer = ["오매불망","등용문", "대기만성","동고동락","개과천선"]

answer1 =["과대망상","자격지심","일장춘몽","진퇴양난","청출어람"]

answer2= ["선우후락","홍익인간","과유불급","각곡유목","형설지공"]
#파일읽기

#초급 문제
with open('sample.txt', 'r', encoding='utf-8') as f:
    c1 = f.readlines()

#중급 문제
with open('sample1.txt', 'r', encoding='utf-8') as f:
    c2 = f.readlines()
    
#고급 문제
with open('sample2.txt', 'r', encoding='utf-8') as f:
    c3 =f.readlines()

#게임 선택
while True:
    choice = input("""게임 선택
        1.초급
        2.중급
        3.고급
        4.종료
        게임을 선택해 주세요:  """)
    if choice == "1":
        choice=1
        while True:
            if cnt < 5:
                cnt += 1
            os.system("clear")
            if regame == 'Y' or regame == 'y':
                while True:
                    i = random.randrange(0, len(c1))
                    print(c1[i])
                    a = input("이말의 사자성어는?")
                    if a == answer[i]:
                        print("정답입니다!!\n게임을 종료합니다.")
                        break
                    elif a != answer[i]:
                        cnt -= 1
                        print("틀렸어요! 다시 도전!!")
                        print("남은 기회", cnt,)
                        if cnt == 0:
                            break
                        continue
            else:
                regame = 'y'
                print("다음에 또만나요!!")
                break
            regame = input("한번더 하시겠습니까?\n Y or N:")
            cnt= 5
    if choice == '2':
        choice =2
        while True:
            if cnt < 5:
                cnt += 1
            os.system("clear")
            if regame == 'Y' or regame == 'y':
                while True:
                    i = random.randrange(0,len(c2))
                    print(c2[i])
                    a = input("이말의 사자성어는?")
                    if a == answer1[i]:
                        print("정답입니다!!\n게임을 종료합니다.")
                        break
                    elif a != answer1[i]:
                        cnt -= 1
                        print("틀렸어요! 다시 도전!!")
                        print(cnt, "번 남았아요!")
                        if cnt == 0:
                            break
                        continue
            else:
                regame = 'y'
                break
            regame = input("한번더 하시겠습니까?\n Y or N:")
            cnt = 5
    if choice == '3':
        choice =3
        while True:
            if cnt < 5:
                cnt += 1
            os.system("clear")
            if regame == 'Y' or regame == 'y':
                while True:
                    i = random.randrange(0,len(c3))
                    print(c3[i])
                    a = input("이말의 사자성어는?")
                    if a == answer2[i]:
                        print("정답입니다!!\n게임을 종료합니다.")
                        break
                    elif a != answer2[i]:
                        cnt -= 1
                        print("틀렸어요! 다시 도전!!")
                        print(cnt, "번 남았아요!")
                        if cnt == 0:
                            break
                        continue
            else:
                regame = 'y'
                break
            regame = input("한번더 하시겠습니까?\n Y or N:")
            cnt = 5
    elif choice == '4':
        choice =4
        print('게임을 종료합니다.')
        break
    else:
        print("다시 입력해주세요!")
