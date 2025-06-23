# what will be the length of the following sets:
# s  = set()
# s.add(20)
# s.add(20.0)
# s.add('20') #lenghth of s after these operation?

s  = set()
s.add(20)
s.add(20.0) 
s.add('20')
print(len(s)) #use chatgpt to understand this question

# 20==20.0 so set m duplicate nhi hota 
# so output will be {20 , '20'}
# so length will be 2 not 3 
