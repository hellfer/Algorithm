n, m = map(int, input().split())
if n != 0:
    books = list(map(int, input().split()))
    books.append(m+1)  # 마지막에 큰 수를 추가하여 마지막 박스를 세는 데 도움을 줍니다.
else:
    books = []

box = 0
count = 0

for book in books:
    if box + book <= m:
        box += book
    else:
        box = book
        count += 1

print(count)

