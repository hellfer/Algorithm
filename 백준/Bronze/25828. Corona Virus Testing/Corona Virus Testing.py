def main():
    # 입력을 받아서 공백으로 분리한 후 정수로 변환
    g, p, t = map(int, input().strip().split())
    
    # 개별 테스트에 필요한 총 키트 수 계산
    total_individual_kits = g * p
    
    # 그룹 테스트에 필요한 총 키트 수 계산
    total_group_kits = g + (t * p)
    
    # 두 방법의 키트 수를 비교하여 결과 출력
    if total_individual_kits < total_group_kits:
        print(1)
    elif total_individual_kits > total_group_kits:
        print(2)
    else:
        print(0)

if __name__ == "__main__":
    main()
