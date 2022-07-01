module.exports = grammar({
	name: 'label',

  rules: {
          label: $ => choice(
			$.digit,
			seq( $.label,'.',$.agent,'.',$.digit)
	  ),
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


