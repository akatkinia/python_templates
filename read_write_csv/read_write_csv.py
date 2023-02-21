import csv


def write_csv(data):
    with open('names.csv', 'a', encoding="cp1251", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow((data['name'],
                         data['surname'],
                         data['age']))

def write_csv2(data):
    with open('names.csv', 'a', encoding="cp1251", newline="") as file:
        order = ['name', 'surname', 'age']
        writer = csv.DictWriter(file, fieldnames=order, delimiter=";")
        writer.writerow(data)


def main():
    d = {'name': 'Petr', 'surname': 'Ivanov', 'age': 21}
    d1 = {'name': 'Ivan', 'surname': 'Ivanov', 'age': 18}
    d2 = {'name': 'Ksu', 'surname': 'Ivanova', 'age': 22}

    l = [d, d1, d2]

    for i in l:
        # write_csv(i)
        write_csv2(i)

    with open('names.csv') as file:
        fieldnames = ['name', 'surname', 'age']
        reader = csv.DictReader(file, delimiter=";", fieldnames=fieldnames)

        for row in reader:
            print(row)

if __name__ == '__main__':
    main()
