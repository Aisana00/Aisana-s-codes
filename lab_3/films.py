movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# 1. Function that takes a single movie and returns True if its IMDB score is above 5.5
def is_high_rated(movie):
    return movie["imdb"] > 5.5

# 2. Function that returns a sublist of movies with an IMDB score above 5.5
def get_high_rated_movies(movies_list):
    return [movie for movie in movies_list if movie["imdb"] > 5.5]

# 3. Function that takes a category name and returns just those movies under that category
def get_movies_by_category(movies_list, category):
    return [movie for movie in movies_list if movie["category"].lower() == category.lower()]

# 4. Function that takes a list of movies and computes the average IMDB score
def get_average_imdb(movies_list):
    if not movies_list:
        return 0
    total_score = sum(movie["imdb"] for movie in movies_list)
    return total_score / len(movies_list)

# 5. Function that takes a category and computes the average IMDB score
def get_average_imdb_by_category(movies_list, category):
    category_movies = get_movies_by_category(movies_list, category)
    return get_average_imdb(category_movies)

# Testing the functions
if __name__ == "__main__":
    # Test function 1
    print("1. Testing is_high_rated():")
    print(f"   Dark Knight: {is_high_rated(movies[2])}")  # Should be True
    print(f"   AlphaJet: {is_high_rated(movies[8])}")     # Should be False
    print()
    
    # Test function 2
    print("2. High rated movies (IMDB > 5.5):")
    high_rated = get_high_rated_movies(movies)
    for movie in high_rated:
        print(f"   {movie['name']}: {movie['imdb']}")
    print()
    
    # Test function 3
    print("3. Romance movies:")
    romance_movies = get_movies_by_category(movies, "Romance")
    for movie in romance_movies:
        print(f"   {movie['name']}: {movie['imdb']}")
    print()
    
    # Test function 4
    print("4. Average IMDB score of all movies:")
    avg_all = get_average_imdb(movies)
    print(f"   Average: {avg_all:.2f}")
    print()
    
    # Test function 5
    print("5. Average IMDB score by category:")
    categories = ["Romance", "Thriller", "Action", "Comedy"]
    for category in categories:
        avg_category = get_average_imdb_by_category(movies, category)
        print(f"   {category}: {avg_category:.2f}")