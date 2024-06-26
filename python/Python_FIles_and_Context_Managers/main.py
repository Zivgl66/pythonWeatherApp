import csv
import pandas as pd
from functools import reduce

from string import ascii_lowercase as alphabet

# exercise 1:

# loop the alphabet's and make a new file each time with the letter while writing to it the letter
# def generate_txt_files():
#     for i in alphabet:
#         with open(f"{i}.txt" , "w") as file:
#             file.write(f"{i}")
#     return 0
#
#
# generate_txt_files()


# exercise 2:

# next means the method is called repeatedly, when the file is used as iterator in the loop
# _ means we don't need a variable, just run the specific range
# def read_n_lines(file_path, n):
#     with open(file_path) as input_file:
#         my_list = [next(input_file).strip() for _ in range(n)]
#     for word in my_list:
#         print(word)
#
#
# read_n_lines("./txt.txt", 10)


# exercise 3:
# data_corona = pd.read_csv("corona.csv")
# # file = open('corona.csv')
#
#
# def get_vaccinated_ages(data):
#     df = pd.DataFrame(data)
#     return list(df.query("Is_vaccinated == 'Y'")['Age'])
#
#
# def get_not_vaccinated_ages(data):
#     df = pd.DataFrame(data)
#     return list(df.query("Is_vaccinated == 'N'")['Age'])
#
#
# def get_min_age(age_list):
#     return min(age_list)
#
#
# def get_max_age(age_list):
#     return max(age_list)
#
#
# def get_average_length_of_hospitalization(data):
#     list_hospitalization = list(data.Length_of_hospitalization)
#     return (reduce(lambda x, y: x+y, list_hospitalization))//len(list_hospitalization)
#
#
# def filter_data(data, user_input_list):
#     df = data[user_input_list]
#     df.to_csv('./filtered_data.csv', index=False)
#     print("New file created in the directory with your Input DATA!")
#     return 0
#

# def filter_by_input(data):
#     gender_input = input("What is the gender? M/F\n")
#     vaccinated_input = input("Are they vaccinated? Y/N\n")
#     min_age_input = int(input("What is the min age?\n"))
#     max_age_input = int(input("What is the max age?\n"))
#     filtered_data = data[(data["gender"] == gender_input) &
#                          (data["Age"] > min_age_input) &
#                          (data["Age"] < max_age_input) &
#                          (data["Is_vaccinated"] == vaccinated_input)]
#     filtered_data.to_csv('./filtered_data.csv', index=False)
#     print("File created!")
#     return 0
#
#
# filter_by_input(data_corona)


# print(f"Vaccinated min age is : {get_min_age(get_vaccinated_ages(data_corona))}")
# print(f"Vaccinated max age is : {get_max_age(get_vaccinated_ages(data_corona))}")
# print(f"Not vaccinated min age is : {get_min_age(get_not_vaccinated_ages(data_corona))}")
# print(f"NOt vaccinated max age is : {get_max_age(get_not_vaccinated_ages(data_corona))}")
# print(f"Average length of hospitalization is: {get_average_length_of_hospitalization(data_corona)} days")
# print("-------------------------------------------------------------------------------")







