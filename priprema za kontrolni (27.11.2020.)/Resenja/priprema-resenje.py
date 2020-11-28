# 1. Example

def read_all_books():
    global books 
    books = {}
    with open('files/books.txt') as f:
        for book in f.readlines():
            descriptions = book.split('|')
            books[descriptions[0]] = descriptions[1:]
    print(books)
    
def find_books_by_author():
    author = input("Find books by author >>>")
    
    exists = False
    for book_code in books.keys():
        book_description = books[book_code]
        
        if author in books[book_code]: 
            exists = True
            print(book_description)
            
    if not exists:
        print('There are no books by this author') 

# 2. Example   

def total_number_of_reactions():
    find_user = input("Return number of reactions of user >>>")
    
    numb_reac = 0 
    
    with open("files/user_activities.txt") as f: 
        for user in f.readlines(): 
            if find_user in user:
                user_data = user.split('|')
                numb_reac = numb_reac + int(user_data[-1])
                
    print("Total number of reactions>>>", numb_reac)

# 3. Example 
   
def minimal_flight_distance():
    min_flight_distance = input("Minimal flight distance>>>")
    
    minimum = False
    print("Flights")
    
    with open("files/flights.txt") as f: 
        for flight in f.readlines():
            flight_dist = flight.split('|')[-1]
            if int(min_flight_distance) <= int(flight_dist): 
                print(flight)
    
    if not minimum: 
        print("No flights")
    
if __name__ == "__main__":
    read_all_books()
    find_books_by_author()
    total_number_of_reactions()
    minimal_flight_distance()