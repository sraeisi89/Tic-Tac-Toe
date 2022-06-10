def read_file(file_name):
    with open(file_name) as file:
        lines = []
        rows = file.readlines()
        for line in rows:
            lines.append(line.strip())
        return lines

def get_columns(list_rows):
    columns = []
    for i in range(len(list_rows)):
        column = ""
        for item in list_rows:
            column += item[i]
        columns.append(column)
    return columns

def get_diagonals(list_rows):
    diagonals = []
    diagonal_1 = ""
    rows_number = len(list_rows)
    for i in range(rows_number):
        diagonal_1 += list_rows[i][i]
    diagonals.append(diagonal_1)

    diagonal_2 = ""
    for i in range(rows_number):
        diagonal_2 += list_rows[i][(rows_number - 1) - i]
    diagonals.append(diagonal_2)
    return diagonals

def get_winner(final_list):
    for i in final_list:
        if i.count(i[0]) == len(i):
            return i[0]
    return "Draw"

def tic_tac_result(filename):
    rows = read_file(filename)
    return get_winner(rows + get_columns(rows) + get_diagonals(rows))





print(tic_tac_result("win-o.txt"))
# Should print "O"

print(tic_tac_result("win-x.txt"))
# Should print "X"

print(tic_tac_result("draw.txt"))
# Should print "Draw"