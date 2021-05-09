
start1 = int(input())
finish1 = int(input())
start2 = int(input())
finish2 = int(input())
is1startIn2 = start2 <= start1 <= finish2
is1finishIn2 = start2 <= finish1 <= finish2
is1in2 = is1startIn2 or is1finishIn2
is2startIn1 = start1 <= start2 <= finish1
is2finishIn1 = start1 <= finish2 <= finish1
is2in1 = is2startIn1 or is2finishIn1
answer = start1 <= finish2 and start2 <= finish1
print(answer)
