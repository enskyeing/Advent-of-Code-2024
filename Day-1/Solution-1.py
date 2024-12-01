def get_data():
    with open(file="./Day-1/Puzzle-Input.txt", mode="r") as pi:
        return pi.readlines()


def part_one(list_1: list[int], list_2: list[int]) -> None:
    difference = []

    list_1.sort()
    list_2.sort()

    for i in range(len(puzzle_input)):
        difference.append(abs(list_1[i] - list_2[i]))

    print(sum(difference))

def part_two(list_1: list[int], list_2: list[int]) -> None:
    similarity_score = 0

    for id in list_1:
        similarity_score += id * list_2.count(id)
    
    print(similarity_score)


puzzle_input = get_data()
list_1 = []
list_2 = []

for line in puzzle_input:
    list_1.append(int(line.split()[0]))
    list_2.append(int(line.split()[1]))

print("Part One:")
part_one(list_1=list_1, list_2=list_2)
print("\nPart two:")
part_two(list_1=list_1, list_2=list_2)
