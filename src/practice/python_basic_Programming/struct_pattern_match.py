'''
Exampe of Structureal Pattern Matching
'''

def run_command(command:str) -> None:
    match command:
        case 'TEST':
            print('This is Test')
        case _:
            print('Unknow Command')

run_command('TEST')
