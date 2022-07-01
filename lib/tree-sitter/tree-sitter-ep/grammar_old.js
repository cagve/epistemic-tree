module.exports = grammar({
	name: 'lp',

  rules: {
	  // Como solo se evalua una fórmula no hace falta poner esto. Lo sería si quisieramos crear una gramática 
	source_file: $ => repeat($.formula), 
	formula: $ => choice(
		  $.atom,
		  $.binary_expression,
		  $.unary_expression,
		  seq(
		    $.open_par,
		    $.formula,
		    $.close_par,)
		  ),
    	binary_expression: $ => prec.left(1,seq($.formula,$.binary_operator,$.formula)),
    	unary_expression: $ => choice(
		seq($.unary_operator,$.open_par,$.formula,$.close_par),
		seq($.unary_operator,$.atom)),
	binary_operator:$ => choice(
		'\\land', 
		'\\lor',
		'\\to',
		'\\leftrightarrow'),
	unary_operator:$ => '\\lnot', 
	atom: $ => /[p-z]/,
	variable: $ =>/[x\d\]
	open_par:$ => '(', 
	close_par:$ => ')', 
  }
});
