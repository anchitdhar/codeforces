def slve(year):
    while True:
        year = str(int(year) + 1)
        if (len(set(year)) == 4):
            return year

if __name__ == "__main__":
    print(slve(input()))    