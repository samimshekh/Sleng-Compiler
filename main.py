class Integer:
    def __init__(self, value):
        self.value = value

    # Unary operators (highest precedence)
    def __pos__(self):
        return Integer(+self.value)

    def __neg__(self):
        return Integer(-self.value)

    def __invert__(self):
        return Integer(~self.value)

    # Exponentiation (right-to-left)
    def __pow__(self, other):
        return Integer(self.value ** other.value)

    # Multiplication, Division, Floor Division, Modulo
    def __mul__(self, other):
        return Integer(self.value * other.value)

    def __truediv__(self, other):
        return Integer(self.value // other.value) if other.value != 0 else None

    def __floordiv__(self, other):
        return Integer(self.value // other.value) if other.value != 0 else None

    def __mod__(self, other):
        return Integer(self.value % other.value) if other.value != 0 else None

    # Addition, Subtraction
    def __add__(self, other):
        return Integer(self.value + other.value)

    def __sub__(self, other):
        return Integer(self.value - other.value)

    # Bitwise shift left and right
    def __lshift__(self, other):
        return Integer(self.value << other.value)

    def __rshift__(self, other):
        return Integer(self.value >> other.value)

    # Bitwise AND, OR, XOR
    def __and__(self, other):
        return Integer(self.value & other.value)

    def __or__(self, other):
        return Integer(self.value | other.value)

    def __xor__(self, other):
        return Integer(self.value ^ other.value)

    # Comparisons (equal, not equal, greater than, etc.)
    def __eq__(self, other):
        return true() if self.value == other.value else false()

    def __ne__(self, other):
        return true() if self.value != other.value else false()

    def __lt__(self, other):
        return true() if self.value < other.value else false()

    def __le__(self, other):
        return true() if self.value <= other.value else false()

    def __gt__(self, other):
        return true() if self.value > other.value else false()

    def __ge__(self, other):
        return true() if self.value >= other.value else false()

    # Logical NOT
    def __not__(self):
        return true() if self.value == 0 else false()

    # Logical AND
    def __and__(self, other):
        return true() if self.value and other.value else false()

    # Logical OR
    def __or__(self, other):
        return true() if self.value or other.value else false()

    # Representation
    def __repr__(self):
        return f"Integer({self.value})"

class true:
    def __init__(self):
        self.value = 1

    def __repr__(self):
        return f"true({self.value})"

class false:
    def __init__(self):
        self.value = 0

    def __repr__(self):
        return f"false({self.value})"

# AST Nodes
class Num:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"{self.value[1]}"

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def __repr__(self):
        return f"({self.left} {self.op[1]} {self.right})"
    
class UnaryOp:
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr
    
    def __repr__(self):
        return f"{self.op[1]}{self.expr}"

class Reg:
    def __init__(self, reg):
        self.reg = reg

    def __repr__(self):
        return f"Reg({self.reg})"

class Const:
    def __init__(self, name, value):
        self.name = name 
        self.value = value

    def __repr__(self):
        return f"const {self.name} = {self.value}"

class Integer:
    def __init__(self, value):
        self.value = value

    # Unary operators (highest precedence)
    def __pos__(self):
        return Integer(+self.value)

    def __neg__(self):
        return Integer(-self.value)

    def __invert__(self):
        return Integer(~self.value)

    # Exponentiation (right-to-left)
    def __pow__(self, other):
        return Integer(self.value ** other.value)

    # Multiplication, Division, Floor Division, Modulo
    def __mul__(self, other):
        return Integer(self.value * other.value)

    def __truediv__(self, other):
        return Integer(self.value // other.value) if other.value != 0 else None

    def __floordiv__(self, other):
        return Integer(self.value // other.value) if other.value != 0 else None

    def __mod__(self, other):
        return Integer(self.value % other.value) if other.value != 0 else None

    # Addition, Subtraction
    def __add__(self, other):
        return Integer(self.value + other.value)

    def __sub__(self, other):
        return Integer(self.value - other.value)

    # Bitwise shift left and right
    def __lshift__(self, other):
        return Integer(self.value << other.value)

    def __rshift__(self, other):
        return Integer(self.value >> other.value)

    # Bitwise AND, OR, XOR
    def __and__(self, other):
        return Integer(self.value & other.value)

    def __or__(self, other):
        return Integer(self.value | other.value)

    def __xor__(self, other):
        return Integer(self.value ^ other.value)

    # Comparisons (equal, not equal, greater than, etc.)
    def __eq__(self, other : Integer):
        return true() if self.value == other else false()

    def __ne__(self, other):
        return true() if self.value != other.value else false()

    def __lt__(self, other):
        return true() if self.value < other.value else false()

    def __le__(self, other):
        return true() if self.value <= other.value else false()

    def __gt__(self, other):
        return true() if self.value > other.value else false()

    def __ge__(self, other):
        return true() if self.value >= other.value else false()

    # Logical NOT
    def __not__(self):
        return true() if self.value == 0 else false()

    # Logical AND
    def __and__(self, other):
        return true() if self.value and other.value else false()

    # Logical OR
    def __or__(self, other):
        return true() if self.value or other.value else false()

    # Representation
    def __repr__(self):
        return f"Integer({self.value})"

class true:
    def __init__(self):
        self.value = 1

    def __repr__(self):
        return f"true({self.value})"

class false:
    def __init__(self):
        self.value = 0

    def __repr__(self):
        return f"false({self.value})"

# AST Nodes
class Num:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"{self.value[1]}"

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def __repr__(self):
        return f"({self.left} {self.op[1]} {self.right})"
    
class UnaryOp:
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr
    
    def __repr__(self):
        return f"{self.op[1]}{self.expr}"

class Reg:
    def __init__(self, reg):
        self.reg = reg

    def __repr__(self):
        return f"{self.reg}"

class Const:
    def __init__(self, name, value):
        self.name = name 
        self.value = value

    def __repr__(self):
        return f"const {self.name} = {self.value}"
    
# 1 (Highest) - Parentheses (grouping)
T_LPAREN = "LPAREN"  # (
T_RPAREN = "RPAREN"  # )

# 2 - Exponentiation (right-to-left)
T_POW = "POW"  # **

# 3 - Unary plus, minus, bitwise NOT
T_PLUS_UNARY = "PLUS_UNARY"  # +x
T_MINUS_UNARY = "MINUS_UNARY"  # -x
T_BIT_NOT = "BIT_NOT"  # ~x

# 4 - Multiplication, division, floor division, modulo
T_MUL = "MUL"  # *
T_DIV = "DIV"  # /
T_FLOORDIV = "FLOORDIV"  # //
T_MOD = "MOD"  # %

# 5 - Addition, subtraction
T_PLUS = "PLUS"  # +
T_MINUS = "MINUS"  # -

# 6 - Bitwise shift left, right
T_SHL = "SHL"  # <<
T_SHR = "SHR"  # >>

# 7 - Bitwise AND
T_BIT_AND = "BIT_AND"  # &

# 8 - Bitwise XOR
T_BIT_XOR = "BIT_XOR"  # ^

# 9 - Bitwise OR
T_BIT_OR = "BIT_OR"  # |

# 10 - Comparisons (all have the same precedence)
T_EQ = "EQ"  # ==
T_NEQ = "NEQ"  # !=
T_GT = "GT"  # >
T_LT = "LT"  # <
T_GTE = "GTE"  # >=
T_LTE = "LTE"  # <=

# 11 - Logical NOT
T_LOG_NOT = "LOG_NOT"  # not

# 12 - Logical AND
T_LOG_AND = "LOG_AND"  # and

# 13 (Lowest) - Logical OR
T_LOG_OR = "LOG_OR"  # or

T_KEYWORDS = "KEYWORDS"
T_REGISTERS = "REGISTERS"
T_INT = "INT"
T_ID = "ID"
T_EOF = "EOF"
T_INS_END = "INS_END"
T_ASSIGN = "ASSIGN"
KEYWORDS = ["not", "or", "and", "const"]
REGISTERS = []

X86_REAL_MODE_REGISTERS = [
    # General-purpose registers (16-bit)
    "AX", "BX", "CX", "DX",    

    # General-purpose registers (8-bit - High & Low)
    "AH", "AL", "BH", "BL", "CH", "CL", "DH", "DL",

    # Index and Pointer registers (16-bit)
    "SI", "DI", "BP", "SP",

    # Segment registers (16-bit)
    "CS", "DS", "ES", "FS", "GS", "SS",

    # Instruction Pointer (16-bit)
    "IP",
]

#ins
T_MOV = "MOV" 
T_INTERRUPTED = "INTERRUPTED"


# Custom Error Class
class InterpreterError(Exception):
    def __init__(self, message, line, start, end):
        self.message = message
        self.line = line
        self.start = start
        self.end = end 

    def __str__(self):
        return f"Error at Line {self.line}, Column {self.start, self.end}: {self.message}"


class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.tokens = []
        self.column = 1
        self.tokenize()

    def advance(self, length=1):
        for _ in range(length):
            if self.pos < len(self.text) and self.text[self.pos] == "\n":
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.pos += 1


    def peek(self, offset=0):
        if self.pos + offset < len(self.text):
            return self.text[self.pos + offset]
        return None
    
    def tokenize(self):
        while self.pos < len(self.text):
            char = self.text[self.pos]

            # Skip whitespace
            if char.isspace():
                self.advance()
                continue

            # Integer Identifiers and Keywords
            elif (self.peek().isalnum() or self.peek() == "_"):
                start_col = self.column
                word = ""
                while self.peek() and (self.peek().isalnum() or self.peek() == "_"):
                    word += self.peek()
                    self.advance()
                if word in KEYWORDS:
                    self.tokens.append((T_KEYWORDS, word, self.line, start_col, self.column))
                elif word.upper() in X86_REAL_MODE_REGISTERS:
                    self.tokens.append((T_REGISTERS, word.upper(), self.line, start_col, self.column))
                elif word.isdigit():
                    self.tokens.append((T_INT, Integer(int(word)), self.line, start_col, self.column))
                else:
                    if word[0].isdigit(): 
                        raise InterpreterError(f"invalid decimal literal '{word}'", self.line, start_col, self.column)
                    self.tokens.append((T_ID, word, self.line, start_col, self.column))
                continue 
            
            # Operators
            elif char == ";":
                self.tokens.append((T_INS_END, ";", self.line, self.column, self.column + 1))
            elif char == "+":
                self.tokens.append((T_PLUS, "+", self.line, self.column, self.column + 1))
            elif char == "-":
                self.tokens.append((T_MINUS, "-", self.line, self.column, self.column + 1))
            elif char == "~":
                self.tokens.append((T_BIT_NOT, "~", self.line, self.column, self.column + 1))
            elif char == "^":
                self.tokens.append((T_BIT_XOR, "^", self.line, self.column, self.column + 1))
            elif char == "&":
                self.tokens.append((T_BIT_AND, "&", self.line, self.column, self.column + 1))
            elif char == "|":
                self.tokens.append((T_BIT_OR, "|", self.line, self.column, self.column + 1))
            elif char == "*":
                if self.peek(1) == "*":
                    self.tokens.append((T_POW, "**", self.line, self.column, self.column + 2))
                    self.advance(2)
                    continue
                else:
                    self.tokens.append((T_MUL, "*", self.line, self.column, self.column + 1))
            elif char == "/":
                if self.peek(1) == "/":
                    self.tokens.append((T_FLOORDIV, "//", self.line, self.column, self.column + 2))
                    self.advance(2)
                    continue
                else:
                    self.tokens.append((T_DIV, "/", self.line, self.column, self.column + 1))
            elif char == "%":
                self.tokens.append((T_MOD, "%", self.line, self.column, self.column + 1))
            elif char == ">":
                if self.peek(1) == "=":
                    self.tokens.append((T_GTE, ">=", self.line, self.column, self.column + 2))
                    self.advance(2)
                    continue
                elif self.peek(1) == ">":
                    self.tokens.append((T_SHR, ">>", self.line, self.column, self.column + 2))
                    self.advance(2)
                    continue
                else:
                    self.tokens.append((T_GT, ">", self.line, self.column, self.column + 1))
            elif char == "<":
                if self.peek(1) == "=":
                    self.tokens.append((T_LTE, "<=", self.line, self.column, self.column + 2))
                    self.advance(2)
                    continue
                elif self.peek(1) == "<":
                    self.tokens.append((T_SHL, "<<", self.line, self.column, self.column + 2))
                    self.advance(2)
                    continue
                else:
                    self.tokens.append((T_LT, "<", self.line, self.column, self.column + 1))
            elif char == "=":
                if self.peek(1) == "=":
                    self.tokens.append((T_EQ, "==", self.line, self.column, self.column + 2))
                    self.advance(2)
                    continue
                else:
                    self.tokens.append((T_ASSIGN, "=", self.line, self.column, self.column + 1))
            elif char == "!":
                if self.peek(1) == "=":
                    self.tokens.append((T_NEQ, "!=", self.line, self.column, self.column + 2))
                    self.advance(2)
                    continue
            elif char == "(":
                self.tokens.append((T_LPAREN, "(", self.line, self.column, self.column + 1))
            elif char == ")":
                self.tokens.append((T_RPAREN, ")", self.line, self.column, self.column + 1))
            else:
                raise InterpreterError(f"Unknown character '{char}'", self.line, self.column, self.column + 1)

            self.advance()

        self.tokens.append((T_EOF, None, self.line, self.column, self.column))

    def get_tokens(self):
        return self.tokens

# Parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.ins = []
    
    def addins(self, ins):
        self.ins.append(ins)

    def error(self, message):
        token = self.tokens[self.pos]
        raise InterpreterError(message, token[2], token[3], token[4])

    def eat(self, token_type):
        if self.tokens[self.pos][0] == token_type:
            self.pos += 1
        else:
            self.error(f"Expected {token_type}, found {self.tokens[self.pos][0]}")
    
    def eata(self, token_type):
        if self.tokens[self.pos][0] in token_type:
            self.pos += 1
        else:
            self.error(f"Expected {token_type}, found {self.tokens[self.pos][0]}")
    
    def factor(self):
        token = self.tokens[self.pos]
        if token[0] == T_INT:
            self.eat(T_INT)
            return Num(token)
        elif token[0] == T_REGISTERS:
            self.eat(T_REGISTERS)
            return Reg(token)
        elif (token[0] == T_KEYWORDS) and (token[1] == "not"):
            self.eat(T_KEYWORDS)
            token = [T_LOG_NOT, token[1], token[2], token[3], token[4]]
            return UnaryOp(token, self.factor())
        elif token[0] == T_PLUS:
            self.eat(T_PLUS)
            return UnaryOp(token, self.factor())
        elif token[0] == T_LPAREN:
            self.eat(T_LPAREN)
            node = self.expr()
            if self.tokens[self.pos][0] != T_RPAREN:
                self.error("Mismatched parentheses: Expected ')'")
            self.eat(T_RPAREN)
            return node
        else: 
            self.error(f"bad operand type for unary {token[1]}")
    
    def exponent(self):
        node = self.factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] == T_POW:
            token = self.tokens[self.pos]
            self.eat(T_POW)
            node = BinOp(node, token, self.exponent())
        return node
    
    def bitnot_plus_minus(self):
        if self.tokens[self.pos][0] in (T_BIT_NOT, T_PLUS, T_MINUS):
            op = self.tokens[self.pos]
            self.eat(self.tokens[self.pos][0])
            return UnaryOp(op, self.bitnot_plus_minus())
        else: return self.exponent()
    
    def term(self):
        node = self.bitnot_plus_minus()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in (T_MUL, T_DIV, T_FLOORDIV, T_MOD):
            token = self.tokens[self.pos]
            self.eat(token[0])
            node = BinOp(node, token, self.bitnot_plus_minus())
        return node
    
    def Addition_subtraction(self):
        node = self.term()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in (T_PLUS, T_MINUS):
            token = self.tokens[self.pos]
            self.eat(token[0])
            node = BinOp(node, token, self.term())
        return node
    
    def Bitwise_shift_left_right(self):
        node = self.Addition_subtraction()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in (T_SHL, T_SHR):
            token = self.tokens[self.pos]
            self.eat(token[0])
            node = BinOp(node, token, self.Addition_subtraction())
        return node

    def Bitwise_and(self):
        node = self.Bitwise_shift_left_right()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] == T_BIT_AND:
            token = self.tokens[self.pos]
            self.eat(token[0])
            node = BinOp(node, token, self.Bitwise_shift_left_right())
        return node
        
    def Bitwise_xor(self):
        node = self.Bitwise_and()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] == T_BIT_XOR:
            token = self.tokens[self.pos]
            self.eat(token[0])
            node = BinOp(node, token, self.Bitwise_and())
        return node
         
    
    def Bitwise_or(self):
        node = self.Bitwise_xor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] == T_BIT_OR:
            token = self.tokens[self.pos]
            self.eat(token[0])
            node = BinOp(node, token, self.Bitwise_xor())
        return node

    def comparisons(self):
        node = self.Bitwise_or()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in (T_EQ, T_NEQ, T_GT, T_LT, T_GTE, T_LTE):
            token = self.tokens[self.pos]
            self.eat(token[0])
            node = BinOp(node, token, self.Bitwise_or())
        return node
         
    def Logica_and(self):
        node = self.comparisons()
        while self.pos < len(self.tokens) and ((self.tokens[self.pos][0] == T_KEYWORDS) and (self.tokens[self.pos][1] == "and")):
            token = [T_LOG_AND, self.tokens[self.pos][1], self.tokens[self.pos][2], self.tokens[self.pos][3], self.tokens[self.pos][4]]
            self.eat(T_KEYWORDS)
            node = BinOp(node, token, self.comparisons())
        return node

    def expr(self):
        node = self.Logica_and()
        while self.pos < len(self.tokens) and ((self.tokens[self.pos][0] == T_KEYWORDS) and (self.tokens[self.pos][1] == "or")):
            token = [T_LOG_OR, self.tokens[self.pos][1], self.tokens[self.pos][2], self.tokens[self.pos][3], self.tokens[self.pos][4]]
            self.eat(T_KEYWORDS)
            node = BinOp(node, token, self.Logica_and())
        return node
    
    def insSkiper(self):
        self.eat(T_INS_END)
        token = self.tokens[self.pos]
        while token[0] != T_EOF:
            if token[0] == T_INS_END: self.eat(T_INS_END)
            else: break
    
    def constVar(self):
        self.eat(T_KEYWORDS)
        name = self.tokens[self.pos]
        self.eat(T_ID)
        self.eat(T_ASSIGN)
        expr = self.expr()
        self.insSkiper()
        self.addins(Const(name, expr))

    def pars(self):
        token = self.tokens[self.pos]
        while token[0] != T_EOF:
            if token[0] == T_INS_END: self.insSkiper()
            elif (token[0] == T_KEYWORDS) and (token[1] == "const"):
                const = self.constVar()
                self.addins(const)
            else: 
                expr = self.expr()
                self.insSkiper()
                self.addins(expr)
            token = self.tokens[self.pos]

