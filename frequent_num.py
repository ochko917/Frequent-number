from collections import Counter

def frequent_num(lst):
    count = Counter(lst)
    most_common = count.most_common(1)[0]
    return most_common[0], most_common[1]

def main():
    try:
        user_list = list(map(int, input("Enter a number ").split()))
        most_frequent, count = frequent_num(user_list)
        print(f"The most frequent number: {most_frequent}, Appears: {count} times.")
    except ValueError:
        print("Invalid input!")

if __name__ == "__main__":
    main()
