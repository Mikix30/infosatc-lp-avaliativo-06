inputt = int(input("Qual o número? "))
listt = [1,2,3,4]

if inputt < 0: 
    listt[3] = listt[2]

    listt[2] = listt[1]
    
    listt[1] = listt[0]
    
    del listt[0]
    
    listt.insert(0,"4")
    
    print(listt) 


elif inputt > 0: 

    listt[0] = listt[1]

    listt[1] = listt[2]

    listt[2] = listt[3]

    del listt[3]

    listt.insert(3,"1")

    print(listt) 

else: 

    print(listt)
