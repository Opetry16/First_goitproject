def formatted_numbers():
    lines = []
    header = "|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary')
    lines.append(header)
    for i in range(16):
        decimal = f"{i:<10d}"
        hex_value = f"{i:^10X}"
        binary = f"{i:>10b}"
        row = f"|{decimal}|{hex_value.lower()}|{binary}|"
        lines.append(row)
    return lines

for el in formatted_numbers():
    print(el)