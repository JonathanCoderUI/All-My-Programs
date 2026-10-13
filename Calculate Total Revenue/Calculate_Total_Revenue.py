def process_sales_data(filename):
    try:
        with open (filename, "r") as file:
            total_revenue = 0

            for line in file:
                try:
                    list_text = line.strip().split(",")

                    Item = list_text[0]
                    Quantity = int(list_text[1])
                    Price = int(list_text[2])

                    total_revenue += Quantity * Price
                    
                except ValueError:
                    continue

            return total_revenue
        
    except FileNotFoundError:
        return -1

# Helper to create temporary test files
with open("sales1.txt", "w") as f:
    f.write("Laptop, 2, 10000000\nMouse, N/A, 150000\nKeyboard, 3, 500000\nMonitor, 1, INVALID\n")

with open("sales_invalid.txt", "w") as f:
    f.write("ItemA, N/A, N/A\nItemB, FREE, FREE\n")

with open("sales_spaces.txt", "w") as f:
    f.write(" Pen , 10 , 5000 \n Book , 2 , 15000 \n")

print(process_sales_data("sales1.txt"))
print(process_sales_data("non_existent_file.txt"))
print(process_sales_data("sales_invalid.txt"))
print(process_sales_data("sales_spaces.txt"))