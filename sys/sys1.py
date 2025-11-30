import sys


def show_argv():
    print("=== sys.argv (command-line arguments) ===")
    print(f"Raw argv list: {sys.argv}")
    script = sys.argv[0]
    args = sys.argv[1:]
    print(f"Script name : {script}")
    print(f"Arguments   : {args}")
    print()


def echo_stdin():
    print("=== sys.stdin / sys.stdout demo ===")
    print("Type something and press Enter (empty line to stop):")
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line == "":
            print("Empty line, stopping stdin demo.\n")
            break
        # this goes to stdout
        print(f"you typed: {line}")
    print()


def show_stderr():
    print("=== sys.stderr demo ===")
    print("This is a normal message on stdout.")
    print("This is an error message on stderr.", file=sys.stderr)
    print()


def show_env_info():
    print("=== Interpreter / environment info ===")
    print(f"Python version : {sys.version}")
    print(f"Executable path: {sys.executable}")
    print("First few entries in sys.path:")
    for p in sys.path[:5]:
        print("  ", p)
    print()


def maybe_exit_with_error():
    print("=== sys.exit demo ===")
    if "--fail" in sys.argv:
        print("Simulating failure, exiting with code 1...")
        sys.exit(1)  # non-zero means error
    else:
        print("No --fail flag, exiting with code 0 (success).")
        # returning from main (or just ending the script) is equivalent to sys.exit(0)


def main():
    show_argv()
    echo_stdin()
    show_stderr()
    show_env_info()
    maybe_exit_with_error()


if __name__ == "__main__":
    main()