class X86RealModeRegisters:
    def __init__(self):
        # General-purpose registers (16-bit)
        self.reg = {
            "A": {
                "L": True,
                "H": True,
                "p": True,
            },
            "B": {
                "L": True,
                "H": True,
                "p": True,
            },
            "C": {
                "L": True,
                "H": True,
                "p": True,
            },
            "D": {
                "L": True,
                "H": True,
                "p": True,
            },
        }
    
    def resave(self, reg: Reg):
        reg = reg.reg[1]
        for x in self.reg:
            r = self.reg[x]
            if reg[0] == x: 
                if reg[1] == "X":
                        self.reg[x]["p"] = False
                        self.reg[x]["H"] = False
                        self.reg[x]["L"] = False
                        return True
                elif reg[1] == "H":
                    self.reg[x]["H"] = False
                    return True
                elif reg[1] == "L":
                    self.reg[x]["L"] = False
                    return True
        return False

    def lode(self, bit=16):
        for x in self.reg:
            r = self.reg[x] 
            if r["p"] == True:
                if bit==16: 
                    self.reg[x]["p"] = False
                    self.reg[x]["H"] = False
                    self.reg[x]["L"] = False
                    return Reg((x+"X"))
            if bit==8:
                if self.reg[x]["H"] == True:
                    self.reg[x]["H"] = False
                    return Reg((x+"H"))
                elif self.reg[x]["L"] == True:
                    self.reg[x]["L"] = False
                    return Reg((x+"L"))

    def unlode(self, reg):
        reg = reg.reg[1]
        for x in self.reg:
            r = self.reg[x]
            if reg[0] == x: 
                if reg[1] == "X":
                        self.reg[x]["p"] = True
                        self.reg[x]["H"] = True
                        self.reg[x]["L"] = True
                        return True
                if reg[1] == "H":
                    self.reg[x]["H"] = True
                    return True
                elif reg[1] == "L":
                    self.reg[x]["L"] = True
                    return True
        return False

