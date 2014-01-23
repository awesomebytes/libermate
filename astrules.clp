
;(deffunction python-call ($?z) )

(defglobal ?*ans* = None)

;
(deftemplate MAIN::ASTTemplate
    (slot id)
    (slot name)
    (slot value)
    (multislot children)
    ; properties
    (slot is_matrix (default FALSE))
    (slot is_scalar (default FALSE))
    (slot is_lhs (default FALSE))
    (slot is_rhs (default FALSE))
    )

(defrule MAIN::simple_scalar
    ?fact <- (ASTTemplate (name INT|FLOAT|NUMBER) (is_scalar FALSE) )
    =>
    (python-call rule_callback BaseRules-simple_scalar ?fact )
    ) 

(defrule MAIN::assign_lhs_rhs
    ?fact <- (ASTTemplate (name ASSIGN) )
    =>
    (python-call rule_callback BaseRules-assign_lhs_rhs ?fact )
    ) 

 
(defrule MAIN::map_rand_state
    ?node <- (ASTTemplate (id ?x) (name NAME) (value "rand") )
    ?child <- (ASTTemplate  (children ?x ?y $?) (name PAREN_ARGS))
    (ASTTemplate (id ?y) (value "'state'"))
    =>
    (python-call rule_callback BaseRules-map_rand_state ?node  )
    ) 

(defrule MAIN::int_as_float
    ?node <- (ASTTemplate (name INT) )
    =>
    (python-call rule_callback BaseRules-int_as_float ?node )
    ) 

(defrule MAIN::length_to_shape
    (ASTTemplate (id ?x) (name NAME) (value "'length'"))
    ?node <- (ASTTemplate (id ?b) (name PAREN_ARGS) (children ?x ?y))
    ?a <- (ASTTemplate (id ?y) )
    =>
    (python-call rule_callback BaseRules-length_to_shape ?node ?a )
    ) 

(defrule MAIN::scalar_mult_div_exp
    ?node <- (ASTTemplate (name STAR|EXP|DIV) (children ?x ?y) )
    ?a <- (ASTTemplate (id ?x) )
    ?b <- (ASTTemplate (id ?y) )
    =>
    (python-call rule_callback BaseRules-scalar_mult_div_exp ?node ?a ?b)
    ) 
