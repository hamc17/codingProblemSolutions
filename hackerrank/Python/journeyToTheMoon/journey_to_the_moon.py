from collections import defaultdict


"""
   Problem:
   "The member states of the UN are planning to send 2 people to the moon.
    They want them to be from different countries.
    You will be given a list of pairs of astronaut id's.
    Each pair is made of astronauts from the same country.
    Determine how many pairs of astronauts from different countries
    they can choose from."
"""

# Step explanation:
# - Take in values
# - Begin getting total number of pairs possible
# - Create bidirectional dict for astronaut pairs
# - Create dict to verify if astronaut has been checked
# - For each key that hasn't been checked, get their complete country
#  - Get its values, remove it from the value list, add its values
# to the value list
#    (This allows for retrieval of all values for a "country"
# without recursing; retrieve iteratively)
# - Once all countries gathered, get the total count of possible combos
#  - Remove all single astronaut countries from the list of countries
# and increment solo counter
#  - Get total for countries with more than one member by adding:
#    [length(i) * length(j) {i, 0, length of country list},
#       {j, i + 1, length of country list}]
#  - Get total for countries with one member by adding:
#    [1 * (solo - i) {i, 0, solo}]
#  - return the total
# - print & done


def get_pairs(n, astronauts):
    """Gets the total number of possible pairs where each pair contains
    an astronaut for a different country for a list of
    astronaut - astronaut same country pairings.

    Arguments:
        n {integer} -- The number of astronauts.
        astronauts {list} -- A list of astronaut pairs.

    Returns:
        integer -- The total number of possible different country
        astronaut pairs.
    """

    countries = []
    checklist = []
    solo = 0
    total = 0
    pair_dict = {k: [] for k in range(n)}
    checked = {k: False for k in range(n)}

    for pair in astronauts:
        pair_dict[pair[0]].append(pair[1])
        pair_dict[pair[1]].append(pair[0])
    for astronaut in pair_dict.keys():
        if not checked[astronaut]:
            countries.append(new_country(astronaut, pair_dict, checked))
            if len(countries[-1]) == 1:
                solo += 1
                del countries[-1]

    for i in range(len(countries)):
        total += len(countries[i]) * solo
        for j in range(i + 1, len(countries)):
            total += len(countries[i]) * len(countries[j])
    for i in range(1, solo):
        total += 1 * (solo - i)

    return total


def new_country(astronaut, pair_dict, checked):
    """Gets the complete country for an astronaut key;
    list of all astronauts that share the same country.

    Arguments:
        astronaut {integer} -- The astronaut ID.
        pair_dict {dict} -- A dict containing astronaut ID pairs.
        checked {dict} -- A dict indicating if an astronaut ID has
        been checked already.

    Returns:
        list -- A list containing all IDs in the same country.
    """

    values = pair_dict[astronaut]
    country = [astronaut]
    checked[astronaut] = True

    while values:
        v = values[-1]
        if not checked[v]:
            new_vals = [i for i in pair_dict[v] if i not in values]
            country.append(v)
            checked[v] = True
            del values[-1]
            values.extend(new_vals)
        else:
            del values[-1]

    return country
