from array import array
from typing import Callable


def create_array() -> array:
    user_array_input = input('Enter space separated integers for the array:\n')
    return array('i', list(map(lambda x: int(x.strip()), user_array_input.split(' '))))


def array_operations() -> None:
    print_array: Callable[[array], None] = lambda x: print(f'After operation, the array is as below-\n{x}\n\n')
    input_array: array = create_array()
    while True:
        operation_input = int(input("""
        Dear user, please enter the choice of operation:
        1. Insertion
        2. Appending
        3. Pop
        4. Removing
        5. Index
        6. Reverse
        
        Enter 0 to exit
        
        Your choice: 
        """))
        match operation_input:
            case 1:
                location, value = map(lambda x: int(x.strip()),
                                      input('Please enter separated the choice of location and value: ').split(' '))
                input_array.insert(location - 1, value)
                print_array(input_array)
            case 2:
                appending_value = int(input('Please enter the value to append: ').strip())
                input_array.append(appending_value)
                print_array(input_array)
            case 3:
                popping_index = int(input('Please enter the location to remove from array: ').strip())
                input_array.pop(popping_index)
                print_array(input_array)
            case 4:
                removing_value = int(input('Please enter the value to be removed found at first: '))
                input_array.remove(removing_value)
                print_array(input_array)
            case 5:
                search_value = int(input('Please enter the value to be searched for it\'s first appearance: '))
                value_index = input_array.index(search_value)
                print(f'The value was found first at location {value_index + 1} in the array\n\n')
            case 6:
                input_array.reverse()
                print_array(input_array)
            case 0:
                print(f'Program exiting..')
                import sys
                sys.exit()


def main() -> None:
    array_operations()


if __name__ == '__main__':
    main()
