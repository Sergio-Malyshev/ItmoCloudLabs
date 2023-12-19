from datetime import datetime

def main():
    currrent_time = datetime.time

    with open('wish.txt', 'w') as f:
        f.write('Good luck!\n')
        f.write(f'Current time - {currrent_time}')


main()
