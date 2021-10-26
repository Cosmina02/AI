import random
import copy
final_colors = [[], [], []]
culori_asign = list()
region_list = ['WA', 'SA', 'NT']  # lista cu regiunile

# lista cu culorile fiecarei regiuni
# poz_i din lista de culori corespunde regiunii_i din lista de regiuni
colors_list = [['R', 'G', 'B'], ['R', 'G'], ['G']]

# o lista cu adiacenta intre regiuni
region_adjacency = {
    'WA': ['SA', 'NT'],
    'SA': ['WA', 'NT'],
    'NT': ['WA', 'SA']
}
# exemplul 2
final_colors2 = [[], [], [], [], [], [], []]
region_list2 = ['T', 'WA', 'SA', 'NT', 'Q', 'NSW', 'V']
colors_list2 = [['R', 'B', 'G'], ['R'], ['R', 'B', 'G'], ['R', 'B', 'G'], ['G'], ['R', 'B', 'G'], ['R', 'B', 'G']]
region_adjacency2 = {
    'T': ['V'],
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'Q', 'SA'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW', 'T']
}

# verifica daca 2 regiuni sunt vecine si returneaza true sau false
def is_consistent(region1, region2, color1, region_adj, colors, regions):
    for region, neighbours in region_adj.items():
        if region == region1 and neighbours.__contains__(region2):
            return colors[regions.index(region2)].__contains__(color1)

# verifica daca o regiune nu mai are culori disponibile
def is_empty(colors, regions, region):
    if len(colors[regions.index(region)]) > 0:
        return False
    return True


def forward_checking(r, c, r_index, region_adj):
    while is_empty(c, r, r[r_index]) is False: # cat timp regiunea cu indexul r_index mai are culori disponibile
        c2 = copy.deepcopy(c)

        color = random.choice(c[r.index(r[r_index])])  # ia random o culoare din lista de culori a regiunii i
        color = ' '.join(color)  # transforma culoarea din lista in string(pentru a putea fi folosita mai departe)

        c[r_index].remove(color)
        empty_domain = False
        i = 0
        for k in range(0, len(r)):
            for b in c[r.index(r[k])]:
                if is_consistent(r[r_index], r[k], color, region_adj, c, r):
                    c[k].remove(color)
            # verifica daca odata cu eliminarea culorii color regiunea k va ramane fara nicio culoare disponibila daca
            # nu este regiunea curenta
            if k != r_index and is_empty(c, r, r[k]):
                empty_domain = True
                i = k
                break
        if empty_domain and (i not in culori_asign):
            c = copy.deepcopy(c2)  # reseteaza vectorul de culori
        else:
            culori_asign.append(r_index) # adauga vectorul cu regiunile care au primit o culoare
            return color

#  verifica daca am ajuns la o solutie in care toate regiunile au primit o culoare
def is_final(color_list):
    print("Current color list: ", color_list)
    for c in color_list:
        if len(c) != 0:
            return False
    return True

# returneaza indexul regiunii cu cele mai putine culori de unde putem alege
def get_index_least_constraint(colors):
    smallest = -1
    region_index = -1
    for x in colors:
        if (smallest > len(x) or smallest == -1) and len(x) != 0:
            smallest = len(x)
            region_index = colors.index(x)
    return region_index


def mrv_alg(regions, colors, region_adj, final):
    while is_final(colors) is False:
        region_index = get_index_least_constraint(colors)
        if region_index != -1:
            color = forward_checking(regions, colors, region_index, region_adj)
            print("Chosen color", color)
            if color is not None:
                final[region_index] = color
            else:
                break
    return final

# verifica daca razultatul este unul valid
def check_answear(final,region_adj,regions):
    for region, neighbours in region_adj.items():
        for neighbour in neighbours:
            if final[regions.index(region)] == final[regions.index(neighbour)]:
                return False
    return True


if __name__ == '__main__':
    # Exemplul1:

    mrv_alg(region_list, colors_list, region_adjacency, final_colors)
    print("\nFound solution after MRV algorithm:", final_colors)
    if check_answear(final_colors, region_adjacency, region_list) is False:
        print("The solution is not valid")
    else:
        print("The solution is valid")

    print("\n\n")
    # Exemplul 2
    mrv_alg(region_list2, colors_list2, region_adjacency2, final_colors2)
    print("\nFound solution after MRV algorithm:", final_colors2)
    if check_answear(final_colors2, region_adjacency2, region_list2) is False:
        print("The solution is not valid")
    else:
        print("The solution is valid")

