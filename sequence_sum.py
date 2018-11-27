def sequence_sum(begin_number, end_number, step):
    sum = 0
    if begin_number > end_number:
        sum = 0
    for i in range(begin_number, (end_number + 1), step):
        sum = sum + i
        i += step
    if begin_number == end_number:
        sum = begin_number
    return sum

def main():
    sum = sequence_sum(16, 15, 3)
    print(sum)

if __name__ == "__main__":
    main()