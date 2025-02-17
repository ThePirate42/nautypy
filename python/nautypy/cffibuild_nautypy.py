import path
from cffi import FFI
ffibuilder = FFI()

lib_path = path.Path("../../build/src").absolute()
include_path = path.Path("../../include").absolute()


ffibuilder.set_source(
    "_nautypy",
    """
    #include "nautypy.h"   // the C header of the library
    """,
    libraries=['nautypy','nauty'],
    library_dirs=[lib_path],
    include_dirs=[include_path]
)


ffibuilder.cdef(
    """
    void canonize(int _nv, size_t _nde, size_t* _v, int* _d, int* _e, 
                  int* lab, int* ptn, int* n_auts, int*** auts);
    """
)


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
