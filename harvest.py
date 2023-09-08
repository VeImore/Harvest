############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, "green", True, True, "Muskmelon")
    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')            
    crenshaw = MelonType('cren', '1996', 'green', 'False', 'False', 'Crenshaw')
    yellow_watermelon = MelonType('yw', '2013', 'yellow', 'False', 'True', "Yellow Watermelon")

    muskmelon.add_pairing("mint")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    crenshaw.add_pairing("prosciutto")
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types.append(muskmelon)
    all_melon_types.append(casaba)
    all_melon_types.append(crenshaw)
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

melon_types = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    
    for melon in melon_types:
        lst_melon = ', '.join([str(mn) for mn in melon.pairings])
        print(f"{melon.name} pairs with \n -{lst_melon}")

#print_pairing_info(make_melon_types())

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_by_code = {}

    for melon in melon_types:
        melon_by_code[melon.code] = melon

    return melon_by_code

#print(make_melon_type_lookup(make_melon_types()))
melon_by_code = make_melon_type_lookup(melon_types)

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):

        if self.shape_rating > 5 and self.color_rating > 5:
            if self.field != 3:
                return True
        return False

def make_melons(melon_by_code):
    """Returns a list of Melon objects."""

    melon1 = Melon(melon_by_code['yw'], 8, 7, 2, 'Sheila')
    melon2 = Melon(melon_by_code['yw'], 3, 4, 2, 'Sheila')
    melon3 = Melon(melon_by_code['yw'], 9, 8, 3, 'Sheila')
    melon4 = Melon(melon_by_code['cas'], 10, 6, 35, 'Sheila')
    melon5 = Melon(melon_by_code['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(melon_by_code['cren'], 8, 2, 35, 'Michael')
    melon7 = Melon(melon_by_code['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon(melon_by_code['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(melon_by_code['yw'], 7, 10, 3, 'Sheila')

    melons = [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]

    return melons

melons = make_melons(melon_by_code)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable() == True:
            print(f'Harvested by {melon.harvester} from Field {melon.field} (CAN BE SOLD)')
        else:
            print(f'Harvested by {melon.harvester} from Field {melon.field} (NOT SELLABLE)')


# get_sellability_report(melons)

melons_from_harvest = []

data = open('harvest_log.txt')
for line in data:
   #line.count()
    split_line = line.rstrip().split(" ")
    shape_rating = int(split_line[1])
    color_rating = int(split_line[3])
    field = int(split_line[11])
    harvester = split_line[8]
    melon_type =  melon_by_code[split_line[5]]
    
    melons_from_harvest.append(
        Melon(melon_type, shape_rating, color_rating, field, harvester)
    )
    
    get_sellability_report(melons_from_harvest)
    