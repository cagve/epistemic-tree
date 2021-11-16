#include <tree_sitter/parser.h>

#if defined(__GNUC__) || defined(__clang__)
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmissing-field-initializers"
#endif

#define LANGUAGE_VERSION 13
#define STATE_COUNT 13
#define LARGE_STATE_COUNT 5
#define SYMBOL_COUNT 15
#define ALIAS_COUNT 0
#define TOKEN_COUNT 9
#define EXTERNAL_TOKEN_COUNT 0
#define FIELD_COUNT 4
#define MAX_ALIAS_SEQUENCE_LENGTH 3
#define PRODUCTION_ID_COUNT 5

enum {
  anon_sym_LPAREN = 1,
  anon_sym_RPAREN = 2,
  sym_not = 3,
  sym_and = 4,
  sym_iff = 5,
  sym_eq = 6,
  sym_or = 7,
  sym_atom = 8,
  sym_formula = 9,
  sym__monary_expression = 10,
  sym__binary_expression = 11,
  sym__par_expression = 12,
  sym__monary_operator = 13,
  sym__binary_operator = 14,
};

static const char * const ts_symbol_names[] = {
  [ts_builtin_sym_end] = "end",
  [anon_sym_LPAREN] = "(",
  [anon_sym_RPAREN] = ")",
  [sym_not] = "not",
  [sym_and] = "and",
  [sym_iff] = "iff",
  [sym_eq] = "eq",
  [sym_or] = "or",
  [sym_atom] = "atom",
  [sym_formula] = "formula",
  [sym__monary_expression] = "_monary_expression",
  [sym__binary_expression] = "_binary_expression",
  [sym__par_expression] = "_par_expression",
  [sym__monary_operator] = "_monary_operator",
  [sym__binary_operator] = "_binary_operator",
};

static const TSSymbol ts_symbol_map[] = {
  [ts_builtin_sym_end] = ts_builtin_sym_end,
  [anon_sym_LPAREN] = anon_sym_LPAREN,
  [anon_sym_RPAREN] = anon_sym_RPAREN,
  [sym_not] = sym_not,
  [sym_and] = sym_and,
  [sym_iff] = sym_iff,
  [sym_eq] = sym_eq,
  [sym_or] = sym_or,
  [sym_atom] = sym_atom,
  [sym_formula] = sym_formula,
  [sym__monary_expression] = sym__monary_expression,
  [sym__binary_expression] = sym__binary_expression,
  [sym__par_expression] = sym__par_expression,
  [sym__monary_operator] = sym__monary_operator,
  [sym__binary_operator] = sym__binary_operator,
};

static const TSSymbolMetadata ts_symbol_metadata[] = {
  [ts_builtin_sym_end] = {
    .visible = false,
    .named = true,
  },
  [anon_sym_LPAREN] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_RPAREN] = {
    .visible = true,
    .named = false,
  },
  [sym_not] = {
    .visible = true,
    .named = true,
  },
  [sym_and] = {
    .visible = true,
    .named = true,
  },
  [sym_iff] = {
    .visible = true,
    .named = true,
  },
  [sym_eq] = {
    .visible = true,
    .named = true,
  },
  [sym_or] = {
    .visible = true,
    .named = true,
  },
  [sym_atom] = {
    .visible = true,
    .named = true,
  },
  [sym_formula] = {
    .visible = true,
    .named = true,
  },
  [sym__monary_expression] = {
    .visible = false,
    .named = true,
  },
  [sym__binary_expression] = {
    .visible = false,
    .named = true,
  },
  [sym__par_expression] = {
    .visible = false,
    .named = true,
  },
  [sym__monary_operator] = {
    .visible = false,
    .named = true,
  },
  [sym__binary_operator] = {
    .visible = false,
    .named = true,
  },
};

enum {
  field_left_term = 1,
  field_operator = 2,
  field_right_term = 3,
  field_term = 4,
};

static const char * const ts_field_names[] = {
  [0] = NULL,
  [field_left_term] = "left_term",
  [field_operator] = "operator",
  [field_right_term] = "right_term",
  [field_term] = "term",
};

static const TSFieldMapSlice ts_field_map_slices[PRODUCTION_ID_COUNT] = {
  [1] = {.index = 0, .length = 2},
  [2] = {.index = 2, .length = 3},
  [3] = {.index = 5, .length = 2},
  [4] = {.index = 7, .length = 3},
};

static const TSFieldMapEntry ts_field_map_entries[] = {
  [0] =
    {field_operator, 0, .inherited = true},
    {field_term, 0, .inherited = true},
  [2] =
    {field_left_term, 0, .inherited = true},
    {field_operator, 0, .inherited = true},
    {field_right_term, 0, .inherited = true},
  [5] =
    {field_operator, 0},
    {field_term, 1},
  [7] =
    {field_left_term, 0},
    {field_operator, 1},
    {field_right_term, 2},
};

