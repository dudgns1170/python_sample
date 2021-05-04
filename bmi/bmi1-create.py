import random

# BMI를 계산해서 레이블을 리턴하는 함수
def calc_sp(s, o):
    sp = s * (o+15)
    if sp > 60: return "Speed Warning"
    if sp > 80: return "speeding Warning"
    return "License suspension"

# 출력 파일 준비하기
fp = open("sp.csv","o",encoding="utf-8")
fp.write("speed,speeding,label\r\n")

# 무작위로 데이터 생성하기
cnt = {"Speed Warning":0, "speeding Warning":0, "License suspension":0}
for i in range(20000):
    h = random.randint(50,100)
    w = random.randint(60,120)
    label = calc_sp(s, o)
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(s, o, label))
fp.close()
print("ok,", cnt)