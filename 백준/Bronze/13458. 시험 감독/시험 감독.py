import sys
input = sys.stdin.readline

# 각 시험장별 총감독관1명, 부감독관 여러명 가능
N = int(input()) # 시험장 수
arr = list(map(int, input().split())) # 시험장별 응시인원
B, C = map(int, input().split()) # B: 총감독관 감시 인원수 # C: 부감독관 감시 인원수
cnt = N # 총감독관은 시험장 개수만큼
for i in arr:
    if i-B >0: # 총감독관이 감독한 인원 외의 인원만 부감독관이 감독
        cnt += ((C - 1 + i - B)//C) 
print(cnt)