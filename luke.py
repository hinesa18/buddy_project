#Entry code for first scene
scene_one_entry = print("As you walk down the road you encounter a mysterious forest, what will you do?")

scene_one_opta = ("(a) Enter")
scene_one_optb = ("(b) Turn around")

scene_one_entra = (input("> "))

if scene_one_entra == "A" or "a":
    print("If you wish")

elif scene_one_entra == "B" or "b":
    #End code

#End of start******continue with scene one game code******

#Entry code for second scene
scene_two_entry = print("You've made it out of the forest. Your journey continues, theirs a fork in the road do you go left or right?")

scene_two_opta = ("(a) left")
scene_two_optb = ("(b) right")

scene_two_entra = (input("> "))

if scene_two_entra == "A" or "a":
    #(Enter code) scene_two_a = first scene two option

    elif scene_two_entra == "B" or "b":
    #(Enter code) scene_two_b = second scene two option

    else:
        #Insert end code here

#End of scene two entry for now*************** Need to create both scenes

scene_three_entry = print("The path comes to a hault on a river bank. The water looks dangerously rough, how will you get across?")

scene_three_opta = (input("(a) The rocks sticking out of the water"))
scene_three_optb = (input("(b)Try to find a way around"))
scene_three_optc = (input("(c) Sit and wait for help"))
                    
scene_three_entra = (input("> "))

if scene_three_entra == "A" or "a":
    #(Enter code) scene three
elif scene_three_entra == "B" or "b":
    #(Random number generator 1-20) if num >= 15 (Enter code) scene three

else:
    print("You died in the wilderness" + #End code)