home_base = (10.01, 11.21)
visitor_ids_list = [1,2,3,4,1,5,2,1]
visitor_ids_set = set()

for visitor in visitor_ids_list:
    visitor_ids_set.add(visitor)

for id in visitor_ids_set:
    print(f"Home Base X Coordinates {home_base[0]}. Y Coordinates {home_base[1]}")
    print(f"User id {id}")