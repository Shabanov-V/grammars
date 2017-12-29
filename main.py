import os
import re


def solver(graph_file_path, grammar_file_path):
    graph_file = open(graph_file_path, 'r')
    grammar_file = open(grammar_file_path, 'r')
    graph = graph_file.read()
    grammar = grammar_file.read()
    N = max(list(map(int, re.findall('\d+', graph)))) + 1
    arr = [[''] * N for i in range(N)]
    paths = re.findall('(\d+) -> (\d+)\[label=\"(.+)\"\]', graph)
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
    grammar_file.close()
    graph_file.close()
    return ans



def algo2(graph_file_path, grammar_file_path):
    graph_file = open(graph_file_path, 'r')
    grammar_file = open(grammar_file_path, 'r')
    graph = graph_file.read()
    grammar = grammar_file.read()
    N = max(list(map(int, re.findall('\d+', graph)))) + 1
    arr = [[''] * N for i in range(N)]
    visited = [False] * N
    paths = re.findall('(\d+) -> (\d+)\[label=\"(.+)\"\]', graph)
    grammar_rules = list(zip(*(re.findall(r"(.+) -> (.+)", grammar))))
    grammar_rules[1] = [x.replace(" ", "") for x in grammar_rules[1]]
    M = len(grammar_rules[1])
    max_depth = max([len(x) for x in grammar_rules[1]])
    for i in paths:
        (a, b, c) = i
        arr[int(a)][int(b)] = c
    f = [True]

    def dfs(start, cur, cur_depth, path):
        visited[cur] = True
        t = [i for i, x in enumerate(grammar_rules[1]) if x == path]
        for j in t:
            if not (grammar_rules[0][j] in arr[start][cur]):
                f[0] = True
                arr[start][cur] += grammar_rules[0][j]
        if (cur_depth == max_depth):
            return
        for i in range(N):
            if (arr[cur][i] != ''):
                for j in arr[cur][i]:
                    dfs(start, i, cur_depth + 1, path + j)

    while (f[0]):
        f[0] = False
        for i in range(N):
            dfs(i, i, 0, '')

     # dfs(24, 24, -1, '')


    ans = 0
    for i in range(N):
        for j in range(N):
            if ('S' in arr[i][j]):
                ans += 1
    grammar_file.close()
    graph_file.close()
    return ans

if __name__ == '__main__':
    print (algo2('data/skos.dot', 'data/grammar1'))