output1 = []
output = []

for i in range(5):
    row = []
    row.append(i+1)
    row.append(1)
    output1.append(row)



for i in range(5):
    row = []
    for j in range(3):
        if j == 0:
            row.append(output1[i][0]*output1[i][1])
        else:
            row.append(output1[i][0]*row[j-1])
    output.append(row)

for row in output1[:]:
    row +=(output[output1.index(row)])

for row in output1:
    print(' '.join(map(str, row)))