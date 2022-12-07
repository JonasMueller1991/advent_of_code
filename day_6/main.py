from collections import deque

NUM_DISTINCT_SIGNALS = 14

code_segment = deque([], maxlen=NUM_DISTINCT_SIGNALS)


def count_method_call(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@count_method_call
def check_signal_to_end(signal: str) -> bool:
    code_segment.append(signal)
    return len(set(code_segment)) == NUM_DISTINCT_SIGNALS


if __name__ == '__main__':
    with open('input.csv', 'r') as file:
        for c in file.read():
            if check_signal_to_end(c):
                break
    print(f'Processed signals: {check_signal_to_end.calls}')
