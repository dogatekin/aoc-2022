import fileinput
import re
from collections import defaultdict
from itertools import combinations

lines = [line.strip() for line in fileinput.input()]

pattern = r'Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.+)'
flows = {}
adj = {}
for line in lines:
    valve, flow, leads_to = re.match(pattern, line).groups()
    flows[valve] = int(flow)
    adj[valve] = leads_to.split(', ')

v2i = {valve: i for i, valve in enumerate(flows)}
i2v = {i: valve for i, valve in enumerate(flows)}

valves = flows.keys()
dist = {v2i[v]: {v2i[w]: 1 if w in adj[v] else 0 if v == w else float('inf') for w in valves} for v in valves}
for k in range(len(valves)):
    for i in range(len(valves)):
        for j in range(len(valves)):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

cost = defaultdict(dict)
for v in dist:
    for w, c in dist[v].items():
        if 0 < c < float('inf'):
            cost[i2v[v]][i2v[w]] = c

important = {v for v, f in flows.items() if f > 0}

def solve(valve, t, opened, important, memo):
    if t <= 0:
        return 0
    if (valve, t, opened) in memo:
        return memo[valve, t, opened]
    flow = t * flows[valve]
    opened |= (1 << v2i[valve])
    memo[valve, t, opened] = flow + max((solve(v, t - cost[valve][v] - 1, opened, important, memo) for v in important if not opened & (1 << v2i[v])), default=0)
    return memo[valve, t, opened]

print(solve('AA', 30, 0, important, {}))

m = 0
for l1 in range(len(important)//2 - 1, len(important)//2 + 1):
    persons = combinations(important, l1)
    for person in map(set, persons):
        elephant = important - person
        f = solve('AA', 26, 0, person, {}) + solve('AA', 26, 0, elephant, {})
        m = max(m, f)
print(m)