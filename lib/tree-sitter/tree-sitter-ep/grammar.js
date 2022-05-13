module.exports = grammar({
	name: 'ep',

  rules: {
	 // valid_expression: $ => choice(
		  // $.label,
		  // $.formula
	 //  ),
	// # COMO LA ESTRUCTURA D ELAS ETIQUETAS ES MUY SIMPLE EN PRINCIPIO NO HACE FALTA
	 //  label: $ => choice(
		  // seq( $.label,'.',$.agent,'.',$.digit)
	 //  ),
	formula: $ => choice(
			$.atom,
			$._monary_expression,
			$._binary_expression,
			$._par_expression,
			),

	  _monary_expression: $=> prec.left(1,seq(field('operator',$._monary_operator), field('term',$.formula))),
	  _binary_expression: $=> prec.left(1,seq(field('left_term',$.formula),field('operator',$._binary_operator), field('right_term',$.formula))),
	  _par_expression:    $=> seq('(', $.formula, ')'),

	  _monary_operator: $=> choice(
		$.not,
		$.know
	  ),
	  _binary_operator: $=> choice(
		  $.and,
		  $.or,
		  $.iff,
		  $.eq
	  ),

	  not: $ => "-",
	  and: $ => "&&",
	  iff: $ => "=>",
	  eq: $ => "<>",
	  or: $ => "||",
	  know: $=> seq("K",$.agent),
	  atom: $ => /[p-z]/,
	  agent: $=> choice(
		/[a-d]/,
		/[a-d]\d+/,
	  ),
	  digit: $=> choice(
		  /\d/,
		  /\d+/
	  )
  }
});


