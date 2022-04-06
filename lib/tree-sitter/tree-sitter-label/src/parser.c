#include <tree_sitter/parser.h>

#if defined(__GNUC__) || defined(__clang__)
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmissing-field-initializers"
#endif

#define LANGUAGE_VERSION 13
#define STATE_COUNT 10
#define LARGE_STATE_COUNT 2
#define SYMBOL_COUNT 9
#define ALIAS_COUNT 0
#define TOKEN_COUNT 6
#define EXTERNAL_TOKEN_COUNT 0
#define FIELD_COUNT 0
#define MAX_ALIAS_SEQUENCE_LENGTH 5
#define PRODUCTION_ID_COUNT 1

enum {
  anon_sym_DOT = 1,
  aux_sym_agent_token1 = 2,
  aux_sym_agent_token2 = 3,
  aux_sym_digit_token1 = 4,
  aux_sym_digit_token2 = 5,
  sym_label = 6,
  sym_agent = 7,
  sym_digit = 8,
};

static const char * const ts_symbol_names[] = {
  [ts_builtin_sym_end] = "end",
  [anon_sym_DOT] = ".",
  [aux_sym_agent_token1] = "agent_token1",
  [aux_sym_agent_token2] = "agent_token2",
  [aux_sym_digit_token1] = "digit_token1",
  [aux_sym_digit_token2] = "digit_token2",
  [sym_label] = "label",
  [sym_agent] = "agent",
  [sym_digit] = "digit",
};

static const TSSymbol ts_symbol_map[] = {
  [ts_builtin_sym_end] = ts_builtin_sym_end,
  [anon_sym_DOT] = anon_sym_DOT,
  [aux_sym_agent_token1] = aux_sym_agent_token1,
  [aux_sym_agent_token2] = aux_sym_agent_token2,
  [aux_sym_digit_token1] = aux_sym_digit_token1,
  [aux_sym_digit_token2] = aux_sym_digit_token2,
  [sym_label] = sym_label,
  [sym_agent] = sym_agent,
  [sym_digit] = sym_digit,
};

static const TSSymbolMetadata ts_symbol_metadata[] = {
  [ts_builtin_sym_end] = {
    .visible = false,
    .named = true,
  },
  [anon_sym_DOT] = {
    .visible = true,
    .named = false,
  },
  [aux_sym_agent_token1] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_agent_token2] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_digit_token1] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_digit_token2] = {
    .visible = false,
    .named = false,
  },
  [sym_label] = {
    .visible = true,
    .named = true,
  },
  [sym_agent] = {
    .visible = true,
    .named = true,
  },
  [sym_digit] = {
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
      if (eof) ADVANCE(1);
      if (lookahead == '.') ADVANCE(2);
      if (lookahead == '\t' ||
          lookahead == '\n' ||
          lookahead == '\r' ||
          lookahead == ' ') SKIP(0)
      if (('a' <= lookahead && lookahead <= 'd')) ADVANCE(3);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(5);
      END_STATE();
    case 1:
      ACCEPT_TOKEN(ts_builtin_sym_end);
      END_STATE();
    case 2:
      ACCEPT_TOKEN(anon_sym_DOT);
      END_STATE();
    case 3:
      ACCEPT_TOKEN(aux_sym_agent_token1);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(4);
      END_STATE();
    case 4:
      ACCEPT_TOKEN(aux_sym_agent_token2);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(4);
      END_STATE();
    case 5:
      ACCEPT_TOKEN(aux_sym_digit_token1);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(6);
      END_STATE();
    case 6:
      ACCEPT_TOKEN(aux_sym_digit_token2);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(6);
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
};

static const uint16_t ts_parse_table[LARGE_STATE_COUNT][SYMBOL_COUNT] = {
  [0] = {
    [ts_builtin_sym_end] = ACTIONS(1),
    [anon_sym_DOT] = ACTIONS(1),
    [aux_sym_agent_token1] = ACTIONS(1),
    [aux_sym_agent_token2] = ACTIONS(1),
    [aux_sym_digit_token1] = ACTIONS(1),
    [aux_sym_digit_token2] = ACTIONS(1),
  },
  [1] = {
    [sym_label] = STATE(5),
    [sym_digit] = STATE(6),
    [aux_sym_digit_token1] = ACTIONS(3),
    [aux_sym_digit_token2] = ACTIONS(3),
  },
};

static const uint16_t ts_small_parse_table[] = {
  [0] = 3,
    ACTIONS(5), 1,
      aux_sym_agent_token1,
    ACTIONS(7), 1,
      aux_sym_agent_token2,
    STATE(9), 1,
      sym_agent,
  [10] = 2,
    STATE(7), 1,
      sym_digit,
    ACTIONS(3), 2,
      aux_sym_digit_token1,
      aux_sym_digit_token2,
  [18] = 1,
    ACTIONS(9), 2,
      ts_builtin_sym_end,
      anon_sym_DOT,
  [23] = 2,
    ACTIONS(11), 1,
      ts_builtin_sym_end,
    ACTIONS(13), 1,
      anon_sym_DOT,
  [30] = 1,
    ACTIONS(15), 2,
      ts_builtin_sym_end,
      anon_sym_DOT,
  [35] = 1,
    ACTIONS(17), 2,
      ts_builtin_sym_end,
      anon_sym_DOT,
  [40] = 1,
    ACTIONS(19), 1,
      anon_sym_DOT,
  [44] = 1,
    ACTIONS(21), 1,
      anon_sym_DOT,
};

static const uint32_t ts_small_parse_table_map[] = {
  [SMALL_STATE(2)] = 0,
  [SMALL_STATE(3)] = 10,
  [SMALL_STATE(4)] = 18,
  [SMALL_STATE(5)] = 23,
  [SMALL_STATE(6)] = 30,
  [SMALL_STATE(7)] = 35,
  [SMALL_STATE(8)] = 40,
  [SMALL_STATE(9)] = 44,
};

static const TSParseActionEntry ts_parse_actions[] = {
  [0] = {.entry = {.count = 0, .reusable = false}},
  [1] = {.entry = {.count = 1, .reusable = false}}, RECOVER(),
  [3] = {.entry = {.count = 1, .reusable = false}}, SHIFT(4),
  [5] = {.entry = {.count = 1, .reusable = false}}, SHIFT(8),
  [7] = {.entry = {.count = 1, .reusable = true}}, SHIFT(8),
  [9] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_digit, 1),
  [11] = {.entry = {.count = 1, .reusable = true}},  ACCEPT_INPUT(),
  [13] = {.entry = {.count = 1, .reusable = true}}, SHIFT(2),
  [15] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_label, 1),
  [17] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_label, 5),
  [19] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_agent, 1),
  [21] = {.entry = {.count = 1, .reusable = true}}, SHIFT(3),
};

#ifdef __cplusplus
extern "C" {
#endif
#ifdef _WIN32
#define extern __declspec(dllexport)
#endif

extern const TSLanguage *tree_sitter_label(void) {
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
