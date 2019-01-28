# prints hello

import utils

@utils.benchmark
def say_hi():
    print("hello Git!")

@utils.benchmark
def say_bye():
    print("Goodbye!")

if __name__ == "__main__":
    say_hi()
    say_bye()
