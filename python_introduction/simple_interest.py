```python
def calculate_simple_interest():
    try:
        # Prompt user for input
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (as a percentage): "))
        time = float(input("Enter the time period (in years): "))
        
        # Validate inputs
        if principal < 0 or rate < 0 or time < 0:
            print("Error: Principal, rate, and time must be non-negative.")
            return
        
        # Calculate simple interest
        interest = principal * rate * time / 100
        
        # Print the result
        print(f"The simple interest is: {interest}")
        
    except ValueError:
        print("Error: Please enter valid numeric values for principal, rate, and time.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculate_simple_interest()
```