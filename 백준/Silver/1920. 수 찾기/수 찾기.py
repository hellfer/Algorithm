import sys
input = sys.stdin.readline  # 입력을 빠르게 받기 위해 sys.stdin.readline을 사용합니다.

# 이진 탐색 함수
def binary_search(array, target, start, end):
    while start <= end:  # 시작점이 끝점보다 작거나 같을 동안 반복
        mid = (start + end) // 2  # 중간점을 구합니다.
        # 찾은 경우 1 반환
        if array[mid] == target:
            return 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return 0  # 원소를 찾지 못한 경우 0 반환

n = int(input())  # 원소의 개수 입력 받기
array = list(map(int, input().split()))  # 전체 원소 입력 받기
array.sort()  # 이진 탐색을 수행하기 위해 사전에 정렬 수행
m = int(input())  # 찾고자 하는 원소의 개수 입력 받기
x = list(map(int, input().split()))  # 찾고자 하는 원소 입력 받기

# 찾고자 하는 원소를 하나씩 확인
for i in x:
    print(binary_search(array, i, 0, n - 1))  # 각 원소에 대하여 이진 탐색을 수행하고 결과를 출력

            