"""All about IO."""


import json
import os
import requests
import inspect
import sys

# Handy constants
LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
if LOCAL != CWD:
    print(
        f"""
    Be careful that your relative paths are
    relative to where you think they are
    LOCAL: {LOCAL}
    CWD: "CWD
    """
    )


def get_some_details():
    """Parse some JSON.

    In lazyduck.json is a description of a person from https://randomuser.me/
    Read it in and use the json library to convert it to a dictionary.
    Return a new dictionary that just has the last name, password, and the
    number you get when you add the postcode to the id-value.
    TIP: Make sure that you add the numbers, not concatinate the strings.
        E.g. 2000 + 3000 = 5000 not 20003000
    TIP: Keep a close eye on the format you get back. JSON is nested, so you
        might need to go deep. E.g to get the name title you would need to:
        data["results"][0]["name"]["title"]
        Look out for the type of brackets. [] means list and {} means
        dictionary, you'll need integer indeces for lists, and named keys for
        dictionaries.
    """
    json_data = open(LOCAL + "/lazyduck.json").read()
    import json
    # Read the JSON file
    with open('lazyduck.json', 'r') as json_file:
        data = json.load(json_file)
    
    # Extract the required information
    last_name = data["results"][0]["name"]["last"]
    password = data["results"][0]["login"]["password"]
    postcode = data["results"][0]["location"]["postcode"]
    user_id = data["results"][0]["id"]["value"]
    
    # Convert postcode and user_id to integers and compute the sum
    postcode_number = int(postcode)
    user_id_number = int(user_id)
    postcode_plus_id = postcode_number + user_id_number
    
    # Create a new dictionary with the required information
    get_some_details = {
        "last_name": last_name,
        "password": password,
        "postcode_plus_id": postcode_plus_id
    }
    
    return get_some_details


data = json.loads(json_data)
return {"lastName": None, "password": None, "postcodePlusID": None}


def wordy_pyramid():
    """Make a pyramid out of real words.

    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=20
    The generator takes a single argument, length (`wordlength`) of the word.
    Visit the above link as an example.
    Use this and the requests library to make a word pyramid. The shortest
    words they have are 3 letters long and the longest are 20. The pyramid
    should step up by 2 letters at a time.
    Return the pyramid as a list of strings.
    I.e. ["cep", "dwine", "tenoner", ...]
    [
    "cep",
    "dwine",
    "tenoner",
    "ectomeric",
    "archmonarch",
    "phlebenterism",
    "autonephrotoxin",
    "redifferentiation",
    "phytosociologically",
    "theologicohistorical",
    "supersesquitertial",
    "phosphomolybdate",
    "spermatophoral",
    "storiologist",
    "concretion",
    "geoblast",
    "Nereis",
    "Leto",
    ]
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. &wordlength=
    """

    base_url=https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=20 

    pyramid = []
    wordy_pyramid = [] 
    for i in range(3, 21, 2):
        url = base_url.format(length=1)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.text
        wordy_pyramid.append(message)
    else:
        print("failed a request", r.status_code, i)
    for i in range(20, 3, -2):
        url = base_url.format(length=i)
        r = requests.get(url) 
        if r.status_code is 200:
            message = r.text
            wordy_pyramid.append(message)
    else:
        print("failed a request", r.status_code, 1)
        return wordy_pyramid



def pokedex(low=1, high=5):
    """Return the name, height and weight of the tallest pokemon in the range low to high.

    Low and high are the range of pokemon ids to search between.
    Using the Pokemon API: https://pokeapi.co get some JSON using the request library
    (a working example is filled in below).
    Parse the json and extract the values needed.

    TIP: reading json can someimes be a bit confusing. Use a tool like
    http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
    get very long. If you are accessing a thing often, assign it to a
    variable and then future access will be easier.
    """
    import requests
    tallest_name = ""
    tallest_height = 0
    tallest_weight = 0
    for pokemon_id in range(low, high + 1):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        response = requests.get(url)
        if response.status_code == 200:
            pokemon_data = response.json()
            name = pokemon_data['name']
            height = pokemon_data['height']
            weight = pokemon_data['weight']
            if height > tallest_height:
                tallest_name = name
                tallest_height = height
                tallest_weight = weight
    return pokedex



def diarist():
    """Read gcode and find facts about it.

    Read in Trispokedovetiles(laser).gcode and count the number of times the
    laser is turned on and off. That's the command "M10 P1".
    Write the answer (a number) to a file called 'lasers.pew' in the Set4 directory.

    TIP: you need to write a string, so you'll need to cast your number
    TIP: Trispokedovetiles(laser).gcode uses windows style line endings. CRLF
    not just LF like unix does now. If your comparison is failing this
    might be why. Try in rather than == and that might help.
    TIP: remember to commit 'lasers.pew' and push it to your repo, otherwise
    the test will have nothing to look at.
    TIP: this might come in handy if you need to hack a 3d print file in the future.

    NOTE: this function doesn't return anything. It has the _side effect_ of modifying the file system
    """
    count_m10_p1 = 0
    
    with open('Trispokedovetiles(laser).gcode', 'r', newline='') as file:
        for line in file:
            if "M10 P1" in line:
                count_m10_p1 += 1
    with open('Set4/lasers.pew', 'w') as output_file:
        output_file.write(str(count_m10_p1))



if __name__ == "__main__":
    print(get_some_details())

    wp = wordy_pyramid()
    [print(f"{word} {len(word)}") for word in wp]

    print(pokedex(low=3, high=7))

    diarist()

    in_root = os.path.isfile("lasers.pew")
    in_set4 = os.path.isfile("set4/lasers.pew")
    if not in_set4 and not in_root:
        print("diarist did not create lasers.pew")
    elif not in_set4 and in_root:
        print(
            "diarist did create lasers.pew, but in the me folder, it should be in the set4 folder"
        )
    elif in_set4:
        print("lasers.pew is in the right place")

