# Part 1: Collect customer information
name = input("Customer's full name: ")
meter_number = input("Meter number: ")
tariff = input("Tariff category (Residential, Commercial, or Industrial): ")
consumption = float(input("Electricity consumed (kWh): "))

# Challenge 1: Input validation for negative consumption
if consumption < 0:
    print("Error: Electricity consumption cannot be negative.")

# Challenge 2 & Part 2: Select rate based on tariff category
else:
    if tariff == "Residential":
        rate = 50
    elif tariff == "Commercial":
        rate = 75
    elif tariff == "Industrial":
        rate = 100
    else:
        rate = 0
        print("Invalid tariff category")

    # Proceed only if the tariff category was valid
    if rate > 0:
        # Part 3: Calculate the service charge
        if consumption < 100:
            service_charge = 500
        elif consumption < 300:
            service_charge = 1000
        else:
            service_charge = 2000

        # Part 4: Determine the customer's consumption level
        if consumption < 100:
            level = "Low Consumption"
        elif consumption < 300:
            level = "Moderate Consumption"
        else:
            level = "High Consumption"

        # Part 5: Calculate electricity charge and total bill
        electricity_charge = consumption * rate
        total_bill = electricity_charge + service_charge

        # Challenge 3: Ask for payment status
        paid = input("Has the customer paid their bill? (Yes or No): ")

        # Part 5: Display the well-formatted bill
        print("\n- ELECTRICITY BILL -")
        print("Customer Name:", name)
        print("Meter Number:", meter_number)
        print("Tariff Category:", tariff)
        print("Consumption:", consumption, "kWh")
        print("Consumption Level:", level)
        print("Unit Rate:", rate)
        print("Electricity Charge:", consumption, "*", rate, "=", electricity_charge)
        print("Service Charge:", service_charge)
        print("Total Amount Payable:", total_bill)

        # Challenge 3 & 4: Display payment status and outstanding balance
        if paid == "Yes":
            print("Payment Successful")
        else:
            print("Payment Pending")
            print("Outstanding Balance:", total_bill)