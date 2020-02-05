import re
from operator import xor
from pprint import pprint
import csv

def brake_names(a_list):
    for contact in a_list:
        if ' ' in contact[0]:
            temp_list = contact[0].split(sep=' ', maxsplit=1)
            contact[0] = temp_list[0]
            contact[1] = temp_list[1]

    for contact in a_list:
        if ' ' in contact[1]:
            temp_list = contact[1].split(sep=' ')
            contact[1] = temp_list[0]
            contact[2] = temp_list[1]
    
    return contacts_list


def delete_duplicates(a_list):
    dic = {}
    out_list = []
    for contact in a_list:
        surname = contact[0]
        if surname not in dic.keys():
            dic[surname] = contact
        else:
            for i in range(1, 7):
                if xor(bool(dic[surname][i]), bool(contact[i])):
                # if not dic[surname][i] xor not contact[i]:
                    dic[surname][i] += contact[i]
    for key in dic.keys():
        out_list.append(dic[key])
    return out_list

def do_regexp(text):
    pattern1 = re.compile(r"\+?[78]\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})")
    replacer1 = r"+7(\1)\2-\3-\4"
    result1 = pattern1.sub(replacer1, text)
    pattern2 = re.compile(r"\W*доб(\.?\s?)(\d+)\W*")
    replacer2 = r" доб.\2"
    final_result = pattern2.sub(replacer2, result1)
    return final_result


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    contacts_list = brake_names(contacts_list)
    new_contacts_list = delete_duplicates(contacts_list)
    for contact in new_contacts_list:
        contact[5] = do_regexp(contact[5])
    pprint(new_contacts_list)
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)

