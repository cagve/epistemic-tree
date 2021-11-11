#include <tree_sitter/parser.h>

#if defined(__GNUC__) || defined(__clang__)
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmissing-field-initializers"
#endif

#define LANGUAGE_VERSION 13
#define STATE_COUNT 17
#define LARGE_STATE_COUNT 8
#define SYMBOL_COUNT 16
#define ALIAS_COUNT 0
#define TOKEN_COUNT 9
#define EXTERNAL_TOKEN_COUNT 0
#define FIELD_COUNT 0
#define MAX_ALIAS_SEQUENCE_LENGTH 3
#define PRODUCTION_ID_COUNT 1

enum {
  anon_sym_LPAREN = 1,
  anon_sym_RPAREN = 2,
  sym_not = 3,
  sym_si = 4,
  sym_eq = 5,
  sym_and = 6,
  sym_or = 7,
  sym_atom = 8,
  sym_formula = 9,
  sym_par_formula = 10,
  sym_negation_formula = 11,
  sym_and_formula = 12,
  sym_or_formula = 13,
  sym_si_formula = 14,
  sym_eq_formula = 15,
};

static const char * const ts_symbol_names[] = {
  [ts_builtin_sym_end] = "end",
  [anon_sym_LPAREN] = "(",
  [anon_sym_RPAREN] = ")",
  [sym_not] = "not",
  [sym_si] = "si",
  [sym_eq] = "eq",
  [sym_and] = "and",
  [sym_or] = "or",
  [sym_atom] = "atom",
  [sym_formula] = "formula",
  [sym_par_formula] = "par_formula",
  [sym_negation_formula] = "negation_formula",
  [sym_and_formula] = "and_formula",
  [sym_or_formula] = "or_formula",
  [sym_si_formula] = "si_formula",
  [sym_eq_formula] = "eq_formula",
};

