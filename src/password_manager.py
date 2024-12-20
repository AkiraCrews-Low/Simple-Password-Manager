# Global variables
menu = ("\n[1] Enter 1 to Add New Credentials.\n[2] Enter 2 to View Stored Credentials.\n[e] Enter e to Exit the Program.\n")

# Function that encrypts a users password
def Password_encrypter (Password):
    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
    return "".join([charSet[(charSet.find(c) + 3) % 95] for c in Password])

# Function that decrypts a users password
def Password_decrypter (enPassword):
    charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
    return "".join([charSet[(charSet.find(c) - 3) % 95] for c in enPassword])

# Add credentials function
def Add_credentials():
    print ("\n• You have chosen to Add New Credentials.")

    # Input username
    Username = input("\nPlease enter your username here: ")

    # Making sure the username is not empty
    # While loop that continues as long as the stripped version of Username is empty
    while not Username.strip(): 
        print ("\n• You have not entered a username. Please enter a valid username.")
        Username = input("\nPlease enter your username here: ")

    # Input password   
    Password = input("\nPlease enter your password here: ")

    # Making sure the password is not empty
    # While loop that continues as long as the stripped version of Password is empty
    while not Password.strip(): 
        print ("\n• You have not entered a password. Please enter a valid password.")
        Password = input("\nPlease enter your password here: ")

    # Input website/URL
    URL = input("\nPlease enter the website/URL here: ")

    # Making sure the URL is not empty
    # While loop that continues as long as the stripped version of URL is empty
    while not URL.strip(): 
        print ("\n• You have not entered a website/URL. Please enter a valid website/URL.")
        URL = input("\nPlease enter the website URL here: ")

    # Encrypting the password
    enPassword = Password_encrypter(Password)

    # Appending to the text file - Creating the text file if it does not exist.
    f = open("credentialstorage.txt", "a")
    f.write(Username + "   " + enPassword + "   " + URL + "   ")

    print ("\n• Your credentials have been stored.\n")

# View credentials function
def View_credentials():
    print ("\n• You have chosen to View Stored Credentials.\n")

    # Reading the text file
    try:
        f = open ("credentialstorage.txt", "r")
        data = f.read()
        
        # Checking if there is data in the text file
        if data != "":
            
            # Stripping the data of any empty spaces
            data_strip = data.strip()

            # Splitting the data by three spaces
            dataList = data_strip.split("   ")

            # Displaying the text file contents in a visually presentable way    
            i = 0
            border = "|"
            print (f"{border}{'USERNAME' : ^20}{border}{'PASSWORD' : ^20}{border}{'WEBSITE/URL' : ^20}{border}")
            print ("----------------------------------------------------------------")
            while i < len(dataList):  # repeat until 'i' is larger than the list length
                
                username = dataList[i]
                encrypted_password = dataList[i + 1]
                website_url = dataList[i + 2]

                # Decrypting each password individually
                dePassword = Password_decrypter(encrypted_password)

                print (f"{border}{username : ^20}{border}{dePassword: ^20}{border}{website_url : ^20}{border}")
                i += 3

            else:
                print ("\n• All stored credentials have been displayed.\n")

        else:
            print ("No data in the credential storage.")

    # Testing if the text file exists
    except FileNotFoundError:
        print ("No stored credentials exist. New credentials must be added.")
    

# Execution Section
print ("\nWelcome to the Simple Password Manager!")

choice = ''

while choice != 'e':
    print (menu)
    choice = input("\nPlease enter your response here: ")

    if choice == '1':
        Add_credentials()

    elif choice == '2':
        View_credentials()

    elif choice == 'e':
        print ("\n• You have chosen to quit the program. The system will shutdown.\n")

    else:
        print ("\n• Invalid response, please try again.\n")

# To indicate that the program is finished
print ("System will shutdown.")
