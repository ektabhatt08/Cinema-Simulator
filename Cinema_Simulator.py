
# Films = {Available Film name : [age, availability of ticket]

Films = {"Finding Dary" :[3,5],
         "Bourne" :[18,5],
         "Tarzan" :[15,5],
         "Ghost Blusters" :[12,5]
         }

while True:

    Choice = input("What film would you like to watch? : ").strip().title()

    if Choice in Films:

        if Films[Choice][1]== 0:
            print("We are sold out")
        else:
            age = int(input("How old are you?: ").strip())
            if age >= Films[Choice][0]:
                if Films[Choice][1]>0:
                    print("Enjoy the film..!!")
                    Films[Choice][1] = Films[Choice][1]-1
                else:
                    print("We are sold out")
            else:
                print("You are too young to see that film.")
    else:
        print("We don't have that film")

   
        
            

