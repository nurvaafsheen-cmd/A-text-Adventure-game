name = input("Type your name: ")
print("Welcome,", name + ". Tonight, you enter a scary place. Be careful...")

answer = input(
    "You stand at the gate of an old graveyard. Do you go in? (yes/no): ").lower()

if answer == "yes":
    answer = input(
        "You walk past the graves. The wind is cold. You see a dark shape moving. Do you follow it or hide? (follow/hide): ").lower()

    if answer == "follow":
        answer = input(
            "You follow the shadow into a small house. The door closes behind you. Do you turn on a light or walk in the dark? (light/dark): ").lower()

        if answer == "light":
            print("The light turns on... and you see a ghost in front of you. You scream and everything goes dark.")
        elif answer == "dark":
            print("You walk in the dark. Cold hands grab you. You are pulled away. Nobody sees you again.")
        else:
            print("You stand still. The ghost finds you and takes you away.")

    elif answer == "hide":
        answer = input(
            "You hide behind a stone. You hear a voice call your name. Do you run or stay? (run/stay): ").lower()

        if answer == "run":
            print("You run to the gate, but fall. A hand comes out of the ground and pulls you down.")
        elif answer == "stay":
            print("You stay quiet. The ghost comes close and sees you. It takes you into the night.")
        else:
            print("You wait too long. The ghost finds you.")

    else:
        print("You wait. A ghost comes from the dark and takes you.")

elif answer == "no":
    answer = input(
        "You walk away. But the road is gone. There is a dark forest. Do you go in? (yes/no): ").lower()

    if answer == "yes":
        answer = input(
            "In the forest, you hear soft steps. You see a pale face behind a tree. Do you call out or keep walking? (call/walk): ").lower()

        if answer == "call":
            print("The face runs at you fast. You cannot escape.")
        elif answer == "walk":
            print("You walk fast, but the face follows. You are lost forever.")
        else:
            print("You wait. The face comes close and you are never seen again.")

    elif answer == "no":
        print("You turn back, but a small ghost blocks your way. It says, 'Stay here...' You cannot move.")
    else:
        print("You wait too long. The ground opens and you fall into the dark.")

else:
    print("You wait. A cold hand touches your back... and you are gone.")

print("Thank you for playing,", name + ". If you hear whispers tonight... don’t look back.")
