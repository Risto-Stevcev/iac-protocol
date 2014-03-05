import iac.interfaces as interfaces

__package__ = 'iac'

class Command(object):
    '''Create command for execution after parsing'''
    scope = ''
    variable = ''
    object = ''
    function = ''
    parameters = []

    @staticmethod
    def clear():
        Command.scope = ''
        Command.variable = ''
        Command.object = ''
        Command.function = ''
        Command.parameters = []
    
    @staticmethod
    def parameters_to_string():
        return ','.join(["'%s'" % parameter if type(parameter) is str else str(parameter) \
                for parameter in Command.parameters])

    @staticmethod
    def to_string():
        if Command.variable and Command.object and Command.function:
            return "interfaces.%s.Interface.variables['%s'] = interfaces.%s.Interface.%s(interfaces.%s.Interface.variables['%s'],%s)" \
                    % (Command.scope, Command.variable, 
                            Command.scope, Command.function, 
                            Command.scope, Command.object, Command.parameters_to_string())

        elif not Command.variable and Command.object and Command.function:
            return "interfaces.%s.Interface.%s(interfaces.%s.Interface.variables['%s'],%s)" \
                    % (Command.scope, Command.function, 
                            Command.scope, Command.object, Command.parameters_to_string())

        elif Command.variable and not Command.object and Command.function:
            return "interfaces.%s.Interface.variables['%s'] = interfaces.%s.Interface.%s(%s)" \
                    % (Command.scope, Command.variable, 
                            Command.scope, Command.function, Command.parameters_to_string())

        elif Command.variable and Command.object and not Command.function:
            return "interfaces.%s.Interface.variables['%s'] = interfaces.%s.Interface(interfaces.%s.Interface.variables['%s'])" \
                    % (Command.scope, Command.variable, 
                            Command.scope, Command.scope, Command.object)

        elif Command.variable and not Command.object and not Command.function:
            return "interfaces.%s.Interface.variables['%s']" \
                    % (Command.scope, Command.variable)

        elif not Command.variable and not Command.object and Command.function:
            return "interfaces.%s.Interface.%s(%s)" \
                    % (Command.scope, Command.function, Command.parameters_to_string())



#-------
# Lexer
#-------
tokens = ('NAME', 'NUMBER', 'EQUALS', 'DOT', 'COMMA', 'LITERAL', 'LPAREN', 'RPAREN', 'ARROW')

t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_DOT     = r'\.'
t_COMMA   = r','
t_ARROW   = r'->'
t_LITERAL = r'(\'[^\']*\'|"[^"]*")'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

functions = { 'current_document' }

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()



#--------
# Parser
#--------
def p_scope(t):
    'scope : NAME ARROW statement' 
    Command.scope = t[1]

def p_statement_expr(t):
    'statement : expression'

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    Command.variable = t[1]

def p_expression_name(t):
    'expression : NAME'
    Command.variable = t[1]

def p_expression_function(t):
    '''
    expression : NAME LPAREN parameters RPAREN
               | NAME LPAREN RPAREN
               | NAME DOT NAME LPAREN parameters RPAREN
               | NAME DOT NAME LPAREN RPAREN
    '''
    if len(t) == 6 and t[2] is ".":
        Command.object = t[1]
        Command.function = t[3]
    elif len(t) == 7 and t[2] is ".":
        Command.object = t[1]
        Command.function = t[3]
        Command.parameters = t[5]
    elif len(t) == 4:
        Command.function = t[1]
    elif len(t) == 5:
        Command.function = t[1]
        Command.parameters = t[3]
    else:
        print("Function '%s' not defined" % t[1])

def p_parameters(t):
    '''
    parameters : parameters COMMA optional_argument
               | optional_argument
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    elif len(t) > 2:
        t[0] = t[1]
        t[0].append(t[3])

def p_optional_argument_literal(t):
    'optional_argument : LITERAL'
    t[0] = t[1][1:-1]

def p_optional_argument_number(t):
    'optional_argument : NUMBER'
    t[0] = t[1]

def p_error(t):
    if t:
        print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
yacc.yacc()

def parse(user_input):
    if user_input:
        Command.clear()
        yacc.parse(user_input)
        
        try:
            if Command.variable and Command.function:
                exec(Command.to_string())
                result = True
            else:
                result = eval(Command.to_string())
        except (TypeError, AttributeError):
            result = False
            pass

        return result
    else:
        return False
