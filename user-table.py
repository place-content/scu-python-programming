filename = "scores.txt"

def parse_line(line):
    line = line.strip()
    if not line:
        return []
    if ',' in line:
        return [item.strip() for item in line.split(',')]
    else:
        return line.split()

with open(filename, 'r', encoding='utf-8') as file:
    print(f"{'학번':<10} {'이름':<6} {'국어':<4} {'영어':<4} {'수학':<4}")
    print("-" * 32)

    buffer = []

    for line in file:
        parts = parse_line(line)

        if len(parts) == 5:
            grade, name, kor, eng, math = parts
            print(f"{grade:<10} {name:<6} {kor:<4} {eng:<4} {math:<4}")
        elif 0 < len(parts) < 5:
            buffer.extend(parts)
            if len(buffer) == 5:
                grade, name, kor, eng, math = buffer
                print(f"{grade:<10} {name:<6} {kor:<4} {eng:<4} {math:<4}")
                buffer = []
        else:
            continue
