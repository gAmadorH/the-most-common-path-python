import json


def mcp():
    users_transitions = {}
    freq_transitions = {}
    max_count = - 1
    mcps = []

    with open('input.json') as f_in:
        input_data = json.load(f_in)

        for data in input_data:
            data_arr = data.strip().split(',')
            if len(data_arr) == 2:
                user_id, state_id = data_arr
                if user_id not in users_transitions:
                    users_transitions[user_id] = []
                users_transitions[user_id].append(state_id)

    # https://stackoverflow.com/questions/10458437/what-is-the-difference-between-dict-items-and-dict-iteritems
    for user_id, states in users_transitions.items():
        for i in range(2, len(states)):
            transition = states[i - 2] + states[i - 1] + states[i]

            if transition not in freq_transitions:
                freq_transitions[transition] = 0
            freq_transitions[transition] += 1

            if freq_transitions[transition] > max_count:
                max_count = freq_transitions[transition]

    for transition, count in freq_transitions.items():
        if count == max_count:
            mcps.append(transition)

    mcps.sort()

    print('The most common path')
    for mcp_item in mcps:
        print(mcp_item[0] + '->' + mcp_item[1] + '->' + mcp_item[2])


if __name__ == '__main__':
    mcp()
