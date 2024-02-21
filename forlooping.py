def string_itr():
    names = 'urvashi'
    for i in names:
        print(i)


def print_names_of_list():
    my_list = []
    for i in range(5):
        my_names = input("Enter names")
        my_list.append(my_names)
    print(my_list)
    for name in my_list:
        print(name)
        if name.lower() == 'madhavi':
            print(f"hello {name}")


def cube():
    # exponential operator= **
    list_of_nums = [2, 3, 4, 5]
    new_list = []
    for i in list_of_nums:
        print(f"cube of numbers {i} is {i ** 3}")
        new_list.append(i ** 3)
    else:
        print("success")
    print(new_list)


def learn_for_else():
    tupple1 = (1, 2, 3, 4, 5, 6, 7, 8)
    for i in tupple1:
        print(i)
        if i == 5:
            break
    else:
        print("success")


def calculate_avg_height():
    heights_data_list = input("Please enter height of boys in your class")
    final_list = list(heights_data_list.split())
    count = 0
    sum_of_heights = 0
    for i in final_list:
        sum_of_heights = int(i) + sum_of_heights
        count = count + 1
    number_of_boys = count
    total_height = sum_of_heights
    average = (total_height / number_of_boys)
    average_of_height = round(average)
    print(f"average is {average_of_height}")


