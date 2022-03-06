files_to_gen = {}


def binfile(name):
    def _wrapper(func):
        global files_to_gen
        files_to_gen[name] = func
        return func
    return _wrapper


@binfile("0thru255")
def _0thru255():
    return bytes(range(256))


def main():
    for name, gen in files_to_gen.items():
        with open(name + ".bin", mode="wb") as f:
            f.write(gen())


if __name__ == "__main__":
    main()
