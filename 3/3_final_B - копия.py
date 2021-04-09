

count = int(input())
info = []
username, score, fine = input().split()
for _ in range(count):
    info.append((username, -int(score), int(fine)))
print(info)

