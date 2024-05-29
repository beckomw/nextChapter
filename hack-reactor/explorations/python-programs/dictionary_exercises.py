

# continents_countries = {
#   "Asia":["China", "Mongolia", "India"],
#   "South America": ["Brazil", "Argentina", "Chile"],
#   "North America": ["United States", "Canada", "Mexico"], "Antarctica": [],
#   "Africa": ["South Africa", "Algeria", "Kenya", "Ethiopia", "Egypt"],
#   "Europe": ["France", "Germany", "England", "Spain", "Greece", "Italy"],
#   "Australia": ["New Zealand", "Australia", "Fiji"]
#   }


# print(continents_countries["Asia"])

# print(continents_countries["Australia"][2])

# keys = continents_countries.keys()
# sorted_continents = sorted(keys)

# print(sorted_continents)


# attributes  = { 
#     "first_name": "Wally",
#     "last_name": "McCrea",
#     "years_experience": 4,
#     "role": "graphic designer"
# }


# print("The candidate", attributes["first_name"] ,attributes["last_name"], "has" ,attributes["years_experience"], "years of experience as a ", attributes["role"], ".")


my_dict = {"a":1, "b":2, "c":3 }

new_dict = {}
for key in my_dict: 
    new_dict[key] = my_dict[key] ** 2


print(new_dict)