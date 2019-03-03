#! /usr/bin/env python
# encoding: utf-8

APPNAME = "LearnSFML"
VERSION = "0.0"

top = "."
out = "build"

DIRS = "src"

import glob, os

from waflib.Configure import conf

def print_process(
        message,
        lines=70):
    """..."""
    len_msg=\
        int((lines - len(message))/2)
    message_to_print=\
        len_msg * "-" + message + len_msg * "-"
    if len(message_to_print) < lines:
        message_to_print=\
            message_to_print.split(' ')[0] +\
            ' ' + message_to_print.split(' ')[1]
    print(lines * '=')
    print(message_to_print)
    print(lines * '=')

def global_env(context):
    context.env.appname=\
        APPNAME
    context.env.append_unique(
        "LDFLAGS_N",
        ["sfml-graphics",
         "sfml-window",
         "sfml-system",
         "bz2",
         "gsl",
         "gslcblas",
         "dl",
         "stdc++fs"])
    context.env.LIBPATH_MYLIB=\
        ['/usr/local/lib']
    context.env.append_unique(
        "INCLUDES_REL",
        ["include",
         "include/utils"])

def configure_gcc(conf):
    """..."""
    conf.find_program(
        "g++",
        var="C",
        mandatory=True)
    conf.load("g++")
    conf.find_program(
        "gcc",
        var="C",
        mandatory=True)
    global_env(conf)
    conf.env.append_unique(
        "STLIB",
        "stdc++")
    conf.env.append_unique(
        "LDFLAGS_N",
        ["stdc++fs"])
    conf.env.append_unique(
        "CXXFLAGS",
        ["-std=c++17"])

    conf.setenv(
        "gcc-release",
        env=conf.env.derive())
    conf.env.append_unique(
        "CXXFLAGS",
        ['-Wall',
         '-Wno-unknown-pragmas',
         '-Wextra',
         '-Wconversion',
         '-O3'])
    conf.define(
        'RELEASE', 1)

    conf.setenv(
        'gcc-debug',
        env=conf.env.derive())
    conf.env.append_unique(
        "CXXFLAGS",
        ['-DDEBUG',
        '-D_GLIBCXX_DEBUG',
        '-D_GLIBCXX_DEBUG_PEDANTIC',
        '-g'])
    conf.define('DEBUG', 1)

def configure_clang(conf):
    """..."""
    conf.find_program(
        "clang",
        var="C",
        mandatory=True)
    conf.load(
        "clang")
    conf.find_program(
        "clang++",
        var="CXX",
        mandatory=True)
    conf.load(
        "clang++")
    global_env(conf)
    conf.env.append_unique(
        "LIBPATH_FS",
        ["/usr/local/opt/llvm/lib"])
    conf.env.append_unique(
        "LDFLAGS_N",
        ["pthread",
         "util",
         "c++fs",
         "m"])
    conf.env.append_unique(
        "CATCH_PATH",
        "/usr/local/include/Catch")

    conf.setenv(
        "clang-release",
        env=conf.env.derive())
    conf.env.append_unique(
        "CXXFLAGS",
        ['-Wall',
         '-Wno-unknown-pragmas',
         '-Wextra',
         '-Wconversion',
         '-fno-strict-aliasing',
         '-D_FORTIFY_SOURCE=2',
         '-fstack-protector',
         '--param=ssp-buffer-size=4',
         '-Wformat',
         '-Werror=format-security',
         '-fwrapv',
         '-O3',
         "-std=c++17",
         "-Wl",
         "-stdlib=libc++"])
    conf.env.LINKFLAGS=[
        "-std=c++17",
        "-stdlib=libc++"]
    conf.env.append_unique(
        "LIBS",
        ["c++", "c++abi"])
    conf.define(
        "RELEASE", 1)

    conf.setenv(
        "clang-debug",
        env=conf.env.derive())
    conf.env.append_unique(
        "CXXFLAGS",
        ["-g",
        "-glidb",
        "-Wdocumentation"])
    conf.define(
        "DEBUG", 1)

def options(opt):
    opt.load("compiler_cxx")
    opt.load("compiler_c")

    print("read options")
    opt.add_option(
        "--clang",
        action="store_true",
        default=False)

def configure(conf):
    """..."""
    print_process("configuring gcc")
    configure_gcc(conf)

    conf.setenv("bebo") #this can be anything
    print_process("configuring clang")
    configure_clang(conf)


from waflib.Build import BuildContext

class gcc_release(BuildContext):
    cmd= "build_release_gcc"
    variant= "gcc-release"

class gcc_debug(BuildContext):
    cmd= "build_debug_gcc"
    variant= "gcc-debug"

class clang_release(BuildContext):
    cmd= "build_release_clang"
    variant= "clang-release"

class clang_debug(BuildContext):
    cmd= "build_debug_clang"
    variant= "clang-debug"

def make_symlinks(bld):
    """..."""
    try:
        os.makedirs(
            os.path.join(
                "build",
                "apps"))
    except:
        print(
            "directory 'apps' already exists")

    def __make_command(target):
        return ("(cd build/apps; ln -sf " +
                os.path.join(
                    "..",
                    bld.variant,
                    target) + 
                ' ' +
                os.path.join(
                    target.split('/')[-1] + ')'))
    for target in bld.env.targets:
        os.system(
            __make_command(
                target))

def build(bld):
    """..."""
    print(
        "building at",
        bld.path.abspath())
    if not bld.variant:
        bld.fatal(
        """Please invoke a variant to build:\n
        1. waf build_release_gcc"\n
        2. waf build_debug_gcc\n
        3. waf build_release_clang\n
        4. waf build_debug_clang\n""")

    print_process("Building " + bld.variant)
    bld.env.targets= []
    bld.recurse(DIRS)
    print(
        "targets built: {}".format(
            bld.env.targets))
    bld.add_post_fun(make_symlinks)