class codeExpr:
    def __init__(self, ins, reg):
        self.ins = ins
        self.reg = reg
    
    def addend(self, ins):
        for i in ins:
            self.ins.append(i) 
    
    def __repr__(self):
        s = ""
        for i in self.ins:
            s += f"{i}\n" 
        return s

class INSNSAM:
    def __init__(self, Opcode, Destination, Source):
        self.Opcode = Opcode
        self.Destination = Destination
        self.Source = Source
    
    def __repr__(self):
        return f"{self.Opcode} {self.Destination}, {self.Source}"

class UNARYINS:
    def __init__(self, Opcode, Destination):
        self.Opcode = Opcode
        self.Destination = Destination

    def __repr__(self):
        return f"{self.Opcode} {self.Destination}"

class SymbolTable:
    def __init__(self):
        self.data = {}

class compailer:
    def __init__(self, ins):
        self.ins = ins
        self.reg = X86RealModeRegisters()
        Stdata = SymbolTable()
        cxpr =  0
        self.cexpr = codeExpr([], None)
        while cxpr < len(ins):
            _ins = ins[cxpr]
            cxpr += 1 
            _cexpr = self.visit(_ins)
            if isinstance(_cexpr, Reg):
                self.cexpr.addend(_cexpr)
            elif isinstance(_cexpr, codeExpr):
                self.cexpr.addend(_cexpr.ins)
                self.cexpr.reg = _cexpr.reg
            elif isinstance(_cexpr, Integer):
                self.cexpr.addend(_cexpr)
    
    def visit(self, node):
        if isinstance(node, Num):
            return node.value[1]
        elif isinstance(node, Reg):
            return Reg(node.reg[1])
        elif isinstance(node, BinOp):
            left = self.visit(node.left)
            right = self.visit(node.right)
            if (((isinstance(left, Reg)) or (isinstance(left, Integer))) or (isinstance(left, codeExpr))) and (((isinstance(right, Reg)) or (isinstance(right, Integer))) or (isinstance(right, codeExpr))):
                if (isinstance(left, Reg)) and isinstance(right, Reg): 
                    self.reg.resave(left)
                    return codeExpr([INSNSAM(node.op[0], left, right)], left)
                elif isinstance(left, Integer) and isinstance(right, Reg):
                    if node.op[0] in (T_PLUS, T_MUL, T_BIT_AND, T_BIT_OR, T_BIT_XOR, T_EQ, T_NEQ):
                        self.reg.resave(right)
                        return codeExpr([INSNSAM(node.op[0], right, left)], right)
                    else:
                        if right.reg[1] == "X": bitr = 16
                        else: bitr = 8  
                        r = self.reg.lode(bitr)
                        ins = [INSNSAM(T_MOV, r, right), INSNSAM(node.op[0], r, left)]
                        self.reg.unlode(r)
                        return codeExpr(ins, r)
                elif (isinstance(left, Reg)) and isinstance(right, Integer):
                    self.reg.resave(left)
                    return codeExpr([INSNSAM(node.op[0], left, right)], left)
                elif isinstance(left, Integer) and (isinstance(right, Integer)):
                    try:
                        if node.op[0] == T_PLUS:
                            return left + right
                        elif node.op[0] == T_MINUS:
                            return left - right
                        elif node.op[0] == T_MUL:
                            return left * right
                        elif node.op[0] == T_DIV:
                            if right == 0:
                                raise InterpreterError("Division by zero", node.op[2], node.op[3], node.op[4])
                            return left / right
                        elif node.op[0] == T_FLOORDIV:
                            if right == 0:
                                raise InterpreterError("Floor division by zero", node.op[2], node.op[3], node.op[4])
                            return left // right
                        elif node.op[0] == T_MOD:
                            if right == 0:
                                raise InterpreterError("Modulo by zero", node.op[2], node.op[3], node.op[4])
                            return left % right
                        elif node.op[0] == T_POW:
                            return left ** right
                        elif node.op[0] == T_EQ:
                            return left == right
                        elif node.op[0] == T_NEQ:
                            return left != right
                        elif node.op[0] == T_GT:
                            return left > right
                        elif node.op[0] == T_LT:
                            return left < right
                        elif node.op[0] == T_GTE:
                            return left >= right
                        elif node.op[0] == T_LTE:
                            return left <= right
                        elif node.op[0] == T_BIT_AND:
                            return left & right
                        elif node.op[0] == T_BIT_OR:
                            return left | right
                        elif node.op[0] == T_BIT_XOR:
                            return left ^ right
                        elif node.op[0] == T_LT:
                            if right < 0:
                                raise InterpreterError("ValueError: negative shift count", node.op[2], node.op[3])
                            return left << right
                        elif node.op[0] == T_SHR:
                            return left >> right
                        elif node.op[0] == T_LOG_AND:
                            return left and right
                        elif node.op[0] == T_LOG_OR:
                            return left or right
                    except TypeError:
                        raise InterpreterError("Invalid operation between non-numeric types", node.op[2], node.op[3])

                elif isinstance(left, codeExpr) and isinstance(right, codeExpr):
                    left.addend(right.ins)
                    left.addend([INSNSAM(node.op[0], left.reg, right.reg)])
                    self.reg.unlode(right.reg)
                    return left
                elif isinstance(left, codeExpr) and (isinstance(right, Integer)):
                    left.addend([INSNSAM(node.op[0], left.reg, right)])
                    return left
                elif isinstance(left, codeExpr) and (isinstance(right, Reg)):
                    left.addend([INSNSAM(node.op[0], left.reg, right)])
                    return left
                elif (isinstance(left, Reg)) and isinstance(right, codeExpr):
                    right.addend([INSNSAM(node.op[0], left, right.reg)])
                    right.reg = left
                    return right
                elif isinstance(left, Integer) and isinstance(right, codeExpr):
                    if node.op[0] in (T_PLUS, T_MUL, T_BIT_AND, T_BIT_OR, T_BIT_XOR, T_EQ, T_NEQ):
                        right.addend([INSNSAM(node.op[0], right.reg, left)])
                        return right
                    else:
                        if right.reg[1] == "X": bitr = 16
                        else: bitr = 8  
                        r = self.reg.lode(bitr)
                        ins = [INSNSAM(T_MOV, r, right.reg), INSNSAM(node.op[0], r, left)]
                        self.reg.unlode(r)
                        return codeExpr(ins, r)
                else: raise InterpreterError("Syntax error invalid syntax", node.op[2], node.op[3], node.op[4])
        elif isinstance(node, Reg):
            return Reg(node.reg[1])
        elif isinstance(node, UnaryOp):
            expr = self.visit(node.expr)
            if isinstance(expr, Integer):
                if node.op[0] == T_LOG_NOT:
                    return expr.__not__()
                elif node.op[0] == T_BIT_NOT:
                    return ~expr
                elif node.op[0] == T_PLUS:  
                    return +expr
                elif node.op[0] == T_MINUS: 
                    return -expr
                else: raise InterpreterError("Syntax error invalid syntax", node.op[2], node.op[3], node.op[4])
            elif isinstance(expr, Reg):
                return codeExpr([UNARYINS(node.op[1], expr)], expr)
            elif isinstance(expr, codeExpr):
                expr.addend(UNARYINS(node.op[1], expr.reg))
                return expr


