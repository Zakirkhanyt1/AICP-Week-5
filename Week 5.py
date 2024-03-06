def calculate_price(day, arrival_hour, stay_hours, frequent_parking_number):
    # Define prices and discounts
    evening_charge = 2.00  # Price after 16:00
    discount_evening = 0.5  # 50% discount after 16:00
    discount_other = 0.1  # 10% discount at other times

    # Define hourly prices based on the day
    hourly_prices = {
        'Sunday': 2.00,
        'Monday': 2.00,
        'Tuesday': 2.00,
        'Wednesday': 2.00,
        'Thursday': 2.00,
        'Friday': 2.00,
        'Saturday': 2.00,
    }

    # Validate input data
    if day not in hourly_prices:
        print("Invalid day entered.")
        return None

    if arrival_hour < 0 or arrival_hour > 23:
        print("Invalid arrival hour entered.")
        return None

    if stay_hours < 1:
        print("Invalid number of hours entered.")
        return None

    if frequent_parking_number:
        # Validate frequent parking number and check digit
        if not is_valid_frequent_parking_number(frequent_parking_number):
            print("Invalid frequent parking number.")
            return None

        # Apply discount based on arrival time
        discount = discount_evening if arrival_hour >= 16 else discount_other
    else:
        discount = 0.0

    # Calculate the price
    price_before_16 = hourly_prices[day] * stay_hours
    total_price = price_before_16 - (price_before_16 * discount)

    # Add evening charge if applicable
    if arrival_hour < 16 and arrival_hour + stay_hours >= 16:
        total_price += evening_charge

    return total_price


def is_valid_frequent_parking_number(number):
    # Check if the frequent parking number is a 5-digit number with a valid check digit
    if len(number) != 5:
        return False

    try:
        number = int(number)
        check_digit = number % 11
        return check_digit == 0
    except ValueError:
        return False


def task_1():
    # Input data from the user
    day = input("Enter the day: ")
    arrival_hour = int(input("Enter the arrival hour (0-23): "))
    stay_hours = int(input("Enter the number of hours to park: "))
    frequent_parking_number = input("Enter the frequent parking number (optional): ")

    # Calculate and display the price
    price = calculate_price(day, arrival_hour, stay_hours, frequent_parking_number)
    if price is not None:
        print(f"The total price to park is: {price:.2f}")


def task_2():
    daily_total = 0.0

    while True:
        task_1()
        payment = float(input("Enter the amount paid: "))
        daily_total += payment

        more_customers = input("Is there another customer? (yes/no): ").lower()
        if more_customers != 'yes':
            break

    print(f"\nDaily total earnings: {daily_total:.2f}")


def main():
    task_2()


if __name__ == "__main__":
    main()
