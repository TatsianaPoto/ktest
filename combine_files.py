def combine_files(input_files, output_file):
    # Используем множество для хранения уникальных данных
    combined_data = set()  
    for input_file in input_files:
        with open(input_file, 'r') as infile:
            data = infile.read()
             # Разделяем строки по переносам строк и добавляем в множество
            combined_data.update(data.splitlines()) 
    with open(output_file, 'w') as outfile:
        # Записываем уникальные данные в выходной файл
        outfile.write('\n'.join(combined_data))  

if __name__ == "__main__":
    input_files = ['churn.all.txt', 'churn.data.txt', 'churn.test.txt']
    output_file = 'combined_output.txt'
    combine_files(input_files, output_file)
    print("Files combined successfully.")
