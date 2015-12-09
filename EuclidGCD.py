
def gCd(x, y):
    print("X = ",x,"Y = ",y)
    if y==0:
        return x
    else:    
        return gCd(y,x%y)

def main():
    x = int(input("Input a number:"))
    y = int(input("Input a number:"))
    print("GCD of", x, ",",y,"=",gCd(x,y))
    
if __name__ =="__main__":
    main()