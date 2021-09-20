while True:
    # Introduction to player prompt
    answer = input("Hello, My name is Han-Tyumi")

    if answer.lower().strip() == "hello":

        # Start of game
        answer = input("You were held captive by lords of lighting in a flying castle. You lift your face out of the dry sand to take in your surroundings. Do you look left, or right first?").lower().strip()
        
        # Player Picked Left
        if answer == "left":
            answer = input("You glimspe upon a forest, your vision is still blurry. But you are certain you see a dark figure lurking behind the trees. Do you want to seek the figure?")

            if answer == "yes":
                print("You stood up, waking at the unknown in the woods. Suddenly, you feel a sharp pain in your chest, your body is in grave pain, muscles are expanding. You become enraged with hate, hair rapidly grows out of every pore. You drop onto your knees, seeing the nails of your fingers grow into black claws. You became half-man, half-bear. You are the Altered Beast. You now kill for sport.")

            else:
                print("You dismiss the thought of pursuing the unknown, after all, you just fell from a high place and hit your head pretty hard. It could just be an hallucination.")

        # Player Picked Right
        elif answer == "right":
                print("You gaze upon the blazing horizon of the desert. You see nothing but heatwaves, until something catches your eye. A rattlesnake slithers rapidly towards you in a frenzy, it was time to meet your end with the devil's serpent.")

        # Player Didn't Chose Left Or Right
        else:
            print("You chose against your instances and thought to seek the river nearby. You start to feel faint over the sound of the current crashing against the rocks. You begin to drift into sleep.")

    else:
        print("I will have, a lonely death")
    break