import csv
import json
with open('data\open.csv', mode='r', newline='', encoding='utf-8') as file:
        valid_rows = []
        csv_reader = csv.reader(file)
        next(csv_reader)
        #checking the quantity of rows in the csv file
        def check_rows():
            check_total=0
            check_bad=0
            for row in csv_reader:
                check_total += 1
                if(float(row[4])<=0 or row[5]=='' or float(row[5])<=0 or row[1]=='' or row[0]==''):
                    check_bad +=1
                else:
                    total=float(row[4])*float(row[5])
                    row.append(total)
                    valid_rows.append(row)
            return check_total,check_bad
        ##Calculating total revenue and average revenue per order
        def calculate_revenue():
            total_revenue=0
            for row in valid_rows:
                if(row[7].lower()!='cancelled'):
                    total_revenue+=row[8]
            print('*****************************')
            print(f"Total revenue: {total_revenue}")
            print("*****************************")
        ##total revenue / number of completed orders
        def calculate_average_revenue():
            completed_orders=0
            total_revenue=0
            for row in valid_rows:
                if(row[7].lower()!='cancelled'):
                    completed_orders+=1
                    total_revenue+=row[8]
            print(f"Average revenue per order: {total_revenue/completed_orders if completed_orders > 0 else 0}")
            print("*****************************")
        #Calculating total revenue per product
        def calculate_revenue_per_product(): 
            dict1={}
            for row in valid_rows:
                if row[7].lower() == 'completed':
                    dict1[row[2]] = dict1.get(row[2], 0) + row[8]
            dict1 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
            for key, value in dict1.items():
                print(f"Total revenue for {key}: {value}")
            print('****************************')
        #Calculating total revenue per category
        def calculate_revenue_per_category():
            dict1={}
            for row in valid_rows:
                if row[7].lower() == 'completed':
                    dict1[row[2]] = dict1.get(row[2], 0) + row[8]
            dict1 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
            for key, value in dict1.items():
                print(f"Total revenue for {key}: {value}")
            print('****************************')
        #Exporting the cleaned data to a new CSV file
        def export_cleaned_csv():

            export_file = 'data_output\new2.csv'
            with open(export_file, mode='w', newline='', encoding='utf-8') as file:
                    csv_writer = csv.writer(file)
                    # Write the header row
                    csv_writer.writerow(['Order ID', 'Customer Name', 'Customer id', 'Product', 'Category', 'Quantity', 'Price', 'Order Date', 'Status', 'Total Revenue','Discounted Price'])
                    # Write the valid rows to the new CSV file
                    csv_writer.writerows(valid_rows)
        def get_customer_data():
            with open('data/task2.json') as f:
                customer_new_data={}
                data = json.load(f)
                for customer in data:
                    customer_new_data[customer['customer_id']] = customer['name'] 
            return customer_new_data
        def adding_customer_names():
            unknown_count = 0
            customer_data = get_customer_data()
            for row in valid_rows:
                if (row[1] in customer_data):
                    row.insert(1, customer_data[row[1]])
                else:
                    unknown_count += 1
                    row.insert(1, 'Unknown')
            print('===============================')
            print('Customer names added to the valid rows.')
            print(f"Number of unknown customers: {unknown_count}")
            print('===============================')
        ##Day 3 — API → ETL
        def get_discount_prices():
            with open('data/task3_data.json') as f:
                products_discount={}
                data = json.load(f)
                for product in data:
                    products_discount[product['product']] = product['discount']
            return products_discount
        def adding_product_discount():
            products_discount=get_discount_prices()
            for row in valid_rows:
                if(row[3] in products_discount):
                    discount = products_discount[row[3]]
                    discounted_price = round(row[9] * (1 - discount), 2)
                    row.insert(10, discounted_price)
                else:
                    row.insert(10, row[9])
            print('Added discounted prices to the valid rows.')
            print('===============================')

                
        total_rows, bad_rows = check_rows()
        print(f"Total rows: {total_rows}") 
        print(f"Bad rows: {bad_rows}")
        calculate_revenue()
        calculate_average_revenue()
        calculate_revenue_per_product()
        calculate_revenue_per_category()
        adding_customer_names()
        adding_product_discount()
        export_cleaned_csv()
        



