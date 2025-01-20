r1 = ['O','O','O']
r2 = ['O','O','O']
r3 = ['O','O','O']
matrix = [r1,r2,r3]
print(f"{r1}\n{r2}\n{r3}")
pos = input("Enter the position where to hide the money: ")
row_num = int(pos[0])
col_num = int(pos[1])
r_selected = matrix[row_num-1]
r_selected[col_num-1] = 'X'
print(f"{r1}\n{r2}\n{r3}")