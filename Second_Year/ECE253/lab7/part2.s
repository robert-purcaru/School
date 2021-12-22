.text
.global _start
_start:
	ldr		r2, =TEST_NUM
	ldr 	r1, [r2]
	mov		r0, #0
LOOP:
	cmp		r1, #0
	beq		END
	lsr		r2, r1, #1
	and		r1, r1, r2
	add		r0, #1
	b		LOOP
END:
	b		END
	
TEST_NUM:
	.word	0x103FE00F
.end


	
	