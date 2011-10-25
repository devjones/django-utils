import subprocess

def istextfile(name):
    file_result = subprocess.check_output(['file', name])

    try:
        file_type = file_result.split(':')
    except:
        return False

    return 'text' in file_type[1]
