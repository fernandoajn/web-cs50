def square(x):
    return x*x

def main():
    for i in range(10):
        print("{} squared is {}".format(i,square(i))) #before python 3.6
        #print(f"{i} squared is {square(i)}")  #after python 3.6

# if i'm running this particular file, run main() function
if __name__ == "__main__":
    main()