static const TSSymbol ts_alias_sequences[PRODUCTION_ID_COUNT][MAX_ALIAS_SEQUENCE_LENGTH] = {
  [0] = {0},
};

static const uint16_t ts_non_terminal_alias_map[] = {
  0,
};

static bool ts_lex(TSLexer *lexer, TSStateId state) {
  START_LEXER();
  eof = lexer->eof(lexer);
  switch (state) {
    case 0:
      if (eof) ADVANCE(5);
      if (lookahead == '&') ADVANCE(1);
      if (lookahead == '(') ADVANCE(6);
      if (lookahead == ')') ADVANCE(7);
      if (lookahead == '-') ADVANCE(8);
      if (lookahead == '<') ADVANCE(2);
      if (lookahead == '=') ADVANCE(3);
      if (lookahead == '|') ADVANCE(4);
      if (lookahead == '\t' ||
          lookahead == '\n' ||
          lookahead == '\r' ||
          lookahead == ' ') SKIP(0)
      if (('p' <= lookahead && lookahead <= 'z')) ADVANCE(13);
      END_STATE();
    case 1:
      if (lookahead == '&') ADVANCE(9);
      END_STATE();
    case 2:
      if (lookahead == '>') ADVANCE(11);
      END_STATE();
    case 3:
      if (lookahead == '>') ADVANCE(10);
      END_STATE();
    case 4:
      if (lookahead == '|') ADVANCE(12);
      END_STATE();
    case 5:
      ACCEPT_TOKEN(ts_builtin_sym_end);
      END_STATE();
    case 6:
      ACCEPT_TOKEN(anon_sym_LPAREN);
      END_STATE();
    case 7:
      ACCEPT_TOKEN(anon_sym_RPAREN);
      END_STATE();
    case 8:
      ACCEPT_TOKEN(sym_not);
      END_STATE();
    case 9:
      ACCEPT_TOKEN(sym_and);
      END_STATE();
    case 10:
      ACCEPT_TOKEN(sym_iff);
      END_STATE();
    case 11:
      ACCEPT_TOKEN(sym_eq);
      END_STATE();
    case 12:
      ACCEPT_TOKEN(sym_or);
      END_STATE();
    case 13:
      ACCEPT_TOKEN(sym_atom);
      END_STATE();
    default:
      return false;
  }
}

static const TSLexMode ts_lex_modes[STATE_COUNT] = {
  [0] = {.lex_state = 0},
  [1] = {.lex_state = 0},
  [2] = {.lex_state = 0},
  [3] = {.lex_state = 0},
  [4] = {.lex_state = 0},
  [5] = {.lex_state = 0},
  [6] = {.lex_state = 0},
  [7] = {.lex_state = 0},
  [8] = {.lex_state = 0},
  [9] = {.lex_state = 0},
  [10] = {.lex_state = 0},
  [11] = {.lex_state = 0},
  [12] = {.lex_state = 0},
};

static const uint16_t ts_parse_table[LARGE_STATE_COUNT][SYMBOL_COUNT] = {
  [0] = {
    [ts_builtin_sym_end] = ACTIONS(1),
    [anon_sym_LPAREN] = ACTIONS(1),
    [anon_sym_RPAREN] = ACTIONS(1),
    [sym_not] = ACTIONS(1),
    [sym_and] = ACTIONS(1),
    [sym_iff] = ACTIONS(1),
    [sym_eq] = ACTIONS(1),
    [sym_or] = ACTIONS(1),
    [sym_atom] = ACTIONS(1),
  },
  [1] = {
    [sym_formula] = STATE(8),
    [sym__monary_expression] = STATE(9),
    [sym__binary_expression] = STATE(10),
    [sym__par_expression] = STATE(7),
    [sym__monary_operator] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(3),
    [sym_not] = ACTIONS(5),
    [sym_atom] = ACTIONS(7),
  },
  [2] = {
    [sym_formula] = STATE(11),
    [sym__monary_expression] = STATE(9),
    [sym__binary_expression] = STATE(10),
    [sym__par_expression] = STATE(7),
    [sym__monary_operator] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(3),
    [sym_not] = ACTIONS(5),
    [sym_atom] = ACTIONS(7),
  },
  [3] = {
    [sym_formula] = STATE(5),
    [sym__monary_expression] = STATE(9),
    [sym__binary_expression] = STATE(10),
    [sym__par_expression] = STATE(7),
    [sym__monary_operator] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(3),
    [sym_not] = ACTIONS(5),
    [sym_atom] = ACTIONS(7),
  },
  [4] = {
    [sym_formula] = STATE(6),
    [sym__monary_expression] = STATE(9),
    [sym__binary_expression] = STATE(10),
    [sym__par_expression] = STATE(7),
    [sym__monary_operator] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(3),
    [sym_not] = ACTIONS(5),
    [sym_atom] = ACTIONS(7),
  },
};

