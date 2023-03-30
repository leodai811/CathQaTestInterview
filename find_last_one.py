def find_last_qa_member(n):
    people = list(range(1, n + 1))
    index = 0
    while len(people) > 1:
        index = (index + 2) % len(people)
        people.pop(index)
    return people[0]

while True:
    try:
        n = int(input("輸入活動人數（範圍：1-100）："))
        if 1 <= n <= 100:
            break
        else:
            print("輸入錯誤，請輸入1到100之間的整数。")
    except ValueError:
        print("輸入錯誤，請輸入一個整數。")

result = find_last_qa_member(n)
print("最後留下來的同事，是第{}順位。".format(result))
