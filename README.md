# Sleng Compiler
Sleng Compiler is a Python-based compiler for the **Sleng Interpreter** supporting Sleng Interpreter legnuage ko ap isse compile kar sakte hain. It includes a tokenizer, parser, AST generator, and intermediate assembly code generator.

## available Features
- Arithmetic operations (`+`, `-`, `*`, `/`, `%`, `**`, `//`)
- Bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`)
- Logical operations (`and`, `or`, `not`)
- X86 Real Mode Register simulation (`AX`, `BX`, `CX`, `DX`, etc.)
- Parentheses grouping and operator precedence
- AST generation and intermediate assembly code generation

```bash 
my Operator Precedence (Highest to Lowest)
Precedence  	Operator	            Description
1 (Highest)	    ()	                    Parentheses (grouping)
3		        +x, -x, ~x              Unary plus, minus, bitwise NOT
2		        **                      Exponentiation (right-to-left)
4		        *, /, //, %             Multiplication, division, floor division, modulo
5		        +, -                    Addition, subtraction
6		        <<, >>                  Bitwise shift left, right
7		        &                       Bitwise AND
8		        ^                       Bitwise XOR
9		        |                       Bitwise OR
10	            ==, !=, >, <, >=, <=	Comparisons (all have the same precedence)
11		        not                     Logical NOT
12	            and	                    Logical AND
13 (Lowest)		or                      Logical OR
```

## Example Usage

```cpp
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
```
## Limitations and Future Work
Abhi Sleng Interpreter sirf expressions ko support karta hai. Statements aur functions ka support jald hi add kiya jayega. Abhi ye x86 real mode registers ko simulate karta hai, jisme aap AX, BX, CX, DX, etc. ka use kar sakte hain. Lekin ye abhi complete nahi hai; jab Sleng Interpreter ko C/C++ me convert kiya jayega, tab ye fully functional ho jayega.

In dono projects ko complete hone me thoda samay lagega, lekin ye dono projects complete honge aur ek sath use kiye ja sakte hain. Sleng Interpreter ka code Sleng Compiler se compile kiya ja sakta hai. Is compiler se koi bhi development kar sakte hai jaise, OS development, OS applications, web servers, ERC development jaise projects ke liye low-level system development directly compile aur test kar sakte hain. Yehi Sleng Compiler ka main purpose hai. Dono projects fully compatible aur integrated honge.
