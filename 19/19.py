import re
import fileinput
from math import ceil
from time import time

blueprints = [line.strip() for line in fileinput.input()]

pattern = r"Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."

def solve(t, ore, clay, obs, orebot, claybot, obsbot, geobot, memo):
    # act based on next robot to build
    if t <= 0:
        return 0
    if (t, ore, clay, obs, orebot, claybot, obsbot, geobot) in memo:
        return memo[t, ore, clay, obs, orebot, claybot, obsbot, geobot]

    actions = []

    # don't build until the end
    actions.append(t * geobot)

    # build orebot next
    if orebot < max(ore_ore, clay_ore, obs_ore, geo_ore):
        ore_need = max(0, ore_ore - ore)
        dt = ceil(ore_need / orebot) + 1
        if dt < t:
            actions.append(dt*geobot + solve(t-dt, ore + dt*orebot - ore_ore, clay + dt*claybot, obs + dt*obsbot, orebot+1, claybot, obsbot, geobot, memo))

    # build claybot next
    if claybot < obs_clay:
        ore_need = max(0, clay_ore - ore)
        dt = ceil(ore_need / orebot) + 1
        if dt < t:
            actions.append(dt*geobot + solve(t-dt, ore + dt*orebot - clay_ore, clay + dt*claybot, obs + dt*obsbot, orebot, claybot+1, obsbot, geobot, memo))

    # build obsbot next
    if obsbot < geo_obs:
        ore_need = max(0, obs_ore - ore)
        clay_need = max(0, obs_clay - clay)
        if claybot > 0:
            dt = max(ceil(ore_need / orebot), ceil(clay_need / claybot)) + 1
            if dt < t:
                actions.append(dt*geobot + solve(t-dt, ore + dt*orebot - obs_ore, clay + dt*claybot - obs_clay, obs + dt*obsbot, orebot, claybot, obsbot+1, geobot, memo))

    # build geobot next
    ore_need = max(0, geo_ore - ore)
    obs_need = max(0, geo_obs - obs)
    if obsbot > 0:
        dt = max(ceil(ore_need / orebot), ceil(obs_need / obsbot)) + 1
        if dt < t:
            actions.append(dt*geobot + solve(t-dt, ore + dt*orebot - geo_ore, clay + dt*claybot, obs + dt*obsbot - geo_obs, orebot, claybot, obsbot, geobot+1, memo))

    memo[t, ore, clay, obs, orebot, claybot, obsbot, geobot] = max(actions)
    return memo[t, ore, clay, obs, orebot, claybot, obsbot, geobot]

t = time()
part1 = 0
part2 = 1
for bid, blueprint in enumerate(blueprints, 1):
    ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = map(int, re.match(pattern, blueprint).groups())
    max_geodes = solve(24, 0, 0, 0, 1, 0, 0, 0, {})
    part1 += bid * max_geodes

    if bid <= 3:
        max_geodes = solve(32, 0, 0, 0, 1, 0, 0, 0, {})
        part2 *= max_geodes

print(part1) # 1262
print(part2)
print('Took', int(time() - t), 'seconds.')