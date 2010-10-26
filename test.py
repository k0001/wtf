from wtf import WTF


def test():
    try:
        raise RuntimeError("A PDB debugger should have been started now, as a function call. Press 'c' to continue.")
    except:
        WTF()

    try:
        with WTF: # <-- python2.5 and older will raise "SyntaxError"
            raise RuntimeError("A PDB debugger should have been started now, as a context manager. Press 'c' to continue.")
    except RuntimeError:
        pass



if __name__ == '__main__':
    # Run some manual tests
    test()


