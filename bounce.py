dropHeight = float(input("Enter the height from which the ball is dropped: "))
bouncy = float(input("Enter the bounciness index of the ball: "))
timesBounce = int(input("Enter the number if times the ball is allowed to continue bouncing: "))
distance = 0

while True:
    distance=distance+dropHeight
    distance= distance + (dropHeight*bouncy)
    dropHeight=(dropHeight*bouncy)
    timesBounce=timesBounce-1
    if timesBounce==0:
        break

    
print("Total distance traveled is: ", distance, "units.")
