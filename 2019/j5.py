# CCC 2019 Junior 5: Rule of Three

# list of substitution rules
rules = []
# iterate through each line
for i in range(3):
    # input of substitution rule
    rule = input().split()
    # append rule to rules
    rules.append((rule[0], rule[1]))

# input of number of steps and initial and final sequence
steps, initial, final = input().split()

# set of sequence combinations
sequences = set()


# returns the indices where rule is found in sequence
def get_indices(sequence, rule):
    indices = []
    for x in range(len(sequence)):
        if sequence[x:x+len(rule)] == rule:
            indices.append(x)

    return indices


def replace(steps_left, sequence, ans):
    # return ans if sequence is equal to final and there are no steps left
    if sequence == final and steps_left == 0:
        return ans
    # return if there are no steps left
    elif steps_left == 0:
        return

    # return if sequence combination is in sequences set
    if (sequence, steps_left) in sequences:
        return

    # add sequence combination to sequences set
    sequences.add((sequence, steps_left))

    # iterate through each rule
    for i in range(len(rules)):
        rule, sub = rules[i][0], rules[i][1]
        # get indices that rule is found in sequence
        indices = get_indices(sequence, rule)
        # iterate through each index
        for index in indices:
            # form the new sequence with the substitution rule
            new_sequence = sequence[:index] + sub + sequence[index+len(rule):]

            # make copy of ans and append new_sequence to it
            new_ans = ans.copy()
            new_ans.append((i+1, index+1, new_sequence))

            # call recursive function with updated parameters
            res = replace(steps_left-1, new_sequence, new_ans)

            # return res if it is not empty
            if res:
                return res


# output
ans = replace(int(steps), initial, [])
for x in ans:
    print(x[0], x[1], x[2])
