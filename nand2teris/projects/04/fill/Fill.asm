// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
//
//	i = 0
//	LOOP:
//		pointer = screen
//		m[pointer+i] = -1
//		i++
//	
//		goto LOOP

//i = 0

(LOOP)
	//if kbd == R1 goto  LOOP
	@KBD
	D=M
	@R1
	D=D-M
	@LOOP
	D;JEQ

	//else store key
	@KBD
	D=M
	@R1
	M=D
	//And fill screen
	@KBD
	D=M
	@POSITIVEIF
	D;JEQ
	@ELSEIF
	0;JMP

(POSITIVEIF)
	@R2
	M=0
	@i
	M=0
	@SCREENLOOP
	0;JMP
(ELSEIF)
	@R2
	M=-1
	@i
	M=0
	@SCREENLOOP
	0;JMP

(SCREENLOOP)
	//pointer = screen
	@SCREEN
	D=A
	@pointer
	M=D

	//m[pointer + i] = -1
	@i
	D=M
	@pointer
	D=M+D
	@R3
	M=D
	@R2
	D=M
	@R3
	A=M
	M=D

	//i++
	@i
	M=M+1

	//BREAK
	D=M
	@R0
	D=M-D;
	@LOOP
	D;JEQ

	@SCREENLOOP
	0;JMP
	
(END)
	@END
	0;JMP
