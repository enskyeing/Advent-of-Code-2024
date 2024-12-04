import re
import pprint


def get_data():
    with open(file="./Day-3/Puzzle-Input.txt", mode="r") as pi:
        return pi.read().replace("\n", "")


def part_one(memory) -> int:
    answer = 0
    multiplies = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)

    for multiply in multiplies:
        number_1, number_2 = map(int, re.search(r'\((.*?)\)', multiply).group(1).split(","))
        answer += number_1 * number_2
    
    return answer


def part_two(memory) -> int:
    answer = 0
    dos = memory.split("do()")
    multiplies = []

    for conditional in dos:
        if dos.index(conditional) == len(dos) -1 and "don't()" not in conditional:
            found_multiplies = re.findall(r"mul\(\d{1,3},\d{1,3}\)(?=[\s\S]*(?:$))", conditional)
        elif "don't()" not in conditional:
            found_multiplies = re.findall(r"mul\(\d{1,3},\d{1,3}\)(?=[\s\S]*(?:$))", conditional)
        elif conditional.count("don't()") > 1:
            new_conditional = conditional.split("don't()")[0]
            found_multiplies = re.findall(r"mul\(\d{1,3},\d{1,3}\)(?=[\s\S]*(?:$))", new_conditional)
        else:
            found_multiplies = re.findall(r"mul\(\d{1,3},\d{1,3}\)(?=[\s\S]*(?:don't\(\)))", conditional)
        multiplies.extend(found_multiplies)
    
    for multiply in multiplies:
        number_1, number_2 = map(int, re.search(r'\((.*?)\)', multiply).group(1).split(","))
        answer += number_1 * number_2

    return answer


if __name__ == "__main__":
    memory = get_data()
    print("Part One: ", part_one(memory=memory))
    print("Part Two: ", part_two(memory=memory))