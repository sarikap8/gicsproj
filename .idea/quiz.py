# Import package and api and modules
import wikipedia
import re
import operator
flower_list= ['Nelumbo nucifera','rose','Bellis perennis', 'Helianthus']

flower_dict={}
print("Analyzing current flowers, then your quiz will begin! Sit tight!")
#function to get wikipedia info for a given lfower input
def getwiki_info(flower):
    wiki = wikipedia.page(flower)
    # Extract the plain text content of the page, replacing all non plain text characters
    text = wiki.content
    text = text.replace('\n', '')
    text = re.sub(r'==.*?==+', '', text)
    flower_dict[flower]=text
    print (text)


flower_text = {
    "lotus": "Nelumbo nucifera",
    "rose": "rose",
    "daisy": "Bellis perennis",
    "sunflower":"Heliantus"
}

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


def offer_menu_to_get_list_of_choices(prompt, dictionary): #quiz code that takes in prompts (questions) and dictionaries (of responses) as parameters

    print (prompt)
    for key in dictionary:
        print(key, dictionary[key][0]) #print corresponding options (doesn't print associated flower to user)

    while True: #forever loop for error handling: if input does not match key in dictionary, then everything from underneath will run again endlessly
        menu_choice = input('Enter the Number of Your Choice' + '-> ') #display prompt

        try:
            menu_choice = int(menu_choice) # convert input to string
        except ValueError: #error handling exception:
            print("Oops!  'Your input has to be an integer on the list. Try again... ->")

        if menu_choice in list(dictionary.keys()): #convert dictionary into a list and iterate through it
            print('----------------------------')
            return dictionary[menu_choice][1]
            #get second corresponding value (flower returned that is hidden frmo public. )
        print('Pick one of the choices you were given.') #error handling

result_lst =[] #list of answers
clr = offer_menu_to_get_list_of_choices("What's your favorite color?", color) #parameters from above
result_lst.append(clr)
aml = offer_menu_to_get_list_of_choices("What's your favorite animal?", animal)
result_lst.append(aml)
fd = offer_menu_to_get_list_of_choices("What's your favorite food?", food)
result_lst.append(fd)
sub = offer_menu_to_get_list_of_choices("What's your favorite school subject?", subject)
result_lst.append(sub)
dy = offer_menu_to_get_list_of_choices("What's your favorite day of the week?", day)
result_lst.append(dy)

#print (result_lst) debug

res_count_dict={}

for res in result_lst:
    if not res in res_count_dict:
        res_count_dict[res] = 1
    else:
        res_count_dict[res] += 1

print(res_count_dict)


max_opt=max(res_count_dict.items(), key=operator.itemgetter(1))[0]
print("Congratulations, you are most similar to a " + max_opt + "! Here is some information from wikipedia about your assigned flower")
getwiki_info(max_opt)
#get maximum
