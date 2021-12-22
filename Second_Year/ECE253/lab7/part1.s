.global _start
_start:
	LDR 	R1, =TEST_NUM
	BL 		COUNTER	

COUNTER: 
	MOV 	R8, #0
	MOV 	R7, #0
LOOP:
	LDR 	R2, [R1]
	CMP		R2, #-1
	BEQ		END
	ADD 	R7, R7, R2
	CMP 	R2, #0
	ADDGT 	R8, #1
	ADD 	R1, R1, #4
	B		LOOP

END:
	B		END
	
.end


	
	