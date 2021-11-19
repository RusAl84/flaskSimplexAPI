import pulp

def optimize(z, rests):
    prob = pulp.LpProblem('MAX', pulp.LpMaximize)
    x1 = pulp.LpVariable('x1', 0, None)
    x2 = pulp.LpVariable('x2', 0, None)
    x3 = pulp.LpVariable('x3', 0, None)
    prob += z[0] * x1 + z[1] * x2 + z[2] * x3
    for rest in rests:
        prob += rest[0] * x1 + rest[1] * x2 + rest[2] * x3 <= rest[3]
    prob.solve()
    str1 = f"x1 = {pulp.value(x1)}, x2 = {pulp.value(x2)}, x3 = {pulp.value(x3)}, Z = {pulp.value(prob.objective)}"
    return str1

if __name__ == '__main__':
    z = [6, 1, 5]
    rests = [[7, 17, 17, 242],
             [16, 5, 1, 329],
             [18, 3, 3, 325]]
    str1 = optimize(z, rests)
    print(str1)
