
#Dateizugriff
fo = open("/Users/joshualohmann/01_Data/02_Education/00_Uni/00_Vorsemesterkurs/04_Python_Listen_und_Funktionen/Programme/zahl.txt")
str1 = fo.readlines(1)
str2 = fo.readlines(2)
print(int(str1[0])+int(str2[0]))