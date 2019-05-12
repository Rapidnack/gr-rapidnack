INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_RAPIDNACK rapidnack)

FIND_PATH(
    RAPIDNACK_INCLUDE_DIRS
    NAMES rapidnack/api.h
    HINTS $ENV{RAPIDNACK_DIR}/include
        ${PC_RAPIDNACK_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    RAPIDNACK_LIBRARIES
    NAMES gnuradio-rapidnack
    HINTS $ENV{RAPIDNACK_DIR}/lib
        ${PC_RAPIDNACK_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(RAPIDNACK DEFAULT_MSG RAPIDNACK_LIBRARIES RAPIDNACK_INCLUDE_DIRS)
MARK_AS_ADVANCED(RAPIDNACK_LIBRARIES RAPIDNACK_INCLUDE_DIRS)

