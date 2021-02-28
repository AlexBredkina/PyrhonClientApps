import csv


files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = ['Изготовитель ОС','Название ОС', 'Код продукта','Тип системы']
    dict = {}
    files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    for item in files:
        with open(item, encoding='cp1251') as fd:
            for line in fd:
                if line.startswith('Изготовитель ОС'):
                    value = line[len('Изготовитель ОС')+2:]
                    value = value.strip()
                    os_prod_list.append(value)
                elif line.startswith('Название ОС'):
                    value = line[len('Название ОС') + 2:]
                    value = value.strip()
                    os_name_list.append(value)
                elif line.startswith('Код продукта'):
                    value = line[len('Код продукта') + 2:]
                    value = value.strip()
                    os_code_list.append(value)
                elif line.startswith('Тип системы'):
                    value = line[len('Тип системы') + 2:]
                    value = value.strip()
                    os_type_list.append(value)
    mylist = [os_prod_list,os_name_list, os_code_list, os_type_list]
    for i in range(len(main_data)):
        dict[main_data[i]] = mylist[i]

    # return dict
    with open('TASK1.csv', 'w') as f_n:
        f_n_writer = csv.DictWriter(f_n, fieldnames=main_data)
        f_n_writer.writeheader()
        for i in range(0,3):
            for a in range(len(mylist)-1):
                dictionary = {}
                for key in dict:
                    dictionary[key] = dict[key][a]
                f_n_writer.writerow(dictionary)








get_data()






# def write_to_csv():
#     n =get_data()
#     fieldnames = list(n.keys())
#     with open('TASK1.csv', 'w') as f_n:
#         f_n_writer = csv.DictWriter(f_n, fieldnames=fieldnames)
#         f_n_writer.writeheader()
#     print(fieldnames)
#     print(type(fieldnames))
#
# write_to_csv()





