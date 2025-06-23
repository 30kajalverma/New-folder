marks = {
    "Harry": 100,
    "shubham":56,
    "rohan": 36,
    0: "Harry"
}
# method number 1
# print(marks.items()) # output: key values tuple ki form m milenge

#method no.2
# print(marks.keys())

# method no. 3
# print(marks.values())

#method no.4
#marks.update({"Harry": 99, "Renuka":100})
#print(marks)

# another method 5
# dono m difference kya h?
# print(marks.get("Harry"))
# print(marks["Harry"]) # dono hi 100 marks dengi
# pr agr "Harry2" kr de to niche wale m eror ayega 

print(marks.get("Harry2")) # prints none
# print(marks["Harry2"]) # returns an error

# More methods are available on docs.python.org

# u can use more methods from chatgpt


  