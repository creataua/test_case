def max(file_numbers):
    mx = file_numbers[0]
    print(f"Максимальне число в файлі - '{mx}'")


def min(file_numbers):
    mn = file_numbers[-1]
    print(f"Мінімальне число в файлі - '{mn}'")

def average_sum(file_numbers):
    lst_len = len(file_numbers)
    lst_sum = sum(file_numbers)
    avg_sum = round(lst_sum/lst_len, 2)
    print(f"Середнє арифметичне значення - '{avg_sum}'")


def mediana(file_numbers):
    number_check = len(file_numbers)/2
    if number_check.is_integer():
        nb_mediana = int(number_check)
        print(f"Медіана - '{nb_mediana}'")
    else:
        add_number = int(number_check + 0.5)
        get_first_digit = file_numbers[add_number]
        minus_number = int(number_check - 0.5)
        get_second_digit = file_numbers[minus_number]
        nb_mediana = (get_first_digit + get_second_digit)*0.5
        print(f"Медіана - '{nb_mediana}'")


def get_file():
    lst_number = []
    with open('10m.txt') as file_object:
        content = file_object.readlines()
        for i in content:
            lst_number.append(int(i))
        new_list = sorted(lst_number, reverse=True)
        return new_list



def main():
    file_numbers = get_file()
    max(file_numbers)
    min(file_numbers)
    mediana(file_numbers)
    average_sum(file_numbers)



if __name__ == '__main__':
    main()
