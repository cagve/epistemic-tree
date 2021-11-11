from tree_sitter import Language, Parser

Language.build_library(
  # Store the library in the `build` directory
  'tree-sitter/build/my-languages.so',

  # Include one or more languages
  [
    'tree-sitter/tree-sitter-ep',
  ]
)
