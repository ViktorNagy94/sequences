available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd drive"
                   ]
current_choice = "-"
computer_parts = [] #create an empty list
                        #valid_choices = [str(i) for i in range(1,len(available_parts) +1)]
valid_choices = []
for i in range(1,len(available_parts) + 1):
    valid_choices.append(str(i))
#ez a for hozzáadja a lehetséges megfelelő választásokat a változónkhoz ami ennek vizsgálatára jött létre.

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            #it's already in so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below")
        for number, part in enumerate(available_parts):
           print("{0}: {1}".format(number + 1,part))

    current_choice = input()

print(computer_parts)