def direction():
    all_directions = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
    single_side = 45
    try:
        facing = str(input().upper())
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
    direction()
