
def eval_loop():
    user = input("Please enter values and enter done when finished: ")
    while user != "done" and user != "DONE":
        user = eval(user)
        print(user)
        if user == "done" and user == "DONE":
            break
        user = input("Please enter values and enter done when finished: ")
        
eval_loop()
    