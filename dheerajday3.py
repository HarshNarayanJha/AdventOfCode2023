with open("input3.txt") as fp:
    data = fp.read()
    schematic = data.replace("\r", "").replace("\n", "")

SYMBOLS = "@#$%&*-+?=/"
LINELENGTH = 140
s = []


def check(i, length):
    try:
        if schematic[i-1] in SYMBOLS:
            print(
                f"left {schematic[i-1]}",
            )
            return True
    except IndexError:
        pass
    try:
        if schematic[i + length] in SYMBOLS:
            # print(
            #     schematic[i:i+length+1]
            #     # schematic[i + length + 1] in SYMBOLS
            # )
            print(
                f"right {schematic[i+length+1]}",
            )
            return True
    except IndexError:
        pass

    for j in range(i, i + length-1):
        for dl in range(-1, length+1):
            try:
                if schematic[j - LINELENGTH + dl] in SYMBOLS:
                    print(
                        f"up {schematic[j-LINELENGTH+dl]}",
                    )
                    return True
            except IndexError:
                pass

            try:
                if schematic[j + LINELENGTH + dl] in SYMBOLS:
                    print(
                        f"down {schematic[j+LINELENGTH-dl]}",
                    )
                    return True
            except IndexError:
                pass

    print("no symbol found")
    return False


cur = 0
while cur < len(schematic):
    if schematic[cur].isdigit():
        start = cur
        cur += 1
        while schematic[cur].isdigit():
            cur += 1
        num = int(schematic[start:cur])
        l = len(str(num))
        print(num, start, l, end="  ---  ")
        if check(start, l):
            s.append(num)
    cur += 1
print(sum(s))