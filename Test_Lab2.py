import Lab2
import statistics

print("Testing Lab2")



num_list = [10,11,45,67]
sorted_list = Lab2.sort_temp(num_list)

def test_find_min_max():
    max_temp = max(num_list)
    min_temp = min(num_list)
    
    test_list = [min_temp, max_temp]
    result_list = Lab2.find_min_max(num_list)

    assert(result_list == test_list)
    
def test_calc_average():
     test_average = sum(num_list)/len(num_list)
     result_average = Lab2.calc_average(num_list)

     assert(result_average == test_average)


def test_calc_median_temperature():
     test_median_temp = statistics.median(sorted_list)
     result_median_temp = Lab2. calc_median_temperature(sorted_list)

     assert(result_median_temp == test_median_temp)





