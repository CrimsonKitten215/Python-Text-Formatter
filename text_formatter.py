def format(text: str, fg="-1", bg="-1", bold=False, italic=False, underline=False, strong_underline=False, strikethrough=False, boxed=False):
	"""
	Formats console text as specified (defaults to normal text).
	:param text: Text to be coloured
	:param fg: Hex foreground colour code
	:param bg: Hex background colour code
	:param bold: If you want it bold
	:param italic: If you want it italic
	:param underline: If you want it underlined
	:param strong_underline: If you want it underlined with an extra thick line
	:param strikethrough: If you want it crossed out
	:param boxed: If you want it boxed up like it's in a table
	:return: Formatted text
	"""

	# makes it bold/italic/etc
	code = ""
	if bold:
		code += ";1"
	if italic:
		code += ";3"
	if underline and not strong_underline:
		code += ";4"
	if strong_underline:
		code += ";21"
	if strikethrough:
		code += ";9"
	if boxed:
		code += ";51"

	# makes it colourful
	if fg != "-1":
		code += f";38;2;{int(fg[0:2], 16)};{int(fg[2:4], 16)};{int(fg[4:6], 16)}"
	if bg != "-1":
		code += f";48;2;{int(bg[0:2], 16)};{int(bg[2:4], 16)};{int(bg[4:6], 16)}"

	return f"\033[{code[1:]}m{text}\033[0m"


# built-in formatting codes cheat sheet
"""
Base = \033[{code}m
Specific RGB FG = \033[38;2;{r};{g};{b}m
Specific RGB BG = \033[48;2;{r};{g};{b}m

7 = Swap FG & BG (Basically useless)

0 = Normal <-- Clears all formatting
1 = Bold
3 = Italic
4 = Underlined
9 = Strikethrough
21 = Strong Underline
51 = Boxed

30 = Black FG
31 = Red FG
32 = Yellow FG
33 = Green FG
34 = Blue FG
35 = Purple FG
36 = Cyan FG
37 = Grey FG

90 = Dark Grey FG
91 = Lighter Red FG
92 = Vibrant Yellow FG
93 = Vibrant Green FG
94 = Lighter Blue FG <-- User input colour
95 = Bright Pink FG
96 = Vibrant Cyan FG
97 = Perfect White FG

40 = Black BG
41 = Red BG
42 = Yellow BG
43 = Green BG
44 = Blue BG
45 = Purple BG
46 = Cyan BG
47 = Grey BG

100 = Lighter Black BG
101 = Lighter Red BG
102 = Vibrant Yellow BG
103 = Vibrant Green BG
104 = Lighter Blue BG
105 = Bright Pink BG
106 = Vibrant Cyan BG
107 = Perfect White BG
"""