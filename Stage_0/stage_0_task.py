
# First, we organize the information of the team members using a clear data structure (dictionary).
# Each dictionary contains personal details for a specific team member.

MuniruElijah_info = {
    "Name": "Muniru Elijah Taiwo",
    "Slack Username": "MuniruElijah",
    "Email": "muniruelijah@gmail.com",
    "Hobby": "Reading",
    "Country": "Nigeria",
    "Discipline": "Anatomy",
    "Preferred Programming Language": "R"
}

Lase_info = {
    "Name": "Toluwalase Taiwo",
    "Slack Username": "Lase",
    "Email": "princesstoluwalase@gmail.com",
    "Hobby": ["Watching movies", "Sleeping"],
    "Country": "Nigeria",
    "Discipline": "Microbiology",
    "Preferred Programming Language": "Python"
}

NeoMametja_info = {
    "Name": "Neo Mokgadi Mametja",
    "Slack Username": "NeoMametja",
    "Email": "nmametja@gmail.com",
    "Hobby": ["Outdoor activities", "Gym", "Sleeping"],
    "Country": "South Africa",
    "Discipline": "Plant Biotechnology",
    "Preferred Programming Language": "Python"
}

Sproff_info = {
    "Name": "Samuel Ogunleye",
    "Slack Username": "Sproff",
    "Email": "hellodevsproff@gmail.com",
    "Hobby": "Music",
    "Country": "Nigeria",
    "Discipline": "Biochemistry",
    "Preferred Programming Language": "Python"
}

Stella_info = {
    "Name": "Stella Adediwura",
    "Slack Username": "Stella",
    "Email": "ifeoluwastella02@gmail.com",
    "Hobby": ["Sleeping", "Reading", "Watching movies", "Surfing the Internet"],
    "Country": "Nigeria",
    "Discipline": "Microbiology",
    "Preferred Programming Language": "Python"
}

Elias_info = {"Name":"Elias Korchi Meziani",
"Slack Username": "Elias",
"Email": "elias.k.meziani@gmail.com",
"Hobby": ["Videogames", "History", "Life Sciences", "Gym", "Sleeping"],
"Country": "Spain",
"Discipline": "Pharmacy",
"Prefered programming language": "Python"} 

# To allow structured access to the information, we store all individual dictionaries
# inside a larger dictionary called Team_Histidine.

Team_Histidine = {'NeoMametja_info': NeoMametja_info, 
                  'Sproff_info': Sproff_info, 
                  'Stella_info': Stella_info, 
                  'MuniruElijah_info': MuniruElijah_info,
                  'Lase_info': Lase_info,
                  'Elias_info': Elias_info}

# This structure enables us to retrieve all information about a specific team member

print(Team_Histidine["Lase_info"])

# Or access only a particular piece of data using dictionary keys.

print(Team_Histidine["Stella_info"]["Name"])
