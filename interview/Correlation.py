def mean(lst):
    return sum(lst) / len(lst)


def std(lst):
    mu = mean(lst)
    ss = mean([(x - mu)**2 for x in lst])
    return pow(ss, 0.5)


def corr(lst1, lst2):
    mu1 = mean(lst1)
    mu2 = mean(lst2)
    sd1 = std(lst1)
    sd2 = std(lst2)

    cov = mean([x[0]*x[1] for x in zip(lst1, lst2)]) - mu1*mu2

    return cov / (sd1 * sd2)

n = int(input().strip())

scores = [[], [], []]

while (n):
    n -= 1
    s = [int(x) for x in input().strip().split()]
    scores[0].append(s[0])
    scores[1].append(s[1])
    scores[2].append(s[2])

cor1 = corr(scores[0], scores[1])
cor2 = corr(scores[1], scores[2])
cor3 = corr(scores[2], scores[0])

print('%.2f' % cor1)
print('%.2f' % cor2)
print('%.2f' % cor3)
