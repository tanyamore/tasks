def main ():

    print ("Enter temperature")
    a = input ();
    try:
        a = float (a)
    except ValueError:
        print ("Not a number")
        return
    if a >= -273:
        kel = a + 273
        print ("Kel", kel)
        far = a * (9 / 5) + 32
        print ("Faren" , far)
    else:
        print ("Min temperature -273")

if __name__=='__main__':
    main()
