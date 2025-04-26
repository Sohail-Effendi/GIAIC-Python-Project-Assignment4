def main():
    deg_fahrenheit = float(input("\033[1;3m Please enter the value of Fahrenheit:\033[0m "))
    deg_celsius = (deg_fahrenheit-32)*5.0/9.0
    print(f"The value of celsius: {deg_celsius}")
    

if __name__=='__main__':
    main()