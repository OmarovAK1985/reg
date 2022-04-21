import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

    header = contacts_list.pop(0)


print(header)
for i in contacts_list:
    print(i)
print("______________________")
phone_number_list = []
my_list = []
for i in contacts_list:
    regular_search = r"\+?([1-9])\s?[\(]?([0-9]{3})[\)]?\s?[-]?([0-9]{3})[-]?([0-9]{2})[-]?([0-9]{2})\s?[\(]?([" \
                         r"доб.]{0,4})\s*([0-9]{0,4})[\)]?"
    regular_edit = r"+7(\2)\3\4\5 \6\7"
    phone_number = re.sub(regular_search, regular_edit, i[5])
    last_name = re.split(r' ', i[0])
    first_name = re.split(r' ', i[1])
    surname = re.split(r' ', i[2])
    local_my_list = []
    if len(last_name) == 3 and re.findall(r'\w', last_name[0]):
        my_list.append(last_name)
    if len(first_name) == 2 and re.findall(r'', surname[0]):
        local_my_list = [last_name[0]]
        for k in first_name:
            local_my_list.append(k)
        my_list.append(local_my_list)
    if len(last_name) == 1 and re.findall(r'\w', last_name[0]) and len(first_name) == 1 and re.findall(r'\w', first_name[0]) and len(surname) == 1 and re.findall(r'\w', surname[0]):
        local_my_list = [last_name[0], first_name[0], surname[0]]
        my_list.append(local_my_list)
    if len(last_name) == 2 and re.findall(r'', first_name[0]) and re.findall(r'', surname[0]):
        local_my_list = [last_name[0], last_name[1], surname[0]]
        my_list.append(local_my_list)
    phone_number_list.append(phone_number)


for i in contacts_list:
    count = 0
    while count != 3:
        i.pop(0)
        count = count + 1


for i, k in zip(contacts_list, phone_number_list):
    i.pop(2)
    i.insert(2, k)

for i, k in zip(contacts_list, my_list):
    k.extend(i)

last_name = None
first_name = None
c = 0
double_list = []
for i in my_list:
    if len(i) != 7:
        i.pop(-1)
    last_name = i[0]
    first_name = i[1]
    count = 0
    for k in my_list:
        if re.findall(last_name, k[0]) and re.findall(first_name, k[1]):
            count = count + 1
            if count > 1:
                double_list.append(my_list.pop(c))
    c = c + 1

for i in double_list:
    last_name = i[0]
    first_name = i[1]
    count = 0
    for k in my_list:
        if re.findall(last_name, k[0]) and re.findall(first_name, k[1]):
            while count < len(k):
                if len(i[count]) > len(k[count]):
                    k.pop(count)
                    k.insert(count, i[count])
                count = count + 1

my_list.insert(0, header)
for i in my_list:
    print(i)

print(my_list)


with open("phonebook.csv", 'w', encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=",")
    datawriter.writerows(my_list)


































