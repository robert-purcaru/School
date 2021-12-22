.text
.global _start
_start:
	ldr		r10, =0xFF200050		//	keys register
	ldr		r5, =0xFF200000		// 	LED registers
	ldr		r6, =NUMS			// 	Root of nums	
	ldr		r7, =0xFFFEC600		//	Delay Register
	ldr		r0, =100000000		//	50000000 for 0.25ms delay time
	mov		r1, #4				//	current index counter
	mov		r4, #1				//	offset dir
	
	str		r0, [r7]			//	Store 0.25ms time in timer
	mov		r0, #0b011
	str		r0, [r7, #8]
	
	ldr		r8, [r6, #4]
	str		r8, [r5]
	
READY:
	//str		r7, [r5]			//	for test
	mov		r2, #0
	ldr		r0, [r10]
	ldr		r3, [r6]
	ands	r0, r3
	bne		READY_WAIT
	b		READY

READY_WAIT:
	//str		r6, [r5]			//	for test
	ldr		r0, [r10]
	ldr		r3, [r6]
	ands	r0, r3
	beq		LOOP_START
	b		READY_WAIT

LOOP_START:
	ldr		r0, [r6, r1]
	str		r0, [r5]
	ldr		r0, [r7, #0xC]
	str		r0,	[r7, #0xC]
	bl		DELAY
	cmp		r1, #4			//	Setting direction register
	moveq	r4, #1
	cmp		r1, #20
	moveq	r4, #0
	
	cmp		r4, #1
	addeq	r1, #4
	subne	r1, #4
	b		LOOP_START

DELAY:	
	ldr		r0, [r10]			// Button Check
	ldr		r3, [r6]	
	ands	r0, r3
	movne	r2, #8
	cmp		r2, r0
	bne		READY
	
	ldr		r0, [r7, #0xC]		// Timer Check
	cmp		r0,	#0
	beq		DELAY
	str		r0,	[r7, #0xC]
	mov		pc, lr

END:
	b		END
	
NUMS:
	.word	8, 513, 258, 132, 72, 48	//	8 is used to compare for KEY3

.end