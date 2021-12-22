.text
.global SWAP
.global _start

_start:
	ldr		r0, =LIST
	bl		BUBBLE
	b 		END

BUBBLE:
	push	{r4}
	ldr 	r4, [r0]	// r4 holds num of nums
	mov		r3, #1		// r3 holds current comparison front
	add		r0, r0, #4
	mov		r1, #0
	mov		r2, #0
	
LOOP:
	cmp		r4, #1
	popeq	{r4}
	moveq	pc, lr
	push	{r0, lr}
	bl		SWAP
MID_LOOP:
	pop		{r0, lr}
	add		r0, r0, #4
	add		r3, #1
	cmp		r3, r4
	bne		LOOP
	sub		r4, #1	
	sub		r0, r4
	sub		r0, r4
	sub		r0, r4
	sub		r0, r4
	mov		r3, #1
	b		LOOP
	
SWAP:
	ldr		r1, [r0]		// r1 holds curr num
	ldr		r2, [r0, #4]	// r2 holds next num
	cmp		r2, r1			
	strlt	r1, [r0, #4]
	strlt	r2, [r0]
	mov		r0, #0
	movlt	r0, #1
	mov		pc, lr

END:
	b		END

LIST: .word 10, 1400, 45, 23, 5, 3, 8, 17, 4, 20, 33


.end
