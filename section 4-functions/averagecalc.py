# An example for taking command line input
# sys.argv is the list of command line parameters
import sys

def calcaverage(x,y):
    average = (x+y)/2
    print("The average of %0.2f and %0.2f is:  %0.2f" %(x, y, average))
    return average
	
if __name__=='__main__':
    #The command line arguments come into the program as a list of string
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    print(sys.argv)
    calcaverage(x,y)  
