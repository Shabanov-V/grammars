import os
import re


if __name__ == "__main__":
    graph_file = open('data/travel.dot', 'r')
    grammar_file = open('data/grammar1CNF', 'r')
    graph = graph_file.read()
    grammar = grammar_file.read()
    N = max(list(map(int, re.findall('\d+', graph)))) + 1
    arr = [[''] * N for i in range(N)]
    paths = re.findall('(\d+) -> (\d+)\[label=\"(.+)\"\]', graph)
    mp1 = re.findall('(.+) -> (.+)', grammar)
    #print (any((c not in 'CSZSZSZSZSZSZSZSZSZ') for c in ['S', 'Z', 'y']))
    for i in paths:
        (a, b, c) = i
        arr[int(a)][int(b)] = ''.join(re.findall(r"(.+) -> %s" % c, grammar))
    f = True
    while (f):
        f = False
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if (arr[i][k] != '' and arr[k][j] != ''):
                        for o1 in arr[i][k]:
                            for o2 in arr[k][j]:
                                t = o1 + o2
                                fnd = re.findall(r"(.+) -> %s\n" % t, grammar)
                                if (any((c not in arr[i][j]) for c in fnd)):
                                    f = True
                                    arr[i][j] += ''.join(fnd)
                                    #print(fnd, arr[i][j])
    ans = 0
    for i in range(N):
        for j in range(N):
           if ('S' in arr[i][j]):
               ans += 1
    print (ans)