class MakeAssamblyCode:
    def __init__(self, code, m=16, tm=32):
        self.m = m
        self.tm = tm 
        self.code : codeExpr = code 
        self.st = SymbolTable()
        self.st.data["A"] = Integer(0x0000)
        self.st.data["B"] = Integer(0x0000)
        self.st.data["C"] = Integer(0x0000)
        self.st.data["D"] = Integer(0x0000)

    def get(self, r):
        if r[1] == "X": return self.st.data[r[0]]
        else: 
            if r[1] == "H": return self.st.data[r[0]+"X"] & Integer(0x0000FFFF)
            elif r[1] == "L": return self.st.data[r[0]+"X"] & Integer(0xFFFF)

    def MakeCode16(self):
        for x in self.code.ins:
            if isinstance(x, INSNSAM):
                print(x)
            elif isinstance(x, UNARYINS):
                print(x)
            else:
                print(f"not found: {type(x)}", x)
s = Parser(Tokenizer(""" 
+ax;
-ax;
~ax;
ax + 1;
ax - 1;
ax * 1;
ax / 1;
ax ** 1;
ax // 1;
ax % 1;
ax >> 1;
ax << 1;
ax & 1;
ax ^ 1;
ax | 1;
ax == 1;
ax != 1;
ax > 1;
ax < 1;
ax >= 1;
ax <= 1;
ax + not bx;
ax and 1;
ax or 1;
4 - 4 + ax;
ax ** 2 + bx ** 3;
ax // 3 * bx / 4 % cx;
ax << 2 >> bx & 15;
ax ^ bx | cx & dx;
ax >= 10 <= bx;
(ax + bx) * (cx - dx) ** 2 // 5 % 3;
+ax - ~bx + cx;
(ax + 1) << (bx - 2) & (cx | dx);
ax * bx ** 2 // cx % dx;
(ax ^ bx) | (cx & dx) + 15;
ax == bx and cx != dx;
not ax or bx;
(ax + bx) * (cx - dx) + (ax // bx);
(ax << 1) >> (bx + 2);
ax + bx * cx - dx // 2;
(ax + bx) ** 2 - (cx - dx) ** 3;
ax & bx | cx ^ dx;
(ax | bx) & (cx ^ dx);
ax + not bx and cx or dx;
((ax + bx) * (cx - dx)) // (ax % bx + 1);
""").get_tokens())
s.pars()
MakeAssamblyCode(compailer(s.ins).cexpr).MakeCode16()


