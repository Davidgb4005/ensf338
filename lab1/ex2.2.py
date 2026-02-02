import timeit
moby = open("pg2701.txt", 'r',encoding="utf-8") #make sure files in same directory
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
def build_array():
    contents = moby.read()
    my_array =[]
    my_string = ''
    for i in contents:
        if i == "\n":
            if my_string != '':
                my_array.append(my_string)
                my_string = ''  
        else:
            my_string = my_string + i       

    #print(my_array[2500])
    moby.close()
    return my_array
def count_vowels(passed_array):
    counter_en = False
    counter = 0
    for i in passed_array:
        if i == "CHAPTER 1. Loomings.":
            counter_en = True
        if counter_en:
            for k in i:
                if (k in vowels):
                    counter = counter + 1;

    print(counter)
    return counter


if __name__ == "__main__":
    my_array = build_array()
    my_counter = count_vowels(my_array)
            
