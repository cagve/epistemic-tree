module.exports = grammar({
	name: 'ep',

  rules: {
	formula: $ => choice(
			$.atom,
			$.negation_formula,
			$.si_formula,
			$.eq_formula,
			$.and_formula,
			$.or_formula,
			$.par_formula
		),
	par_formula: $=> seq('(',$.formula,')'),
	negation_formula: $=> prec(2,seq($.not, $.formula)),
	and_formula: $=> prec.left(1, seq($.formula,$.and,$.formula)),
	or_formula: $=> prec.left(1, seq($.formula,$.or,$.formula)),
	si_formula: $=> prec.left(1, seq($.formula,$.si,$.formula)),
	eq_formula: $=> prec.left(1, seq($.formula,$.eq,$.formula)),
	not: $=> "-",
	si: $=> "=>",
	eq: $=> "<=>",
	and: $=> "&&",
	or: $=> "||",
	atom: $ => /[p-z]/,
  }
});
