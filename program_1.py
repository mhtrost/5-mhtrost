def kilometer_conversion(kilometers):    
    miles = kilometers * 0.6214
    return miles   

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':

    km = float(input("How many kilometers: "))

    converted_miles = kilometer_conversion(km)
    
    print(f"That is equal to: {converted_miles:.2f} miles.")
