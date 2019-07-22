import sys
import hash_algorithms

FNV_1 = "fnv-1"

algorithms = [FNV_1]

def print_title(version):
    print(" __   __  _______  _______  __   __  _______  ______   \n" +
          "|  | |  ||   _   ||       ||  | |  ||       ||    _ |  \n" +
          "|  |_|  ||  |_|  ||  _____||  |_|  ||    ___||   | ||  \n" +
          "|       ||       || |_____ |       ||   |___ |   |_||_ \n" +
          "|       ||       ||_____  ||       ||    ___||    __  |\n" +
          "|   _   ||   _   | _____| ||   _   ||   |___ |   |  | |\n" +
          "|__| |__||__| |__||_______||__| |__||_______||___|  |_|\n" +
          "                                               Ver. " + version + "\n"
          )


def hash_exec(algorithm, target_str):
    if algorithm == FNV_1:
        return hash_algorithms.fnv1.hash_exec(target_str)


def main():
    args = sys.argv

    print_title("0.1")

    if len(args) < 3:
        print("usage:  python3 main.py hash_algorithm string")

    algorithm = args[1]
    target_str = args[2]

    print("algorithm is \"" + algorithm + "\"")
    print("target string is \"" + target_str + "\"")

    print("")

    if algorithm not in algorithms:
        print("\"" + algorithm + "\" is not available now. You can use following algorithms.")
        print(algorithms)

    output = hash_exec(algorithm, target_str)
    print("result is \"{}\"".format(output))

if __name__ == "__main__":
    main()
