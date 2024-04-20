import subprocess


def normal_input():
    untrusted_input = "normal input"
    subprocess.run(["echo_args.bat", untrusted_input])


def eval_calc_input():
    untrusted_input = "&calc.exe"
    subprocess.run(["echo_args.bat", untrusted_input])


def eval_py_input():
    untrusted_input = "&calc.exe"
    subprocess.run(["python.exe", "-m", "timeit", untrusted_input], shell=True)


def cve():
    untrusted_input = "&calc.exe"
    subprocess.run(["echo_args.bat", untrusted_input], shell=False)


def main():
    cve()
    # normal_input()
    # eval_calc_input()
    # eval_py_input()


if __name__ == "__main__":
    main()