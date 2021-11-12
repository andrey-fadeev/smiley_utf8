output = "smiley_raw.txt"

indexes0 = [bytearray.fromhex(hex(i)[2:].zfill(2)) for i in range(240, 241)]
indexes1 = [bytearray.fromhex(hex(i)[2:].zfill(2)) for i in range(159, 160)]
indexes2 = [bytearray.fromhex(hex(i)[2:].zfill(2)) for i in range(128, 192)]
indexes3 = [bytearray.fromhex(hex(i)[2:].zfill(2)) for i in range(128, 192)]

items = b''
for index0 in indexes0:
    for index1 in indexes1:
        for index2 in indexes2:
            for index3 in indexes3:
                items += index0
                items += index1
                items += index2
                items += index3
                items += b'\n'

items = items[:5*2775]
total_count = len(items) // 5
with open(output, "wb") as w:
    w.write(items)

print("Content generated:", open(output, "r").read())
print(f"Total count: {total_count}")
