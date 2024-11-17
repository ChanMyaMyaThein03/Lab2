# Import statistics Library
import statistics

def display_main_menu():
    print("Enter some numbers separated by comas (e.g 5,67,32)")

def get_user_input():
    user_input = input()
    str_list = user_input.split(",")
    float_list = [float (num.strip()) for num in str_list]
    return float_list

def calc_average(num_list):
    average = sum(num_list)/len(num_list)
    return average

def find_min_max(num_list):
    max_temp = max(num_list)
    min_temp = min(num_list)
    
    min_max_list = [min_temp, max_temp]
    return min_max_list

def sort_temp(num_list):
    a = sorted(num_list)
    return a
    
def calc_median_temperature(sorted_list):
    median_temp = statistics.median(sorted_list)
    return median_temp

def main():
    print("ET0735 (Devops for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("The numbers ",num_list)
    
    print("average",calc_average(num_list))
    print("Min_Max: ", find_min_max(num_list))

    print("ascending", sort_temp(num_list))
    sorted_list = sort_temp(num_list)
    print("the median is ",calc_median_temperature(sorted_list))
    
if __name__ == "__main__":    
    main()



