import glob
import chardet
import re
import csv

files_path = glob.glob('1/res/*.txt')

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []


def find_value_in_file(search_string, file):
    string_with_value = re.findall(f'{search_string}.*$', file, re.MULTILINE)
    value = re.split(r':', string_with_value[0])[1].strip()
    return value


def get_data():
    main_data_values = []
    main_data_headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    for file in files_path:
        opened_file = open(file, 'rb').read()
        file_encoding = chardet.detect(opened_file)['encoding']
        opened_file_utf_8 = opened_file.decode(file_encoding).encode('utf-8').decode('utf-8')

        os_prod = find_value_in_file(main_data_headers[0], opened_file_utf_8)
        os_name = find_value_in_file(main_data_headers[1], opened_file_utf_8)
        os_code = find_value_in_file(main_data_headers[2], opened_file_utf_8)
        os_type = find_value_in_file(main_data_headers[3], opened_file_utf_8)

        os_prod_list.append(os_prod)
        os_name_list.append(os_name)
        os_code_list.append(os_code)
        os_type_list.append(os_type)

        file_main_data_values = [os_prod, os_name, os_code, os_type]
        main_data_values.append(file_main_data_values)
        main_file_name = file.split('/')[2].split('.')[0]
        main_file = open(f'1/main_data_files/main_file_{main_file_name}.txt', 'w', encoding='utf-8')
        for counter, header in enumerate(main_data_headers):
            main_file.write(f'{header}: {file_main_data_values[counter]}\n')

    return main_data_headers, main_data_values


csv_report = open('1/main_data_report.csv', 'w', encoding='utf-8')
csv_report.close()


def write_to_csv(report_link):
    data_headers, data_values = get_data()
    with open(report_link, 'w') as f:
        f_writer = csv.writer(f)
        f_writer.writerow(data_headers)
        f_writer.writerows(data_values)


write_to_csv('1/main_data_report.csv')
