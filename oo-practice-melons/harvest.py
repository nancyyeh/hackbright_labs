############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    cas.add_pairing('mint')
    cas.add_pairing('strawberries')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"-{pairing}")
        print("")

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon
        # melon_dict[melon.code] = melon_dict.get(melon, {})
        # melon_dict[melon.code]['first_harvest'] = melon.first_harvest
        # melon_dict[melon.code]['color'] = melon.color
        # melon_dict[melon.code]['is_seedless'] = melon.is_seedless
        # melon_dict[melon.code]['is_bestseller'] = melon.is_bestseller
        # melon_dict[melon.code]['name'] = melon.name
        # melon_dict[melon.code]['pairing'] = melon.pairings

    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, 
                harvested_from_field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from_field = harvested_from_field
        self.harvested_by = harvested_by

        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from_field != 3:
            self.is_sellable = True
        else:
            self.is_sellable = False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    all_melons_objects = []

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    all_melons_objects.append(melon_1)

    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    all_melons_objects.append(melon_2)

    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    all_melons_objects.append(melon_3)

    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    all_melons_objects.append(melon_4)

    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    all_melons_objects.append(melon_5)

    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    all_melons_objects.append(melon_6)

    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    all_melons_objects.append(melon_7)

    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    all_melons_objects.append(melon_8)

    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    all_melons_objects.append(melon_9)

    return all_melons_objects


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



    for melon_harvested in melons:
        if melon_harvested.is_sellable:
            sold_text = '(CAN BE SOLD)'
        else:
            sold_text = '(NOT SELLABLE)'    
        print(f"Harvested by {melon_harvested.harvested_by} from Field {melon_harvested.harvested_from_field} {sold_text}")


