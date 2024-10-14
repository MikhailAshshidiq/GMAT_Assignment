import csv

def check():
    reader = csv.reader(csv_data.splitlines())
    for row in reader:
        pass
    last_row = row
    if last_row[-1][-1] == ';':
        return True
    else:
        print("No")
        exit()
        return False
    
def check_time(time):
    try:
        data = csv.reader(time.splitlines(), delimiter=":")
        try:
            check = next(data)
        except:
            print("No")
            exit()

        if len(check) != 3:
            print("No")
            exit()
        elif int(check[0]) > 24:
            print("No")
            exit()
        elif int(check[1]) > 59:
            print("No")
            exit()
        elif int(check[2]) > 59:
            print("No")
            exit()
    except ValueError:
        print("No")
        exit()
        return False

no_id: str = input()
no_elements = int(input())
csv_data = input()

# print(no_id)
# print(no_elements)
# print(csv_data)
try:
    reader = csv.reader(csv_data.splitlines(), delimiter= ",", lineterminator=';')
    data = next(reader)

except csv.Error:
    print("CSV error")
    exit()

if data[0] != no_id :
    print("No")
    exit()

if len(data) != no_elements:
    print("No")
    exit()

check_time(data[1])

check()

print("Yes")

# Source:
# https://youtu.be/_r0jzrlcDPM?si=1khXSbPt5NZ_b0Ek
# https://www.geeksforgeeks.org/how-to-take-integer-input-in-python/
# https://www.w3schools.com/python/ref_string_splitlines.asp
# https://docs.python.org/3/library/csv.html


