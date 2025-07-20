attempts = 0
while attempts < 5:
    userPassword = input("Enter your password: ")

    if len(userPassword) < 8 :
        print("invalid password")
        
        attempts += 1
            
    else:
        print("valid password")
        break