static const TSSymbol ts_symbol_map[] = {
  [ts_builtin_sym_end] = ts_builtin_sym_end,
  [anon_sym_LPAREN] = anon_sym_LPAREN,
  [anon_sym_RPAREN] = anon_sym_RPAREN,
  [sym_not] = sym_not,
  [sym_si] = sym_si,
  [sym_eq] = sym_eq,
  [sym_and] = sym_and,
  [sym_or] = sym_or,
  [sym_atom] = sym_atom,
  [sym_formula] = sym_formula,
  [sym_par_formula] = sym_par_formula,
  [sym_negation_formula] = sym_negation_formula,
  [sym_and_formula] = sym_and_formula,
  [sym_or_formula] = sym_or_formula,
  [sym_si_formula] = sym_si_formula,
  [sym_eq_formula] = sym_eq_formula,
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
  [sym_si] = {
    .visible = true,
    .named = true,
  },
  [sym_eq] = {
    .visible = true,
    .named = true,
  },
  [sym_and] = {
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
  [sym_par_formula] = {
    .visible = true,
    .named = true,
  },
  [sym_negation_formula] = {
    .visible = true,
    .named = true,
  },
  [sym_and_formula] = {
    .visible = true,
    .named = true,
  },
  [sym_or_formula] = {
    .visible = true,
    .named = true,
  },
  [sym_si_formula] = {
    .visible = true,
    .named = true,
  },
  [sym_eq_formula] = {
    .visible = true,
    .named = true,
  },
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
      if (eof) ADVANCE(6);
      if (lookahead == '&') ADVANCE(1);
      if (lookahead == '(') ADVANCE(7);
      if (lookahead == ')') ADVANCE(8);
      if (lookahead == '-') ADVANCE(9);
      if (lookahead == '<') ADVANCE(2);
      if (lookahead == '=') ADVANCE(3);
      if (lookahead == '|') ADVANCE(5);
      if (lookahead == '\t' ||
          lookahead == '\n' ||
          lookahead == '\r' ||
          lookahead == ' ') SKIP(0)
      if (('p' <= lookahead && lookahead <= 'z')) ADVANCE(14);
      END_STATE();
    case 1:
      if (lookahead == '&') ADVANCE(12);
      END_STATE();
    case 2:
      if (lookahead == '=') ADVANCE(4);
      END_STATE();
    case 3:
      if (lookahead == '>') ADVANCE(10);
      END_STATE();
    case 4:
      if (lookahead == '>') ADVANCE(11);
      END_STATE();
    case 5:
      if (lookahead == '|') ADVANCE(13);
      END_STATE();
    case 6:
      ACCEPT_TOKEN(ts_builtin_sym_end);
      END_STATE();
    case 7:
      ACCEPT_TOKEN(anon_sym_LPAREN);
      END_STATE();
    case 8:
      ACCEPT_TOKEN(anon_sym_RPAREN);
      END_STATE();
    case 9:
      ACCEPT_TOKEN(sym_not);
      END_STATE();
    case 10:
      ACCEPT_TOKEN(sym_si);
      END_STATE();
    case 11:
      ACCEPT_TOKEN(sym_eq);
      END_STATE();
    case 12:
      ACCEPT_TOKEN(sym_and);
      END_STATE();
    case 13:
      ACCEPT_TOKEN(sym_or);
      END_STATE();
    case 14:
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
  [13] = {.lex_state = 0},
  [14] = {.lex_state = 0},
  [15] = {.lex_state = 0},
  [16] = {.lex_state = 0},
};

static const uint16_t ts_parse_table[LARGE_STATE_COUNT][SYMBOL_COUNT] = {
  [0] = {
    [ts_builtin_sym_end] = ACTIONS(1),
    [anon_sym_LPAREN] = ACTIONS(1),
    [anon_sym_RPAREN] = ACTIONS(1),
    [sym_not] = ACTIONS(1),
    [sym_si] = ACTIONS(1),
    [sym_eq] = ACTIONS(1),
    [sym_and] = ACTIONS(1),
    [sym_or] = ACTIONS(1),
    [sym_atom] = ACTIONS(1),
  },
  [1] = {
    [sym_formula] = STATE(15),
    [sym_par_formula] = STATE(8),
    [sym_negation_formula] = STATE(8),
    [sym_and_formula] = STATE(8),
    [sym_or_formula] = STATE(8),
    [sym_si_formula] = STATE(8),
    [sym_eq_formula] = STATE(8),
    [anon_sym_LPAREN] = ACTIONS(3),
    [sym_not] = ACTIONS(5),
    [sym_atom] = ACTIONS(7),
  },
  [2] = {
    [sym_formula] = STATE(16),
    [sym_par_formula] = STATE(8),
    [sym_negation_formula] = STATE(8),
    [sym_and_formula] = STATE(8),
    [sym_or_formula] = STATE(8),
    [sym_si_formula] = STATE(8),
    [sym_eq_formula] = STATE(8),
    [anon_sym_LPAREN] = ACTIONS(3),
    [sym_not] = ACTIONS(5),
    [sym_atom] = ACTIONS(7),
  },
  [3] = {
    [sym_formula] = STATE(9),
    [sym_par_formula] = STATE(8),
    [sym_negation_formula] = STATE(8),
    [sym_and_formula] = STATE(8),
    [sym_or_formula] = STATE(8),
    [sym_si_formula] = STATE(8),
    [sym_eq_formula] = STATE(8),
    [anon_sym_LPAREN] = ACTIONS(3),
    [sym_not] = ACTIONS(5),
    [sym_atom] = ACTIONS(7),
  },
  [4] = {
    [sym_formula] = STATE(11),
    [sym_par_formula] = STATE(8),
    [sym_negation_formula] = STATE(8),
    [sym_and_formula] = STATE(8),
    [sym_or_formula] = STATE(8),
    [sym_si_formula] = STATE(8),
    [sym_eq_formula] = STATE(8),
    [anon_sym_LPAREN] = ACTIONS(3),
    [sym_not] = ACTIONS(5),
    [sym_atom] = ACTIONS(7),
  },
  [5] = {
    [sym_formula] = STATE(12),
    [sym_par_formula] = STATE(8),
    [sym_negation_formula] = STATE(8),
    [sym_and_formula] = STATE(8),
    [sym_or_formula] = STATE(8),
    [sym_si_formula] = STATE(8),
    [sym_eq_formula] = STATE(8),
    [anon_sym_LPAREN] = ACTIONS(3),
    [sym_not] = ACTIONS(5),
    [sym_atom] = ACTIONS(7),
  },
  [6] = {
    [sym_formula] = STATE(13),
    [sym_par_formula] = STATE(8),
    [sym_negation_formula] = STATE(8),
    [sym_and_formula] = STATE(8),
    [sym_or_formula] = STATE(8),
    [sym_si_formula] = STATE(8),
    [sym_eq_formula] = STATE(8),
    [anon_sym_LPAREN] = ACTIONS(3),
    [sym_not] = ACTIONS(5),
    [sym_atom] = ACTIONS(7),
  },
  [7] = {
    [sym_formula] = STATE(14),
    [sym_par_formula] = STATE(8),
    [sym_negation_formula] = STATE(8),
    [sym_and_formula] = STATE(8),
    [sym_or_formula] = STATE(8),
    [sym_si_formula] = STATE(8),
    [sym_eq_formula] = STATE(8),
    [anon_sym_LPAREN] = ACTIONS(3),
    [sym_not] = ACTIONS(5),
    [sym_atom] = ACTIONS(7),
  },
};

static const uint16_t ts_small_parse_table[] = {
  [0] = 1,
    ACTIONS(9), 6,
      ts_builtin_sym_end,
      anon_sym_RPAREN,
      sym_si,
      sym_eq,
      sym_and,
      sym_or,
  [9] = 1,
    ACTIONS(11), 6,
      ts_builtin_sym_end,
      anon_sym_RPAREN,
      sym_si,
      sym_eq,
      sym_and,
      sym_or,
  [18] = 1,
    ACTIONS(13), 6,
      ts_builtin_sym_end,
      anon_sym_RPAREN,
      sym_si,
      sym_eq,
      sym_and,
      sym_or,
  [27] = 1,
    ACTIONS(15), 6,
      ts_builtin_sym_end,
      anon_sym_RPAREN,
      sym_si,
      sym_eq,
      sym_and,
      sym_or,
  [36] = 1,
    ACTIONS(17), 6,
      ts_builtin_sym_end,
      anon_sym_RPAREN,
      sym_si,
      sym_eq,
      sym_and,
      sym_or,
  [45] = 1,
    ACTIONS(19), 6,
      ts_builtin_sym_end,
      anon_sym_RPAREN,
      sym_si,
      sym_eq,
      sym_and,
      sym_or,
  [54] = 1,
    ACTIONS(21), 6,
      ts_builtin_sym_end,
      anon_sym_RPAREN,
      sym_si,
      sym_eq,
      sym_and,
      sym_or,
  [63] = 5,
    ACTIONS(23), 1,
      ts_builtin_sym_end,
    ACTIONS(25), 1,
      sym_si,
    ACTIONS(27), 1,
      sym_eq,
    ACTIONS(29), 1,
      sym_and,
    ACTIONS(31), 1,
      sym_or,
  [79] = 5,
    ACTIONS(25), 1,
      sym_si,
    ACTIONS(27), 1,
      sym_eq,
    ACTIONS(29), 1,
      sym_and,
    ACTIONS(31), 1,
      sym_or,
    ACTIONS(33), 1,
      anon_sym_RPAREN,
};

static const uint32_t ts_small_parse_table_map[] = {
  [SMALL_STATE(8)] = 0,
  [SMALL_STATE(9)] = 9,
  [SMALL_STATE(10)] = 18,
  [SMALL_STATE(11)] = 27,
  [SMALL_STATE(12)] = 36,
  [SMALL_STATE(13)] = 45,
  [SMALL_STATE(14)] = 54,
  [SMALL_STATE(15)] = 63,
  [SMALL_STATE(16)] = 79,
};

static const TSParseActionEntry ts_parse_actions[] = {
  [0] = {.entry = {.count = 0, .reusable = false}},
  [1] = {.entry = {.count = 1, .reusable = false}}, RECOVER(),
  [3] = {.entry = {.count = 1, .reusable = true}}, SHIFT(2),
  [5] = {.entry = {.count = 1, .reusable = true}}, SHIFT(3),
  [7] = {.entry = {.count = 1, .reusable = true}}, SHIFT(8),
  [9] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_formula, 1),
  [11] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_negation_formula, 2),
  [13] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_par_formula, 3),
  [15] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_si_formula, 3),
  [17] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_eq_formula, 3),
  [19] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_and_formula, 3),
  [21] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_or_formula, 3),
  [23] = {.entry = {.count = 1, .reusable = true}},  ACCEPT_INPUT(),
  [25] = {.entry = {.count = 1, .reusable = true}}, SHIFT(4),
  [27] = {.entry = {.count = 1, .reusable = true}}, SHIFT(5),
  [29] = {.entry = {.count = 1, .reusable = true}}, SHIFT(6),
  [31] = {.entry = {.count = 1, .reusable = true}}, SHIFT(7),
  [33] = {.entry = {.count = 1, .reusable = true}}, SHIFT(10),
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
