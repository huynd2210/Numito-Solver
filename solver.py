import re
from itertools import product

def ensureInput(input):
    if type(input) is int:
        return [input]
    return input

def solve(puzzleInputs, targetSums):
    puzzleInputs = ensureInput(puzzleInputs)
    result = dict()
    if targetSums == "=":
        return solveForEqual(puzzleInputs)

    for targetSum in targetSums:
        result[targetSum] = solveForTarget(puzzleInputs, targetSum)
    return result

def solveForTarget(puzzleInputs: str, targetSum):
    puzzleInputs = parse(puzzleInputs)
    possibleCombinations = product(*puzzleInputs)
    results = []
    for combination in possibleCombinations:
        # ic(combination)
        result = eval("".join(combination))
        if result == targetSum:
            results.append("".join(combination))
    return results

def evaluateEquationSide(equation: str):
    equation = parse(equation)
    possibleCombinations = product(*equation)
    results = dict()
    for combination in possibleCombinations:
        result = eval("".join(combination))
        results[combination] = result
    return results


def solveForEqual(puzzleInputs: str):
    if '=' not in puzzleInputs:
        return None
    lhs, rhs = puzzleInputs.split('=')
    rhsExpressionTargetDict = evaluateEquationSide(rhs)
    results = []
    for rhsExpression, rhsExpressionResult in rhsExpressionTargetDict.items():
         lhsSolution = solveForTarget(lhs, rhsExpressionResult)
         for solution in lhsSolution:
             resultString = "{}={}".format(solution, "".join(rhsExpression))
             results.append(resultString)

    return results
def parse(expr):
    tokens = re.findall(r'\d+|[+\-*/]+', expr)
    return tokens

if __name__ == '__main__':
    input = "59/*53-+853+327"
    target = [12,13]
    # target = "="
    print(solve(input, target))
