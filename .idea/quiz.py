color = {
    1:['pink','lotus'] ,
    2:['red','rose'],
    3:['white','daisy'],
    4:['blue', 'sunflower']

}
animal = {
    1:['dog', 'sunflower'] ,
    2:['cat', 'lotus'],
    3:['shark', 'rose'],
    4:['bird', 'daisy']

}
food= {
    1:['tacos', 'rose'] ,
    2:['spring roll', 'daisy'],
    3:['pasta', 'sunflower'],
    4:['pizza', 'lotus']
}

subject= {
    1:['math', 'daisy'] ,
    2:['english', 'sunflower'],
    3:['art', 'lotus'],
    4:['music', 'rose']
}

day= {
    1:['monday', 'daisy'] ,
    2:['thursday', 'sunflower'],
    3:['wednesday', 'lotus'],
    4:['friday', 'rose']
}


def offer_menu_to_get_list_of_choices(prompt, dictionary): #menu                                  #parameters in general for the variables; will only run if these parameters are given

    print (prompt)
    for key in dictionary:
        print(key, dictionary[key][0]) # will print the Key and the  first value from the dictionary key-value. Ex : 1: ['water','fresh'] = 1 Water

    while True: #true loop means that information will always be true #also, because this is a loop, if input does not match key in dictionary, then everything from underneath will run again endlessly
        menu_choice = input('Enter the Number of Your Choice' + '-> ') #display the prompt; #"input" command means it just takes your answer after displaying prompt

        try:
            menu_choice = int(menu_choice) # Your input is considered as string, so convert it to integer to compare with the dictionary keys
        except ValueError: # try except block is added to handle if the user enters Non-numeric value as input. if you don't have the try except block, when you try to convert the non numeric value to number integer program will fail with following error. ValueError: invalid literal for int() with base 10:
            print("Oops!  'Your input has to be an integer on the list. Try again... ->")

        if menu_choice in list(dictionary.keys()): # after taking the dictionay keys convert it as a list
            #dictionary.keys() = dict_keys([1, 2, 3, 4, 5, 6])
            #list(dictionary.keys()) = [1, 2, 3, 4, 5, 6]

            #this command is saying that if the user's input matches a value from the dictionary then do the "return" command in the next step
            print ('Good Choice!')
            print('----------------------------')
            return dictionary[menu_choice][1]
            #get the value (list) for the given key (user input) from the dictionary
            #[1] gives you the second value from the value list
            #1:['water','fresh']  will return 'fresh'
            # Return command return this value to the variable which is calling this function
        print('Pick one of the choices you were given.') #because this is not indented, this means if the  input (key) does not match a value in the dictionary, then this print statement will appear


#------------------------------------------
# Execution starts from here

clr = offer_menu_to_get_list_of_choices("what's your favorite color?", color) # the stuff in parentheses here are the parameters for the menu above
aml = offer_menu_to_get_list_of_choices("What's your favorite animal?", animal)

fd = offer_menu_to_get_list_of_choices("What's your favorite food?", food)
sub = offer_menu_to_get_list_of_choices("What's your favorite school subject?", subject)
dy = offer_menu_to_get_list_of_choices("What's your favorite day of the week?", day)

print ("Your rap name is", clr, aml, fd, sub, dy + '!')