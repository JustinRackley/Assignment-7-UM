fname = input("Enter file name: ")
fhand = open(fname)
count = 0
con_val = 0
for file in fhand :
    if file.startswith("X-DSPAM-Confidence:"):
        count += 1
        index_start = file.find('0')
        index_stop = file[index_start : ]
        current_con_val = float(index_stop)
        con_val += current_con_val
con_avg = (con_val / count)


print('Average spam confidence:',con_avg)