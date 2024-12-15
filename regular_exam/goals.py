def find_lis(sequence):
    n = len(sequence)
    lis = [[num] for num in sequence]

    for i in range(1, n):
        for j in range(i):
            if sequence[i] >= sequence[j] and len(lis[i]) < len(lis[j]) + 1:
                lis[i] = lis[j] + [sequence[i]]

    max_length = 0
    best_subsequence = []
    for subsequence in lis:
        if len(subsequence) > max_length:
            max_length = len(subsequence)
            best_subsequence = subsequence

    return best_subsequence


def main():
    sequence = list(map(int, input().split(', ')))
    best_subsequence = find_lis(sequence)
    print(' '.join(map(str, best_subsequence)))


if __name__ == "__main__":
    main()

