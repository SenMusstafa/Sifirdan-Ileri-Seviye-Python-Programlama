class Movie:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie object created')

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("Movie deleted")

# Demonstration
def movie_example():
    myList = [1, 2, 3]
    # myString = 'my String'

    # print(len(myList))
    # print(len(myString))
    # print(type(myList))
    # print(type(myString))

    m = Movie('Film Title', 'Director Name', 120)

    # print(myList)
    print(str(m))  # Movie object created
    # print(len(myList))
    # print(len(m))

if __name__ == "__main__":
    movie_example()
