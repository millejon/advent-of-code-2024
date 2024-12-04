# Day 1: Historian Hysteria


def prepare_lists(data: str) -> tuple[list[int], list[int]]:
    list1, list2 = [], []

    with open(data, encoding="utf-8") as input:
        for line in input:
            x, y = line.split()
            list1.append(int(x))
            list2.append(int(y))

    list1.sort()
    list2.sort()

    return list1, list2


def calculate_distance(list1: list, list2: list) -> int:
    distance = 0

    for pair in zip(list1, list2, strict=True):
        distance += abs(pair[0] - pair[1])

    return distance


def calculate_similarity(list1: list, list2: list) -> int:
    similarity = 0

    for number in list1:
        similarity += number * list2.count(number)

    return similarity


def compare_lists(list1: list, list2: list) -> None:
    distance = calculate_distance(list1, list2)
    similarity = calculate_similarity(list1, list2)

    print(f"Total distance is {distance}.")
    print(f"Similarity score is {similarity}.")


if __name__ == "__main__":
    list1, list2 = prepare_lists("input.txt")
    compare_lists(list1, list2)
