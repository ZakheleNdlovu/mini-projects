import random

dice = range(1,7)


while True:
    roll_dice = input('Roll dice (Y) or (N): ').lower()
    if roll_dice == 'y':
        dice_roll = random.choice(dice)
        if dice_roll == 1:
            print('+--------+')
            print('|     *     |')
            print('+--------+')

        if dice_roll == 2:
            print('+----------------+')
            print('|  *                 |')
            print('|                    |')
            print('|                *   |')
            print('+----------------+')

        if dice_roll == 3:
            print('+----------------+')
            print('|  *                 |')
            print('|        *           |')
            print('|              *     |')
            print('+----------------+')

        if dice_roll == 4:
            print('+----------------+')
            print('|    *           *   |')
            print('|                     |')
            print('|    *          *    |')
            print('+----------------+')

        if dice_roll == 5:
            print('+----------------+')
            print('|    *           *   |')
            print('|          *         |')
            print('|    *          *    |')
            print('+----------------+')

        if dice_roll == 6:
            print('+----------------+')
            print('|    *          *    |')
            print('|    *          *    |')
            print('|    *          *    |')
            print('+----------------+')

    elif roll_dice == 'n':
        print('Goodbye!')
        break

    else:
        print('Invalid input')