"""
- add movies
- see movies
- find a movie
- stop running the program

Tasks
[] : Show the user the main interface and get their input
[] : Allow users to add movies
[] : Show all their movies
[] : find a movie
[] : stop running the program when they type "q"
"""

movies = []


def menu():
    userInput = input("Enter 'a' to add a movie, 'l' to see your movie, "
                      "'f' to find a movie, and 'q' to quit")

    while True:
        if userInput == 'a':
            addMovie()
        elif userInput == 'l':
            showMovie()
        elif userInput == 'f':
            findMovie()
        elif userInput == 'q':
            print("Stopping program...")
            break
        else:
            print("Unknown command, pleas  try again:")

        userInput = input("\nEnter 'a' to add a movie, 'l' to see your movie, "
                          "'f' to find a movie, and 'q' to quit")


def addMovie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    year = int(input("Enter the movie release year: "))

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def showMovie(movies_list):
    for movie in movies_list:
        showMovieDetails(movie)


def showMovieDetails(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


def findMovie():
    findBy = input("What property of the movie are you looking for: ")
    lookingFor = input("What are you searching for: ")

    foundMovies = findByAttribute(movies, findBy, lambda x: x[lookingFor])


def findByAttribute(items, findBy, lookingFor):
    found = []

    for movie in items:
        if movie[findBy] == lookingFor:
            found.append(movie)

    return found


menu()
