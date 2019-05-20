.thumb
pop	{r3}
push	{r0-r7}

@check if this is the map being drawn
cmp	r6,#0x0B
bne	End

@check if there is a new image for this map
lsl	r0,#2
ldr	r1,saveTable
ldr	r0,[r1,r0]
cmp	r0,#0
beq	End

@load the new image
ldr	r1,=#0x6008740
ldr	r2,=#0x6008E80
loop:
ldr	r3,[r0]
str	r3,[r1]
add	r0,#4
add	r1,#4
cmp	r1,r2
blo	loop

End:
ldr	r3,=#0x8005160
mov	lr,r3
pop	{r0-r7}
lsl	r1,r0,#2
add	r1,r0
lsl	r0,r1,#4
sub	r0,r1
lsl	r0,#2
.short	0xF800

.align
.ltorg
saveTable:
