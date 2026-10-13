#-------STUDENTS DASHBOARD------------
import random

students_name= input("Enter Your Name: ")
students_email= input("Enter Your Email id: ")

#-----START TEST------

mcqs = [
    ["What is Python?", ["A: Programming language", "B: Snake", "C: Game", "D: Software"], "A"],
    ["Which keyword is used to define a function?", ["A: func", "B: def", "C: function", "D: define"], "B"],
    ["Which symbol is used for comments?", ["A: //", "B: #", "C: /* */", "D: --"], "B"],
    ["Which function is used to display output?", ["A: print()", "B: echo()", "C: display()", "D: out()"], "A"],
    ["What is the extension of Python files?", ["A: .py", "B: .python", "C: .pt", "D: .p"], "A"],
    ["Which operator is used for exponentiation?", ["A: ^", "B: **", "C: exp", "D: ^^"], "B"],
    ["Which loop is available in Python?", ["A: for", "B: repeat", "C: loop", "D: iterate"], "A"],
    ["Which keyword exits a loop?", ["A: stop", "B: exit", "C: break", "D: quit"], "C"],
    ["Which function returns length?", ["A: size()", "B: length()", "C: len()", "D: count()"], "C"],
    ["Which data type is immutable?", ["A: List", "B: Dictionary", "C: Tuple", "D: Set"], "C"],
    ["Which keyword is used for class?", ["A: class", "B: object", "C: def", "D: type"], "A"],
    ["Which function converts string to integer?", ["A: str()", "B: int()", "C: float()", "D: chr()"], "B"],
    ["Which operator is used for floor division?", ["A: /", "B: //", "C: %", "D: **"], "B"],
    ["Which keyword is used to import modules?", ["A: include", "B: import", "C: using", "D: module"], "B"],
    ["Which function gives absolute value?", ["A: abs()", "B: fabs()", "C: absolute()", "D: val()"], "A"],
    ["Which function gives maximum value?", ["A: max()", "B: maximum()", "C: largest()", "D: high()"], "A"],
    ["Which function gives minimum value?", ["A: min()", "B: minimum()", "C: smallest()", "D: low()"], "A"],
    ["Which function gives absolute value?", ["A: abs()", "B: fabs()", "C: absolute()", "D: val()"], "A"],
    ["Which function gives maximum value?", ["A: max()", "B: maximum()", "C: largest()", "D: high()"], "A"],
    ["Which function gives minimum value?", ["A: min()", "B: minimum()", "C: smallest()", "D: low()"], "A"],
    ["Which function converts integer to string?", ["A: str()", "B: int()", "C: chr()", "D: ord()"], "A"],
    ["Which keyword is used for inheritance?", ["A: inherit", "B: extends", "C: super", "D: class"], "D"],
    ["Which function sorts a list?", ["A: sort()", "B: sorted()", "C: arrange()", "D: order()"], "B"],
    ["Which function adds element to list?", ["A: add()", "B: insert()", "C: append()", "D: push()"], "C"],
    ["Which function removes last element?", ["A: pop()", "B: remove()", "C: delete()", "D: discard()"], "A"],
    ["Which keyword is used for exception handling?", ["A: try", "B: catch", "C: except", "D: finally"], "A"],
    ["Which keyword is used with try?", ["A: error", "B: except", "C: handle", "D: catch"], "B"],
    ["Which keyword runs code always?", ["A: end", "B: finally", "C: last", "D: close"], "B"],
    ["Which function reads input?", ["A: input()", "B: scan()", "C: read()", "D: get()"], "A"],
    ["Which function returns type?", ["A: datatype()", "B: type()", "C: typeof()", "D: class()"], "B"],
    ["Which function gives power?", ["A: pow()", "B: power()", "C: exp()", "D: **"], "A"],
    ["Which keyword defines a module?", ["A: module", "B: def", "C: class", "D: None"], "A"],
    ["Which keyword creates a generator?", ["A: yield", "B: return", "C: gen", "D: next"], "A"],
    ["Which function gives ASCII value?", ["A: ord()", "B: chr()", "C: ascii()", "D: code()"], "A"],
    ["Which function converts ASCII to char?", ["A: ord()", "B: chr()", "C: str()", "D: int()"], "B"],
    ["Which keyword is used for boolean?", ["A: bool", "B: True/False", "C: boolean", "D: logic"], "B"],
    ["Which function gives sum?", ["A: sum()", "B: total()", "C: add()", "D: plus()"], "A"],
    ["Which operator is used for modulus?", ["A: %", "B: //", "C: /", "D: **"], "A"],
    ["Which keyword is used for null?", ["A: null", "B: None", "C: empty", "D: void"], "B"],
    ["Which function gives help?", ["A: help()", "B: doc()", "C: info()", "D: manual()"], "A"],
    ["Which function gives id of object?", ["A: id()", "B: objid()", "C: identity()", "D: key()"], "A"],
    ["Which keyword is used for lambda?", ["A: lambda", "B: func", "C: def", "D: anon"], "A"],
    ["Which function gives round value?", ["A: round()", "B: approx()", "C: floor()", "D: ceil()"], "A"]   
    
]
score=0
random.shuffle(mcqs)
for question in mcqs:
    print(question[0])

    for  option in question[1]:
         print(option)

           
    answer=input("Your answer: ")

    if answer == question[2]:
         print("Correct!")                                                                                                                                                    #index is function so we use() instead of[]
         score+=1
         
    else:
         print("Wrong!")
         print("Corrrect answer is: ", question[2])

print("Total Score is: ", score,"/",len(mcqs))
         


    