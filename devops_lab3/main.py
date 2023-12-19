from datetime import datetime


def main():
    current_time = datetime.now().time()

    with open('wish.txt', 'w') as f:
        f.write('Good luck!\n')
        f.write(f'Current time - {current_time}')


main()
