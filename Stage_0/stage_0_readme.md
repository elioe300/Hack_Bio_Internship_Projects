# Team Histidine Information Organizer

## Overview
This Python project organizes and stores information about Team Histidine's members using Python dictionaries.

## Features
- Stores detailed information about each team member.
- Uses a structured dictionary format for organization.
- Allows easy retrieval of individual and specific details.

## Data Structure
Each member's details, including name, email, country, discipline, and preferred programming language, are stored in individual dictionaries in a dictionary format as follows:

```python
MuniruElijah_info = {
    "Name": "Muniru Elijah Taiwo",
    "Slack Username": "MuniruElijah",
    "Email": "muniruelijah@gmail.com",
    "Hobby": "Reading",
    "Country": "Nigeria",
    "Discipline": "Anatomy",
    "Preferred Programming Language": "R"
}
```

All individual dictionaries are then stored within a master dictionary called `Team_Histidine`:

```python
Team_Histidine = {
    'NeoMametja_info': NeoMametja_info,
    'Sproff_info': Sproff_info,
    'Stella_info': Stella_info,
    'MuniruElijah_info': MuniruElijah_info,
    'Lase_info': Lase_info,
    'Elias_info': Elias_info
}
```

## Usage
To retrieve information about a specific team member, you can access their dictionary from `Team_Histidine`:

```python
print(Team_Histidine["Lase_info"])
```

To get a specific detail, such as a name:

```python
print(Team_Histidine["Stella_info"]["Name"])
```

## Requirements
- Python 3.x

## License
This project is open-source and available under the MIT License.

