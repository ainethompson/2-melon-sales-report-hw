SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
LINE_LENGTH = 80

print("*" * LINE_LENGTH)


def melon_counts(filename):

    file = open(filename)
    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

    for line in file:
        data = line.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count

    file.close()
    return melon_tallies

def sales_stats():

    melon_tallies = melon_counts("orders-by-type.txt")
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue))
        print("We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(melon_tallies[melon_type], melon_type, price, revenue))
    print("******************************************")

sales_stats()

def sales_orders(filename):

    file = open(filename)

    online_sales = 0
    person_sales = 0

    for line in file:
        data = line.split("|")
        if data[1] == "0":
            online_sales += float(data[3])
        else:
            person_sales += float(data[3])

    print("Salespeople generated ${:.2f} in revenue.".format(person_sales))
    print("Internet sales generated ${:.2f} in revenue.".format(online_sales))
    if person_sales > online_sales:
        print("Guess there's some value to those salespeople after all.")
    else:
        print("Time to fire the sales team! Online sales rule all!")
    print("******************************************")

sales_orders("orders-with-sales.txt")