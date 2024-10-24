while(True):
    try:    
        x = input()
        print(x)
        print(float(x)**3)
    except ValueError:
        if(x == "stop"):
            print("Koncze prace")
            break
        print("Prosze wpisac liczbe typu float")
    