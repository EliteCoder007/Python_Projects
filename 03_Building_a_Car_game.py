commad = ""
started = False
while True:
    commad = input("> ").lower()
    if commad == "start":
        if started:
            print("Car is alreafy started!")
        else:
            started = True
            print("Car started... ")
        
    elif commad == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stoped.")
    elif(commad == "help"):
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        
        """)
    elif commad == "quit":
        break
    else:
        print("Sorry, I don't understand that! ")
    
