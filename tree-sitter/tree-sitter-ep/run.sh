#!/bin/sh
echo "$1" > test.lp | tree-sitter parse test.lp
