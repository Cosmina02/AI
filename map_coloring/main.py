
region_list = ['WA', 'SA', 'NT']  # lista cu regiunile

# lista cu culorile fiecarei regiuni
# poz_i din lista de culori corespunde regiunii_i din lista de regiuni
colors_list = [{'R', 'G', 'B'}, {'R', 'G'}, {'G'}]

# o lista cu adiacenta intre regiuni
region_adjacency = {
                    'WA': {'SA', 'NT'},
                    'SA': {'WA', 'NT'},
                    'NT': {'WA', 'SA'}
                    }


def is_consistent(region1, region2, color1):
    for region, neighbours in region_adjacency.items():
        if region == region1 and neighbours.__contains__(region2):
            return colors_list[region_list.index(region2)].__contains__(color1)


def remove_color(region, color):
    colors_list[region_list.index(region)].remove(color)


def is_empty(region):
    if len(colors_list[region_list.index(region)]) > 0:
        return False
    return True
