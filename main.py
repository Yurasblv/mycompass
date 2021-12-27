def direction():
    all_directions = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
    single_side = 45
    try:
        print('Enter facing')
        facing = str(input().upper())
        print('Enter turn')
        turn = int(input())
        if facing in all_directions:
            if turn in range(-1080,1080) and turn%single_side==0 :
                start_index = all_directions.index(facing)
                end_index = (start_index + (turn//single_side)) % len(all_directions)
                print(all_directions[end_index])
            else:
                print('Enter correct turn')
        else:
            print('Enter correct side')
    except Exception as e:
        print (f"error: {e}")

if __name__ == '__main__':
    print("""You receive the direction you are facing (one of the 8 directions: N, NE, E, SE, S, SW, W, NW)
     and a certain degree to turn (a multiple of 45, between -1080 and 1080); positive means clockwise, 
     and negative means counter-clockwise.
     Return the direction you will face after the turn.
     Examples:
        "S",  180  -->  "N"
        "SE", -45  -->  "E"
        "W",  495  -->  "NE""")
    direction()
