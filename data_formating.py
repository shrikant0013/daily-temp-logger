import json
import csv
from collections import OrderedDict

with open("fridge_clean.txt", "r", encoding='utf-8') as data_file:
    lines = data_file.readlines()

    entries_list = []

    for line in lines:
        entry_dict = {}
        tokens = line.split(' ')
        entry_dict['id'] = tokens[0]
        entry_dict['date'] = tokens[1]
        entry_dict['time'] = tokens[2]
        entry_dict['temp'] = tokens[3]

        entries_list.append(entry_dict)

    for entry in entries_list:
        print(json.dumps(entry, indent=4))
        break

    unique_entries = []
    unique_entry = OrderedDict()
    for entry in entries_list:
        key = entry['date']
        if key not in unique_entry.keys():
            min_max_dict = {"min": entry["temp"], "max": entry["temp"]}
            unique_entry.update({key : min_max_dict})
        else:
            temp_dict = unique_entry[key]
            new_value = float(entry['temp'])
            min = float(temp_dict['min'])
            max = float(temp_dict['max'])

            if new_value < min:
                temp_dict['min'] = new_value
            elif new_value > max:
                temp_dict['max'] = new_value

            unique_entry.update({key: temp_dict})

    # with open ("final_output.txt", "w") as output:
    #     output.write(json.dumps(unique_entry, indent=4))

    csv_header = ["Date", "Minimum Temperature", "Maximum Temperature"]
    csv_data = [csv_header]

    for key, item in unique_entry.items():
        csv_entry = [key, item['min'], item['max']]
        csv_data.append(csv_entry)

    with open("final_output.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file,dialect='excel')

        for row in csv_data:
            csv_writer.writerow(row)

    #print(json.dumps(unique_entry, indent=4))