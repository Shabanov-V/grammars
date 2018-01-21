import os
import re

def algo1(graph_file_path, grammar_file_path):
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
    ans = []
    for i in range(N):
        for j in range(N):
            if ('S' in arr[i][j]):
                ans.append(arr[i][j])
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

    ans = []
    for i in range(N):
        for j in range(N):
            if ('S' in arr[i][j]):
                ans.append(str(i) + 'S' + str(j))
    grammar_file.close()
    graph_file.close()
    return ans


def graph_to_array(graph_file_path):
    graph_file = open(graph_file_path, 'r')
    graph = graph_file.read()
    N = max(list(map(int, re.findall('\d+', graph)))) + 1
    arr = [[''] * N for i in range(N)]
    paths = re.findall('(\d+) -> (\d+)\[label=\"(.+)\"\]', graph)
    for i in paths:
        (a, b, c) = i
        arr[int(a)][int(b)] = c
    return arr


def grammar_to_graph(grammar_file_path):
    grammar_file = open(grammar_file_path, 'r')
    grammar = grammar_file.read()
    grammar_rules = list(zip(*(re.findall(r"(.+) -> (.+)", grammar))))
    M = len(grammar_rules[1])
    unique = list(set(grammar_rules[0]))
    order = []
    net = 0
    D = 100 * M
    arr = [[''] * (D + 1) for i in range(D + 1)]
    #print(M)
    starts = []
    ends = []
    max_cur = 0
    for i in unique:
        order += [(i, net)]
        cur_grammars = list(filter(lambda x: x[0] == i, list(zip(*grammar_rules))))
        counter = 1
        #print("cur_grammars = " + str(cur_grammars))
        rls = [s.split(' ') for s in list(zip(*cur_grammars))[1]]
        #print ("rls = " + str(rls))
        D = sum(list(map(len, rls))) - len(rls) + 3
        #print("D = " + str(D))
        starts += [str(net)]
        for j in cur_grammars:
            t, rules = j # rules = 'F F'
            prev = net
            cur = net + counter
            #print("rules = " + rules)
            for k in range(len(rules)): # k = 'F'
                if (k == len(rules) - 1):
                    cur = net + D - 1
                    ends += [str(cur)]
                    counter -= 1
                if rules[k] == ' ':
                    continue
                #print(prev, cur, rules[k])
                arr[prev][cur] = rules[k]
                max_cur = max(max_cur, cur)
                prev = cur
                counter += 1
                cur = net + counter
        net += D
    ends = list(set(ends))
    #print("order = " + str(order))
    #print("starts = " + str(starts))
    #print("ends = " + str(ends))
    ans = [[''] * (max_cur + 1) for i in range(max_cur + 1)]
    for i in range(max_cur + 1):
        for j in range(max_cur + 1):
            ans[i][j] = arr[i][j]
    return ans, starts, ends, order


def out_graph(arr, starts = [], ends = [], comments=''):
    ans = '''
digraph AST {
rankdir=LR
'''
    t = ''
    tmp = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (arr[i][j] == ''):
                continue
            tmp += [str(i)]
            tmp += [str(j)]
            t += str(i) + ' -> ' + str(j) + '[label="' + str(arr[i][j]) + '"]\n'
    for i in starts:
        ans += i + '[label="' + i + '", color="green"]\n'
    for i in ends:
        ans += i + '[label="' + i + '", shape="doublecircle"]\n'
    tmp = list(filter(lambda x: not x in starts and not x in ends, list(set(tmp))))
    ans += '; '.join(tmp) + '\n'
    ans += t
    ans += 'label="' + comments + '";\n'
    ans += '}'
    return ans

def out_graph_list(arr):
    ans = '''digraph AST {
rankdir=LR
'''
    t = ''
    tmp = []
    for i in arr:
        a, b, c = i
        t += '"' + ','.join(str(x) for x in a) +  '" -> "' + ','.join(str(x) for x in c) + '"' + '[label="' + str(b) + '"]\n'
    ans += t
    ans += '}'
    return ans


def algo3(graph_file_path, grammar_file_path):
    arr = graph_to_array(graph_file_path)
    grammar, starts, ends, order = grammar_to_graph(grammar_file_path)
    ans = []
    starts_dic = dict(order)
    conf_set = set()
    gss = []
    for z in range(len(arr)):
        conf = [(z, starts_dic['S'], (z, 'S'))]
        conf_set = set()
        colored = set()
        while conf:
            if (conf[0] in conf_set):
                enter_pos, gramm_pos, gss_node = conf.pop(0)
                # print("--cur_node = ", end='')
                # print(enter_pos, gramm_pos, gss_node)
                continue
            conf_set.add(conf[0])
            enter_pos, gramm_pos, gss_node = conf.pop(0)
            if str(gramm_pos) in ends:
                ans += [str(gss_node[0]) + str(gss_node[1]) + str(enter_pos)]
                for i in gss:
                    fr, ed, to = i
                    if fr == gss_node:
                        conf += [(enter_pos, ed, to)]
            # print("cur_node = ", end='')
            # print(enter_pos, gramm_pos, gss_node)
            for j in range(len(arr[enter_pos])):
                if arr[enter_pos][j] != '':
                    # print(arr[enter_pos][j])
                    next_symb = arr[enter_pos][j]
                    for i in range(len(grammar[gramm_pos])):
                        grammar_symb = grammar[gramm_pos][i]
                        if grammar_symb == next_symb:
                            conf += [(j, i, gss_node)]
                        if re.match(r'[A-Z]+\d*', grammar_symb):
                            conf += [(enter_pos, starts_dic[grammar_symb], (enter_pos, grammar_symb))]
                            # print("GSS: ", end='')
                            # print(((enter_pos, grammar_symb), i, gss_node))
                            gss.append(((enter_pos, grammar_symb), i, gss_node))

    # f = open('graph.dot', 'w')
    # for i in out_graph(grammar, starts, ends, str(order)):
    #     f.write(i)
    # f.close()
    # os.system('dot -Tpdf graph.dot -o testGraph.pdf')

    res = []
    for i in ans:
        if ('S' in i):
            res.append(i)

    res = set(res)
    return res