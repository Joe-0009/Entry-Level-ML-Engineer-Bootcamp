
kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }


def print_dic():
    for key, value in kata.items():
        print(f"{key} was created by {value}")


print_dic()
