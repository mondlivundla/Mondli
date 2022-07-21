
#islands objects and their attributes ina dictionary
island_dimension = {
    "x_axis": 100,
    "y_axis": 100,
}

#function to create a map
def island_map(sides):
    isl_map = []
    for r in range(sides):
        # Add an empty sub-list in the list existing one
        new_map.append([])
        for c in range(sides):
            isl_map[r].append(c)
            #making empty boxes have zero in the map
            new_map[r][c] = 0
    # printing current new map
    #print(map) 
    return new_map

# printing island_map    
def print_island_map():
    print("*******************************************************")
    print("************ We are now in the island *****************")
    print("*******************************************************")
    for r in range(side):
        print(island_map[r])

    print("********************************************************")
    print("****************** Have some fun ***********************")
    print("********************************************************")
