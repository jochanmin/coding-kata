"""
link: https://school.programmers.co.kr/learn/courses/30/lessons/43164?itm_content=course14743
"""

import collections

answer = []
graph = collections.defaultdict(list)


def dfs(s):
    while graph[s]:
        dfs(graph[s].pop(0))

    if not graph[s]:
        answer.append(s)
        return


def solution(tickets):
    for a, b in tickets:
        graph[a].append(b)
    for a, b in graph.items():
        graph[a].sort()

    dfs("ICN")

    return answer[::-1]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"])
