import timeit
counter_start = False
moby = open("pg2701.txt", 'r',encoding="utf-8") #make sure files in same directory
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
def time_fn(my_array):
    execution_count =100
    run_time = timeit.timeit(lambda :count_vowels(my_array),number=execution_count ) 
    average = run_time/execution_count 
    print(average)

def build_array():
    contents = moby.read()
    my_array =[]
    my_string = '';
    for i in contents:
        if i == "\n":
            #print(my_string)
            if my_string != '':
                my_array.append(my_string)
                my_string = ''  
        else:
            my_string = my_string + i
    moby.close()
    return my_array

def count_vowels(passed_array):
    counter_en = False
    counter = 0
    for i in passed_array:
        if i == "CHAPTER 1. Loomings.":
            counter_en = True
        for k in i:
            if (k in vowels) and counter_en:
                counter = counter + 1;
                #print(k)
    #print(counter)
    return counter

if __name__ == "__main__":
    my_array = build_array()
    my_counter = count_vowels(my_array)
    time_fn(my_array)
            
