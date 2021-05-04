import random

#bmi를 계산해서 레이블을 리턴하는 함수

def Metabolism(w,h,a):
     bmi = 66.47 + 13.75 * w + 5 * h -6.76 * a
     if bmi > 1600: return "man"
     if bmi > 1200: return "woman"
     return "baby"

#출력 파일 준비하기

fp = open("Metabolism.csv","w",encoding="utf-8")
fp.write("weight,heigh,age,label\r\n")

#무작위로 데이터 생성하기
cnt = {"man":0, "woman":0, "baby":0}
for i in range(1000):
    h = random.randint(150,200)
    w = random.randint(40,100)
    a= random.randint(20,70)
    label = Metabolism(w,h,a)
    cnt[label] += 1
    fp.write("{0},{1},{2},{3}\r\n".format(w,h,a,label))

fp.close()

print("ok", cnt)