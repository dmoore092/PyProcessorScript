with open("BetteDavisFilms.txt") as f:
    items = f.readlines()
    itemList = [x.strip() for x in items]
    doneList = [h.replace(".", ",").replace(",", "") for h in itemList]

year1 = doneList[1].replace("(", ",").replace(")", ",")
year2 = doneList[4].replace("(", ",").replace(")", ",")
year3 = doneList[7].replace("(", ",").replace(")", ",")

str1 = doneList[0] + "," + year1 + "," + doneList[2] + "\n"
str2 = doneList[3] + "," + year2 + "," + doneList[5] + "\n"
str3 = doneList[6] + "," + year3 + "," + doneList[8] + "\n"

print(str1)
print(str2)
print(str3)

outFile = file("Q5_output.csv", 'w')
outFile.writelines(str1)
outFile.writelines(str2)
outFile.writelines(str3)

outFile.close()
