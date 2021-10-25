import random
import copy

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


def forward_checking(r, c):
    i = 0
    while is_empty(r[i]) is False:
        c2 = copy.deepcopy(c)
        # pentru 3.10
        # a = random.choice(c[r.index(r[i])])  # ia random o culoare din lista de culori a regiunii i
        # pentru 3.9
        a = random.sample(c[r.index(r[i])],1)  # ia random o culoare din lista de culori a regiunii i
        a = ' '.join(a)  # transforma culoarea din lista in string(pentru a putea fi folosita mai departe)
        remove_color(r[i], a)
        empty_domain = False
        for k in range(i + 1, len(r)):
            for b in c[r.index(r[k])]:
                if is_consistent(r[i], r[k], a):
                    remove_color(r[k], b)
            if is_empty(r[k]):
                empty_domain = True
        if empty_domain:
            c = copy.deepcopy(c2)  #asta ar trebui sa reseteze teoretic
            a = 1  # asta e random pus -> trebuie reset function(nu stiu inca cum)
        else:
            return a
    return 0


if __name__ == '__main__':
    forward_checking(region_list, colors_list)
    print(colors_list)
