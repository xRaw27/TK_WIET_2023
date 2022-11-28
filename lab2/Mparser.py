import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSE'),
    ('right', 'MULASSIGN', 'DIVASSIGN', 'SUBASSIGN', 'ADDASSIGN'),
    ('nonassoc', 'LT', 'GT', 'GE', 'LE', 'EQ', 'NE'),
    ('left', '+', '-'),
    ('left', 'DOTADD', 'DOTSUB'),
    ('left', '*', '/'),
    ('left', 'DOTMUL', 'DOTDIV'),
    ('right', 'UMINUS'),
    ('left', "'"),
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_instructions_opt_1(p):
    """instructions_opt : instructions """


def p_instructions_opt_2(p):
    """instructions_opt : """


def p_instructions_1(p):
    """instructions : instructions instruction """


def p_instructions_2(p):
    """instructions : instruction """


def p_instruction(p):
    """instruction : sys_instruction ';'
                   | assignment ';'
                   | '{' instructions '}' """


def p_sys_instruction_return(p):
    """sys_instruction : RETURN expression """


def p_sys_instruction_break(p):
    """sys_instruction : BREAK """


def p_sys_instruction_continue(p):
    """sys_instruction : CONTINUE"""


def p_sys_instruction_print(p):
    """sys_instruction : PRINT print_values """


def p_instruction_if(p):
    """instruction : IF '(' condition ')' instruction %prec IFX """


def p_instruction_if_else(p):
    """instruction : IF '(' condition ')' instruction ELSE instruction """


def p_instruction_for(p):
    """instruction : FOR var '=' expression ':' expression instruction """


def p_instruction_while(p):
    """instruction : WHILE '(' condition ')' instruction """


def p_assignment(p):
    """assignment : var assignment_operator expression
                  | matrix_element assignment_operator expression
                  | vector_element assignment_operator expression """


def p_assignment_operator(p):
    """assignment_operator : '='
                           | ADDASSIGN
                           | SUBASSIGN
                           | MULASSIGN
                           | DIVASSIGN """


def p_matrix(p):
    """matrix : '[' vectors ']' """


def p_vector(p):
    """vector : '[' variables ']' """


def p_vectors(p):
    """vectors : vectors ',' vector
                | vector """


def p_matrix_function(p):
    """matrix_function : function_name '(' INTNUM ')' """


def p_function_name(p):
    """function_name : EYE
                     | ONES
                     | ZEROS """


def p_var(p):
    """var : ID """


def p_number(p):
    """number : INTNUM
              | FLOATNUM """


def p_string(p):
    """string : STRING """


def p_variable(p):
    """variable : number
                 | var
                 | element """


def p_vector_element(p):
    """ vector_element : ID "[" INTNUM "]" """


def p_matrix_element(p):
    """ matrix_element : ID "[" INTNUM "," INTNUM "]" """


def p_element(p):
    """ element : vector_element
               | matrix_element"""


def p_variables(p):
    """variables : variables ',' variable
                 | variable """


def p_expression(p):
    """expression : number
                  | var
                  | matrix
                  | matrix_function
                  | uminus
                  | transposition
                  | matrix_element
                  | vector_element """


def p_bin_expression(p):
    """expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression DOTADD expression
                  | expression DOTSUB expression
                  | expression DOTMUL expression
                  | expression DOTDIV expression """


def p_condition(p):
    """condition : expression EQ expression
                 | expression NE expression
                 | expression LE expression
                 | expression GE expression
                 | expression LT expression
                 | expression GT expression """


def p_uminus(p):
    """uminus : '-' expression %prec UMINUS """


def p_transposition(p):
    """transposition : expression "'" """


def p_print_values(p):
    """print_values : print_values ',' string
                    | print_values ',' expression
                    | string
                    | expression """


parser = yacc.yacc(debug=True)
