from collections import deque

NUM_DISTINCT_SIGNALS = 14

code_segment = deque([], maxlen=NUM_DISTINCT_SIGNALS)


def check_signal_to_end(signal: str) -> bool:
    code_segment.popleft()
    code_segment.append(signal)
    return len(set(code_segment)) == NUM_DISTINCT_SIGNALS


if __name__ == '__main__':
    result_counter = 0
    with open('input.csv', 'r') as file:
        for counter, c in enumerate(file.read()):
            if counter < NUM_DISTINCT_SIGNALS:
                code_segment.append(c)
            elif check_signal_to_end(c):
                result_counter = counter + 1
                break

    print(f'Processed signals: {result_counter}')
