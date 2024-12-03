def get_data():
    with open(file="./Day-2/Puzzle-Input.txt", mode="r") as pi:
        return pi.readlines()


def part_one(reports: list) -> int:
    safe_reports = 0
    for report in reports:
        if sorted(report) == report or sorted(report, reverse=True) == report:
            safe_report = True
            for i, level in enumerate(report):
                if i > 0:
                    if 0 < abs(level - report[i-1]) < 4:
                        safe_report = True
                    else:
                        safe_report = False
                        break
            if safe_report:
                safe_reports += 1
    return safe_reports


def part_two(reports: list) -> int:
    safe_reports = 0

    for report in reports:
        safe_report = True
        current_report = report
        for n in range(len(report) + 1):
            if n > 0:
                current_report = report[:n-1] + report[n:]
            
            # Check if report is in descending or ascending order
            if sorted(current_report) == current_report or sorted(current_report, reverse=True) == current_report:
                # if it is, then check if the difference between each adjacent number is between 1 and 3
                for i, level in enumerate(current_report):
                    if i > 0:
                        if 0 < abs(level - current_report[i-1]) < 4:
                            safe_report = True
                        # If it's not, then report is unsafe
                        else:
                            safe_report = False
                            break
                if safe_report:
                    safe_reports += 1
                    break

    return safe_reports
            

if __name__ == "__main__":
    reports = [list(map(int, line.strip().split())) for line in get_data()]
    print("safe reports 1: ",part_one(reports=reports))
    print("safe reports 2: ", part_two(reports=reports))
