# Initialize empty lists and dictionaries to store data.
country_name = []  # List to store country names.
population = []  # List to store population data.
literacy_rate = []  # List to store literacy rate data.
num_mo_sub = []  # List to store the number of mobile subscriptions.
num_in_users = []  # List to store the number of internet users.
amount_elec_prod = []  # List to store the amount of electricity produced.
amount_elec_consum = []  # List to store the amount of electricity consumed.
country_dict = {}  # Dictionary to map country names to their index.
prod_m_con = []  # List to store countries with more electricity production than consumption.
con_m_prod = []  # List to store countries with more electricity consumption than production.
subPerCapita = []  # List to store mobile subscription per capita.
intPerCapita = []  # List to store internet user per capita.

# Function to find the index of the maximum value in a list.
def max_index(myList):
    for index, number in enumerate(myList):
        if number == max(myList):
            return index

# Function to find the index of the minimum value in a list.
def min_index(myList):
    for index, number in enumerate(myList):
        if number == min(myList):
            return index

# Function to read data from a CSV file.
def read_csv():
    document = open("CountryData.csv", 'r')
    lines = document.readlines()[1:]
    for line in lines:
        data = line.strip().split(',')
        country_name.append(data[0])
        population.append(int(data[1]))
        literacy_rate.append(int(data[2]))
        num_mo_sub.append(int(data[3]))
        num_in_users.append(int(data[4]))
        amount_elec_prod.append(float(data[5]))
        amount_elec_consum.append(float(data[6]))
        
        # Create a dictionary mapping country names to their index.
        for index, name in enumerate(country_name):
            country_dict[name] = index

# Function to display information about a specific country.
def query(name):
    country_index = country_dict[name]
    print(name,  "has a population of", population[country_index], "and a literacy rate of", literacy_rate[country_index])
    print("The estimate of the number of mobile subscriptions is", num_mo_sub[country_index], "while that of internet users is", num_in_users[country_index])
    print(name, "produces", amount_elec_prod[country_index], "billion KWh of electricity annually, while it consumes",amount_elec_consum[country_index], "billion KWh of electricity.")

# Function to create a new file with subscription and internet per capita data.
def create_file():
    global country_name, num_mo_sub, num_in_users, population

    new_document = open("newFile" , "w")
    new_document.write("Country Name\tSubscription Per Capita\tInternet Per Capita\n")
    for index, value in enumerate(country_name):
        new_document.write(f"{value.ljust(20)}\t{round(num_mo_sub[index]/population[index], 2)}\t\t{round(num_in_users[index]/population[index], 2)}\n")

# Function to print various statistics and information.
def print_info():
    # Calculate and print the total population of Africa.
    print("The total population of Africa is: ", sum(population))

    # Find and print the most and least populous countries in Africa.
    for index, value in enumerate(population):
        if value == max(population):
            max_country = country_name[index]
        if value == min(population):
            min_country = country_name[index]
    print('The most populous African country is', max_country)
    print("The least populous country in Africa is", min_country)
    
    # Calculate and print the country with the highest and lowest literacy rates.
    weighted_literacy_rates = []
    for index, value in enumerate(literacy_rate):
        if value == max(literacy_rate):
            max_literacy_rate_country = country_name[index]
        if value == min(literacy_rate):
            min_literacy_rate_country = country_name[index]
        weighted_literacy_rate = value * population[index]
        weighted_literacy_rates.append(weighted_literacy_rate)
    print('The African country with high literacy rate is: ', max_literacy_rate_country)
    print("The African country with low literacy rate is", min_literacy_rate_country)
    print("The “average” literacy rate in Africa is", sum(weighted_literacy_rates)/sum(population))
    
    # Calculate and print countries with the highest and lowest mobile subscription and internet user per capita.
    for index, value in enumerate(num_mo_sub):
        sub_per_cap = value/population[index]
        subPerCapita.append(sub_per_cap)
    maxsubPerCapita = max_index(subPerCapita)
    minsubPerCapita = min_index(subPerCapita)
    
    for index, value in enumerate(num_in_users):
        in_per_cap = value/population[index]
        intPerCapita.append(in_per_cap)
    maxintPerCapita = max_index(intPerCapita)
    minintPerCapita = min_index(intPerCapita)
     
    print("The country with the highest mobile subscription per capita is", country_name[maxsubPerCapita], "and the country with the lowest number of mobile subscriptions per capita is", country_name[minsubPerCapita])
    print("The country with the highest internet users per capita is", country_name[maxintPerCapita], "and the country with the lowest number of internet per capita is", country_name[minintPerCapita]) 

    # Determine and print electricity exporters and importers.
    for index, value in enumerate(amount_elec_prod):
        if value > amount_elec_consum[index]:
            prod_m_con.append(country_name[index])
        elif value < amount_elec_consum[index]:
            con_m_prod.append(country_name[index])
    print("The electricity exporters are:", prod_m_con)
    print("The electricity importers are: ", con_m_prod)

# Read data from the CSV file.
read_csv()

# Print lists and dictionaries for verification.
#print(country_name)
#print(population)
#print(literacy_rate)
#print(num_mo_sub)
#print(num_in_users) 
#print(amount_elec_prod)
#print(amount_elec_consum)
#print(country_dict)

# Prompt the user for input and display country information.
user_input = input("Please enter the country you want to know about.: ")
print(query(user_input))

# Create a new file with subscription and internet per capita data.
create_file()

# Print various statistics and information.
print_info()
