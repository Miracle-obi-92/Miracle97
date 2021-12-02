Title = [{"Title":"War and Peace","Authors":"Joe Biden","Genre":"Action","Category":"Literacy work","Copies_Available":"400 copies","Description":"Action","Price":"$4,5000","Date_Added":"2/4/2021"},
        {"Title":"Vengence","Authors":"Bill Gates","Genre":"Animation","Category":"Literacy work","Copies_Available":"20 copies","Description":"Pixel","Price":"$5,000","Date_Added":"14/6/2021"},
        {"Title":"No Time To Die","Authors":"Monalisa Algae","Genre":"Action","Category":"Literacy work","Copies_Available":"5,000 copies","Description":"Action","Price":"$87,000","Date_Added":"14/9/2021"},
        {"Title":"No Time To Die","Authors":"James Bond","Genre":"Action","Category":"Literacy work","Copies_Available":"23,000 copies","Description":"Action","Price":"$800,000","Date_Added":"25/9/2019"},
        {"Title":"Old","Authors":"Max Paulon","Genre":"Romance","Category":"Literacy work","Copies_Available":"1,000 copies","Description":"Romance","Price":"$8,000","Date_Added":"9/1/2019"},]



ADMIN_USER= "Miracle@tech2.com"
ADMIN_PASS_WORD= "walk alone bro just do dat"
user_name=input("Enter ADMIN_USER: ")
user_pass_word=input("Enter ADMIN_PASS_WORD: ")


Title1=Title
temp=[]
order=""


def admin_login_any_OS():
    print("1.Display Menu")
    print("2.Add Books")
    print('3.Veiw all borrowed books')
    print("4.Manage Sales")
    print("Get Notification on about finished books")
    
    
def adminDisplayMenu_any_OS():
    print("=======")
    print("Title\Authors\Genre\Category\Copies\Description\Price\Date_Added")
    
    
    for d in Title :
        print(f'{d["Title"]}\t{d["Authors"]}\t{["Genre"]}\t{["Category"]}\t{["Copies"]}\{["Description"]}\t{["Price"]}\t{["Date_Added"]}')
        
        
def addproducts():
    n=int("Enter the books to be added: ")
 
    