static const uint16_t ts_small_parse_table[] = {
  [0] = 2,
    STATE(4), 1,
      sym__binary_operator,
    ACTIONS(9), 6,
      ts_builtin_sym_end,
      anon_sym_RPAREN,
      sym_and,
      sym_iff,
      sym_eq,
      sym_or,
  [12] = 2,
    STATE(4), 1,
      sym__binary_operator,
    ACTIONS(11), 6,
      ts_builtin_sym_end,
      anon_sym_RPAREN,
      sym_and,
      sym_iff,
      sym_eq,
      sym_or,
  [24] = 1,
    ACTIONS(13), 6,
      ts_builtin_sym_end,
      anon_sym_RPAREN,
      sym_and,
      sym_iff,
      sym_eq,
      sym_or,
  [33] = 3,
    ACTIONS(15), 1,
      ts_builtin_sym_end,
    STATE(4), 1,
      sym__binary_operator,
    ACTIONS(17), 4,
      sym_and,
      sym_iff,
      sym_eq,
      sym_or,
  [46] = 1,
    ACTIONS(19), 6,
      ts_builtin_sym_end,
      anon_sym_RPAREN,
      sym_and,
      sym_iff,
      sym_eq,
      sym_or,
  [55] = 1,
    ACTIONS(21), 6,
      ts_builtin_sym_end,
      anon_sym_RPAREN,
      sym_and,
      sym_iff,
      sym_eq,
      sym_or,
  [64] = 3,
    ACTIONS(23), 1,
      anon_sym_RPAREN,
    STATE(4), 1,
      sym__binary_operator,
    ACTIONS(17), 4,
      sym_and,
      sym_iff,
      sym_eq,
      sym_or,
  [77] = 1,
    ACTIONS(25), 6,
      ts_builtin_sym_end,
      anon_sym_RPAREN,
      sym_and,
      sym_iff,
      sym_eq,
      sym_or,
};

static const uint32_t ts_small_parse_table_map[] = {
  [SMALL_STATE(5)] = 0,
  [SMALL_STATE(6)] = 12,
  [SMALL_STATE(7)] = 24,
  [SMALL_STATE(8)] = 33,
  [SMALL_STATE(9)] = 46,
  [SMALL_STATE(10)] = 55,
  [SMALL_STATE(11)] = 64,
  [SMALL_STATE(12)] = 77,
};

static const TSParseActionEntry ts_parse_actions[] = {
  [0] = {.entry = {.count = 0, .reusable = false}},
  [1] = {.entry = {.count = 1, .reusable = false}}, RECOVER(),
  [3] = {.entry = {.count = 1, .reusable = true}}, SHIFT(2),
  [5] = {.entry = {.count = 1, .reusable = true}}, SHIFT(3),
  [7] = {.entry = {.count = 1, .reusable = true}}, SHIFT(7),
  [9] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym__monary_expression, 2, .production_id = 3),
  [11] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym__binary_expression, 3, .production_id = 4),
  [13] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_formula, 1),
  [15] = {.entry = {.count = 1, .reusable = true}},  ACCEPT_INPUT(),
  [17] = {.entry = {.count = 1, .reusable = true}}, SHIFT(4),
  [19] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_formula, 1, .production_id = 1),
  [21] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_formula, 1, .production_id = 2),
  [23] = {.entry = {.count = 1, .reusable = true}}, SHIFT(12),
  [25] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym__par_expression, 3),
};

#ifdef __cplusplus
extern "C" {
#endif
#ifdef _WIN32
#define extern __declspec(dllexport)
#endif

extern const TSLanguage *tree_sitter_ep(void) {
  static const TSLanguage language = {
    .version = LANGUAGE_VERSION,
    .symbol_count = SYMBOL_COUNT,
    .alias_count = ALIAS_COUNT,
    .token_count = TOKEN_COUNT,
    .external_token_count = EXTERNAL_TOKEN_COUNT,
    .state_count = STATE_COUNT,
    .large_state_count = LARGE_STATE_COUNT,
    .production_id_count = PRODUCTION_ID_COUNT,
    .field_count = FIELD_COUNT,
    .max_alias_sequence_length = MAX_ALIAS_SEQUENCE_LENGTH,
    .parse_table = &ts_parse_table[0][0],
    .small_parse_table = ts_small_parse_table,
    .small_parse_table_map = ts_small_parse_table_map,
    .parse_actions = ts_parse_actions,
    .symbol_names = ts_symbol_names,
    .field_names = ts_field_names,
    .field_map_slices = ts_field_map_slices,
    .field_map_entries = ts_field_map_entries,
    .symbol_metadata = ts_symbol_metadata,
    .public_symbol_map = ts_symbol_map,
    .alias_map = ts_non_terminal_alias_map,
    .alias_sequences = &ts_alias_sequences[0][0],
    .lex_modes = ts_lex_modes,
    .lex_fn = ts_lex,
  };
  return &language;
}
#ifdef __cplusplus
}
#endif
