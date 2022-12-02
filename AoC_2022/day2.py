import sys

def get_rounds() -> [[str]]:
    r = []
    rounds = []
    for _ in sys.stdin:
        r.append(_.strip())
    for _ in r:
        _ = _.split(' ')
        rounds.append(_)
    return rounds

def get_your_shape(rounds:[[str]]) -> [str]:
    shape = []
    for round in rounds:
        shape.append(round[1])
    return shape

def get_round_outcomes(rounds:[[str]]) -> [str]:
    outcomes = []
    for round in rounds:
        if round[0] == 'A' and round[1] == 'X' or round[0] == 'B' and round[1] == 'Y' or round[0] == 'C' and round[1] == 'Z':
            outcomes.append('D')
        elif round[0] == 'A' and round[1] == 'Y' or round[0] == 'B' and round[1] == 'Z' or round[0] == 'C' and round[1] == 'X':
            outcomes.append('W')
        elif round[0] == 'A' and round[1] == 'Z' or round[0] == 'B' and round[1] == 'X' or round[0] == 'C' and round[1] == 'Y':
            outcomes.append('L')
    return outcomes

def calc_round_score(round:[(str)], choice_score:{str: int}, round_score:{str: int}) -> [int]:
    scores = []
    for i in round:
        scores.append(choice_score[i[0]] + round_score[i[1]])
    return scores

def get_choice(rounds:[[str]]) -> [str]:
    choices = []
    for round in rounds:
        if round[0] == 'A' and round[1] == 'X' or round[0] == 'B' and round[1] == 'Z' or round[0] == 'C' and round[1] == 'Y':
            choices.append('S')
        elif round[0] == 'A' and round[1] == 'Y' or round[0] == 'B' and round[1] == 'X' or round[0] == 'C' and round[1] == 'Z':
            choices.append('R')
        elif round[0] == 'A' and round[1] == 'Z' or round[0] == 'B' and round[1] == 'Y' or round[0] == 'C' and round[1] == 'X':
            choices.append('P')
    return choices

# part 1
def total_score_1() -> int:
    rounds = get_rounds()
    your_choice = {'X': 1, 'Y': 2, 'Z': 3}
    round_outcome = {'L': 0, 'D': 3, 'W': 6}
    choices = get_your_shape(rounds)
    outcomes = get_round_outcomes(rounds)
    choice_and_outcome = list(zip(choices, outcomes))
    scores = calc_round_score(choice_and_outcome, your_choice, round_outcome)
    total_sc = sum(scores)
    return total_sc

# part 2
def total_score_2() -> int:
    rounds = get_rounds()
    round_outcome = {'X': 0, 'Y': 3, 'Z': 6}
    your_choice = {'R': 1, 'P': 2, 'S': 3}
    choices = get_choice(rounds)
    outcomes = get_your_shape(rounds) # same function gets the outcomes, not shape, as the meaning has changed here in part 2 of the question
    choice_and_outcome = list(zip(choices, outcomes))
    scores = calc_round_score(choice_and_outcome, your_choice, round_outcome)
    total_sc = sum(scores)
    print(choice_and_outcome)
    return total_sc

# part 1
print(total_score_1())
# part 2
print(total_score_2())
