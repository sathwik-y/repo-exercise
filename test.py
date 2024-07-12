import numpy as np
import matplotlib.pyplot as plt
def quadratic_models(time,a,b,c):
    temp = a* (time ** 2) + b * time + c
    return temp

time_vals = np.linspace(0,10,50)
def main() :
    sets_of_coefficients = [{0.2,1.5,35},{-0.1,2.0,25},{0.3,-2,30}]
    # Plot each set of coefficients
    for i, (a, b, c) in enumerate(sets_of_coefficients):
        temperature = quadratic_models(time_vals, a, b, c)
        plt.plot(time_vals, temperature, label=f'Set Coefficients')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Multi Set')
    plt.show()

    a,b,c = 0.1,-1,30
    temp_hardcoded = quadratic_models(time_vals,a,b,c)
    plt.plot(time_vals,temp_hardcoded,label ='Hardcoded coeff')
    a = float(input("Enter the value of a : "))
    b = float(input("Enter the value of b : "))
    c = float(input("Enter the value of c : "))
    temp_hardcoded = quadratic_models(time_vals,a,b,c)
    plt.plot(time_vals,temp_hardcoded,label ='User Input')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title("Hardcoded and Input")
    plt.legend()
    plt.show()

main()