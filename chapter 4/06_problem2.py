# write a program to accept marks of 6 students and display them in a appended manner
# shortcut to select multiple to cahnge ctrl+f2 ya fr double tap on wrd ,right click, then change all occurences
marks = []

f1 = int(input("Enter marks here: "))
marks.append(f1)
f2 = int(input("Enter marks here: "))
marks.append(f2)
f3 = int(input("Enter marks here: "))
marks.append(f3)
f4 = int(input("Enter marks here: "))
marks.append(f4)
f5 = int(input("Enter marks here: "))
marks.append(f5)
f6 = int(input("Enter marks here: "))
marks.append(f6)
marks.sort()
print(marks) 
# if ap value rkho
#23
#234
# 6
# 323
# 64
# 645 to hum jb run krenge sorted nhi dikhenge so for that hum int(input k aage intlgayenge kuki vo string h or hum use normal integer m convert krenge
