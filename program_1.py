def kilometer_conversion(kilometers):  

    miles = kilometers * 0.6214

    return miles   

if __name__ == '__main__':

    km = float(input("How many kilometers: "))

    converted_miles = kilometer_conversion(km)
    
    print(f"That is equal to: {converted_miles:.2f} miles.")
