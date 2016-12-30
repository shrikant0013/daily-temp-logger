

with open("fridge.txt", 'r', encoding='utf-8') as date_file:
    lines = date_file.readlines()
    with open("fridge_clean.txt", "w", encoding='utf-8') as clean_data_file:
        for line in lines:
            tokens = line.split(' ')
            if len(tokens) == 6:
                clean_data_file.write(line)