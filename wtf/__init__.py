import sys


class WTFHandler(object):
    """
    Post-mortem debug handler.

    After an exception, a Pdb debugger will be started in the right frame.

    Instances can be used as a context manager:

        WTF = WTFHandler()

        with WTF:
            raise Something

    Or, can be used as a function call:

        WTF = WTFHandler()

        try:
            raise Something
        except:
            WTF()

    In both cases, the debugger will start on the 'raise Something' line.
    """

    def _build_pdb(self):
        """
        Called without arguments, this should return the ``pdb.Pdb``
        instance we will use for our debugging.
        """
        return pdb.Pdb()

    def start(self, wtf_frame, traceback):
        p = self._build_pdb()
        p.reset()
        self._interaction(p, wtf_frame, traceback)

    def _interaction(self, p, wtf_frame, traceback):
        p.interaction(None, traceback)

    def __call__(self):
        self.start(sys._getframe().f_back, sys.exc_info()[2])

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        if traceback:
            self.start(sys._getframe().f_back, traceback)


class WTFHereHandler(WTFHandler):
    """
    The Same as WTFHandler, except that the debuggin starts at the same frame
    where WTF was used.
    """

    def _interaction(self, p, wtf_frame, traceback):
        # We are basically unrolling a call to Pbd.interaction(None, traceback)
        # and modifying it so that we start on the frame where 'WTF' was used.

        ## <Pdb.setup>

        p.forget()
        p.stack, p.curindex = p.get_stack(None, traceback)

        # here we change the current (deepest) frame to wtf_frame.
        for i,(f,ln) in enumerate(p.stack[p.curindex::-1]):
            if f is wtf_frame:
                p.curindex -= i
                break
        else:
            raise RuntimeError("You found a bug! Please report this at http://github.com/k0001/wtf/issues")

        p.curframe = p.stack[p.curindex][0]

        # The f_locals dictionary is updated from the actual frame
        # locals whenever the .f_locals accessor is called, so we
        # cache it here to ensure that modifications are not overwritten.
        p.curframe_locals = p.curframe.f_locals
        p.execRcLines()

        ## </Pdb.setup>

        p.print_stack_entry(p.stack[p.curindex])
        p.cmdloop()
        p.forget()


try:
    # Use IPython if available.
    from IPython.Debugger import Pdb
    from IPython.Shell import IPShell
    from IPython import ipapi

    shell = IPShell(argv=[''])


    class IPythonWTFHandler(WTFHandler):
        def _build_pdb(self):
            return Pdb(ipapi.get().options.colors)

    class IPythonWTFHereHandler(IPythonWTFHandler, WTFHereHandler):
        def _interaction(self, p, wtf_frame, traceback):
            __IPYTHON__.set_completer_frame(None)
            super(IPythonWTFHereHandler, self)._interaction(p, wtf_frame, traceback)

    WTF = IPythonWTFHandler()
    WTFIGOH = IPythonWTFHereHandler()

except ImportError:
    WTF = WTFHandler()
    WTFIGOH = WTFHereHandler()

# For the lazy...
WTF.IGOH = WTFIGOH

