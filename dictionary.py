# capitals = {
#     "Bangladesh": "Dhaka",
#     "India": 50,
#     "Pakistan": "Islamabad"
# }
# # key, value pair

# print("The capital of Bangladesh is ", capitals["Bangladesh"])

# marks = {
#     "Alex": 80,
#     "Baena": 75
# }

# if (marks["Alex"] > 80):
#     print("A+")
# else:
#     print("Fail")


inception_movie_info = {
    "title": "Inception",
    "release_year": 2010,
    "rating": 8.8
}


inception_movie_info["rating"] = 9.1

# print(f"{inception_movie_info["rating"]}")



# print(inception_movie_info.items());

for k, v in inception_movie_info.items():
    print(f"key: {k} , value:{v}")