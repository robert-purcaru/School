.global ONES	

ONES:		
	mov		r0, #0
LOOP:
	cmp		r1, #0
	moveq	pc, lr
	lsr		r2, r1, #1
	and		r1, r1, r2
	add		r0, #1
	b		LOOP



	
	