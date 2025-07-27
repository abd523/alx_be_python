from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days):
    """Calculate and display the future date after adding the specified number of days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    try:
        # Display current date and time
        display_current_datetime()
        
        # Prompt user for number of days
        days = input("Enter the number of days to add to the current date: ")
        days = int(days)  # Validate that input is an integer
        
        # Calculate and display future date
        calculate_future_date(days)
        
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")

if __name__ == "__main__":
    main()