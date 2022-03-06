import pathlib

files_to_gen = {}
here = pathlib.Path(__file__).parent


def binfile(name):
    def _wrapper(func):
        global files_to_gen
        files_to_gen[name] = func
        return func

    return _wrapper


@binfile("0thru255")
def _():
    return bytes(range(256))


@binfile("justascii")
def _():
    return "I've got a lovely bunch of coconuts.".encode("ascii")


@binfile("utf32")
def _():
    return "\N{COCONUT}\N{COCONUT}\N{COCONUT}".encode("utf-32")


def main():
    for name, gen in files_to_gen.items():
        with open(here / (name + ".bin"), mode="wb") as f:
            f.write(gen())


if __name__ == "__main__":
    main()
