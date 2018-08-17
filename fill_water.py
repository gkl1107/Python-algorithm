
def get_water(jug1size,jug2size,targetIn1):

# set initial state for the big jug and the small jug, 
# in default considering jug1size as the bigger and jug2size as the smaller
    jugBig = 0
    jugSmall = jug2size
    print("Start: big jug: {}, small jug: {}".format(jugBig,jugSmall))

# keep pouring small-jug size of water into the big jug, until the big jug is over-filled
    while jugBig <= jug1size:
        jugBig = jugBig + jug2size
        jugSmall = 0
        print("big jug: {}, small jug: {}".format(jugBig,jugSmall))

# when the big jug is over-filled, reset the big jug as 0(empty), 
# calculate the over-fill amount and put it into samll jug.
    else: 
        jugBig = 0
        jugSmall = jug2size - jug1size % jug2size
        print("big jug: {}, small jug: {}".format(jugBig,jugSmall))
# pour the over-filled amount into big jug,  
        jugBig = jugBig + jugSmall
        jugSmall = 0
        print("big jug: {}, small jug: {}".format(jugBig,jugSmall))


# keep pouring small-jug size of water into the big jug, until the big jug is equal to target
    while jugBig != targetIn1:
        jugBig = jugBig + jug2size
        jugSmall = 0
        print("big jug: {}, small jug: {}".format(jugBig,jugSmall))
    else:
        print("Finish! big jug: {}, small jug: {}".format(jugBig,jugSmall))
        
    

get_water(8,3,4)