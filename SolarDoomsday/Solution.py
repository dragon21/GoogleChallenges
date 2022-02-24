# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def StartCount(squareYards):
    #print("Start Measuring with available square Yards",squareYards)
    i = 1
    if i == squareYards:
        return 1
        
    while i < squareYards:
        #print(i)
        i += 1
        if i*i > squareYards:
            #print("Its time to cut with",i-1)
            return (i-1)*(i-1)
        
def StartCorp(squareYards):
    while squareYards != 0:
        totalArea = StartCount(squareYards)
        #print("Start Corping Area",totalArea)
        #print("\n")
        AreasList.append(totalArea)
        squareYards = squareYards - totalArea

def solution(squareYards):
    StartCorp(squareYards)
    print(AreasList)

#print("^^^^^^^^^^^^^^^^^^^^^^^")
#print("Solar Doomsday is here!")
#print("^^^^^^^^^^^^^^^^^^^^^^^\n")
AreasList = []
squareYards = int(input("Please enter Square Yards:"))
#print("#########################\n")
solution(squareYards)



