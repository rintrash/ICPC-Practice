#COMPLETED IN TEST
numCards = int(input())
cards = [int(i) for i in input().split()]

cards = sorted(cards)
if len(cards) == 0:
    score = 0
else: 
    score = cards[0]
    for i in range(1, len(cards)):
        if cards[i] != cards[i - 1] + 1:
            score += cards[i]
print(score)