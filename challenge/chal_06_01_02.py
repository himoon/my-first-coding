def gugudan(number):
    for n in range(1, 10):
        print(str(number) + " x " + str(n) + " = " + str(number * n))


def main():
    user_input = input("숫자를 입력하세요: ")
    user_input = int(user_input)

    if user_input >= 2 and user_input <= 9:
        gugudan(user_input)
    else:
        print("숫자 2~9까지 입력 가능합니다.")


main()
