#! /usr/bin/env python
# encoding: utf-8

APPNAME = "LearnSFML"
VERSION = "0.0"

top = "."
out = "build"

DIRS = "source test"

import glob, os

from waflib.Configure import conf

def print_process(
        message,
        lines=70):
    """..."""
    len_msg=\
        int((lines - len(message))/2)
    message_to_print=\
        len_msg * "-" + message + len_message * "-"
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
        ["bz_2",
         "gsl",
         "gslcblas",
         "dl"])
    context.env.append_unique(
        "CATCH_PATH",
        "/usr/local/include/Catch")


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
    conf.setenv(
        "alternative-gcc",
        env=conf.env.derive())
    conf.env.CXXFLAGS=[
        '-Wall',
        '-Wno-unknown-pragmas',
        '-Wextra',
        '-Wconversion',
        '-O3',
        '-std=c++14']
    conf.define(
        'RELEASE', 1)
    conf.setenv(
        'alternative-gcc-6-debug',
        env=conf.env.derive())
    conf.env.CXXFLAGS=[
        '-DDEBUG',
        '-D_GLIBCXX_DEBUG',
        '-D_GLIBCXX_DEBUG_PEDANTIC',
        '-g', '-std=c++14']
    conf.define('DEBUG', 1)

def configure_clang(conf):
    """..."""
    conf.find_program(
        "clang", var="CXX", mandatory=True)
    conf.load(
        "clang++")
    global_env(conf)
    conf.env.append_unique(
        "LDFLAGS_N",
        ["pthread",
         "util",
         "m"])
    conf.setenv(
        "alternative-clang",
        env=conf.env.derive())
    conf.env.CXXFLAGS=[
        '-Wall',
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
         '-std=c++1z']
    conf.env.append_unique(
        "LIBS",
        ["c++", "c++abi"])
    conf.define(
        "RELEASE", 1)
    conf.setenv(
        "alternative-clang-debug",
        env=conf.env.derive())
    conf.env.CXXFLAGS=[
        "-g",
        "-glidb",
        "-Wdocumentation"]
    conf.define(
        "DEBUG", 1)

