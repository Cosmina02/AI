import random
import copy
final_colors=[[],[],[]]
culori_asign=list()
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
final_colors2=[[],[],[],[],[],[],[]]
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


def is_consistent(region1, region2, color1,region_adj,colors,regions):
    for region, neighbours in region_adj.items():
        if region == region1 and neighbours.__contains__(region2):
            return colors[regions.index(region2)].__contains__(color1)


def remove_color(region, color,regions,colors):
    colors[regions.index(region)].remove(color)


def is_empty(colors,regions,region):
    if len(colors[regions.index(region)]) > 0:
        return False
    return True


def forward_checking(r, c , r_index,region_adj):
    while is_empty(c,r,r[r_index]) is False:
        c2 = copy.deepcopy(c)
        # pentru 3.10
        a = random.choice(c[r.index(r[r_index])])  # ia random o culoare din lista de culori a regiunii i
        # pentru 3.9
        # a = random.sample(c[r.index(r[i])],1)  # ia random o culoare din lista de culori a regiunii i
        a = ' '.join(a)  # transforma culoarea din lista in string(pentru a putea fi folosita mai departe)
        # remove_color(r[r_index], a,r,c)
        c[r_index].remove(a)
        empty_domain = False
        for k in range(0, len(r)):
            for b in c[r.index(r[k])]:
                if is_consistent(r[r_index], r[k], a,region_adj,c,r):
                    # remove_color(r[k], a,r,c)
                    c[k].remove(a)
            if k != r_index and is_empty(c,r,r[k]):
                empty_domain = True
        if empty_domain and (k not in culori_asign):
            c = copy.deepcopy(c2)  #asta ar trebui sa reseteze teoretic
        else:
            culori_asign.append(r_index)
            return a

def is_final(color_list):
    print(color_list)
    for c in color_list:
        if len(c) != 1:
            return False
    return True

def get_index_least_constraint(colors):
    smallest = -1
    region_index= -1
    for x in colors:
        if smallest == -1  or ( smallest > len(x) and len(x) != 0):
            smallest = len(x)
            region_index = colors.index(x)
    return region_index

def mrv_alg(regions,colors, region_adj,final):
    while is_final(colors) is False:
        region_index = get_index_least_constraint(colors)
        if region_index != -1:
            color = forward_checking(regions,colors,region_index,region_adj)
            print(color)
            if color != None:
                print(culori_asign)
                final[region_index] = color
            else:
                break
    return final_colors

if __name__ == '__main__':
    # print("Exemplul1: ",mrv_alg(region_list,colors_list,region_adjacency,final_colors))
    # print(colors_list)

    mrv_alg(region_list2,colors_list2,region_adjacency2,final_colors2)
    print("Exemplul2: ",colors_list2)
