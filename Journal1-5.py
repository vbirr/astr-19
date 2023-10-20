"""
Name: Vanessa Birrueta-Hernandez
Journal #1 - Session 5 Prompt

"""
import math

def generate_sin_table():
    print("sin(x) vs. x")
    for i in range(1000):
        x = 2 * math.pi * i / 999  
        sin_value = math.sin(x)
        print(f"{sin_value:.3f}\t\t{x:.3f}")

def main():
    generate_sin_table()

if __name__ == "__main__":
    main()
