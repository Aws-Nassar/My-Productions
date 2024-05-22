page 60,132
title FINAL_PROJECT
;----------------------------
.model small
.stack 64
;------------------------------
.data
 messege db "Please enter a mathmatical paragraph :",10,13,'$'
 Emessage db "Error, You excceded the 100 character !! ",10,13,'$'  
 
 parlist label byte
 maxlen db 100
 actlen db ?
 array db 100 dup(' ')

 Num db 33 dup(-1) ;to store the given numbers
 NumSize db 0 

 op db '?' ;to store the given operation     

 totalArr db 30 dup('#') ;to store the result
 totalsize db 0     

 final db 70 dup('*') ;to store the numbers and operation as a syntax 
 finalSize db 0

 row db 0
 col db 0 

arrowmessege db "Please press on an arrow: ",10,13,'$'
empty db "                                                            $",10,13 
;------------------------

.code   

Main proc far    
    mov ax,@data
    mov ds,ax 
          
    call clear    ;clear the screen 
        
   ;---set the cursor in the upperleft corner. 
   
    mov dx,0000   ;00:row    00:column
    call setCursor       
    call print    ;will print the massage   
    call read     ;accept input from the keyboard
    call clear 
        
    ;--check the input size
    cmp actlen,0
    je endl
    
    mov al,maxlen  
    cmp actlen,al 
    jge error 
    ;-------------------- 
    call dollar ; to add $ to the end of the input   
                                            
    call find ; to find the number where included in the paragraph  
     
    call Operation ; do the operation on the given numbers and calculate the result 
    
    call Finalize ; put the numbers and the operation in one array
     
    call centerized ; set Cursor in the center of the screen
    
    call result ; print the final expression 
    
    mov ah,09h 
    lea dx,empty
    int 21h  
    mov ah,09h 
    lea dx,arrowmessege
    int 21h
    call shift
    jmp endL
    
    error:
    mov ah,09h
    lea dx,Emessage
    int 21h
     
    endL:
    mov ax,4c00h  ; exit to the OS.
    int 21h
    Main endp
   
shift proc near 
    mov cl,finalSize
    mov col,cl
    shr col,1 
    neg col
    add col,39 
    mov row,12 
    
    mov si, 0
    mov dh, 0
    mov dl, 0
    
arroww:     
    mov ah, 00h
    int 22  
   
    cmp ah, 48h  
    je up
    
    cmp ah, 50h  
    je down
   
    cmp ah, 4Dh 
    je right
  
    cmp ah, 4Bh  
    je left
    jmp exit 
    
up:   
    call clear
    dec row 
    mov dh,row
    mov dl,col
    call setCursor
    call result
    jmp arroww 
    
down: 
     call clear
     inc row 
     mov dh,row
     mov dl,col
     call setCursor
     call result
     jmp arroww  
     
right:    
      call clear
      inc col 
      mov dh,row
      mov dl,col
      call setCursor
      call result
      jmp arroww
left:  
      call clear
      dec col 
      mov dh,row
      mov dl,col
      call setCursor
      call result
      jmp arroww
exit:
    int 020
	ret
shift endp  

;------clear procedure------
clear proc near
     mov ax, 0600h  ; ah=06h, al=00 
     mov bh, 71h  ; blue
     mov cx,0000h ; from
     mov dx,184Fh ; to 
     int 10h
     
     ret
 clear endp 

;----------Set Cursor Procedure----
setCursor proc near
    mov ah,02h
    mov bh,00
    int 10h
    
    ret
setCursor endp  

;------------prompt-------------
print proc near
    mov ah,09h
    lea dx,messege
    int 21h
    
    ret
print endp

;--------------read input from keyboard -----
read proc near
    mov ah,0Ah
    lea dx,maxlen  
    int 21h
    
    ret
read endp  

;----------process input------------
dollar proc near
    mov bh,00
    mov bl,actlen 
    mov array[bx],'$'
     
    ret
dollar endp  

;------------procedure to center---------------
centerized proc near
      mov dl,finalSize
      shr dl,1
      neg dl
      add dl,39 
      mov dh,12
      call setCursor
       
      ret
centerized endp 

;--------------------------------------------;
       
Operation proc near 
     lea di,Num   
     mov al,0 
     mov bl,Numsize  
     cmp op,'+'
     je  addition1 
     
     cmp op,'*'
     je  multiply1
      
     cmp op,'/'
     je  divide1
     
     
     addition1: 
               add al,[di]
               inc di
               cmp [di],-1
               dec bl
               cmp bl,0
               je end1
               jmp addition1
     
     multiply1: 
               mov al,[di] 
               inc di
     multiply2:
               mul [di]
               inc di
               cmp [di],-1
               je end1
               jmp multiply2
     divide1: 
             mov al,[di] 
             inc di
     divide2:
             div [di]
             inc di
             cmp [di],-1
             je end1
             jmp divide2
     
     end1: 
          mov si,0 
          cmp al,09h
          jle end12  
     totalCal:
              mov ah,00h         
              mov dx,0             
              mov bx,10h          
              div bx 
              mov totalArr[si],dl
              inc si
              cmp al,9
              jle continue
              jmp totalCal
     continue:
              mov ax,si
              mov totalsize, al  
              jmp end13
     end12: 
           mov totalArr[si],al
           mov al,1
           mov totalsize,al 
     end13:
     ret
Operation endp
;--------------------------------------------;     
Finalize proc near
    lea di,Num   
    mov si,0 
    mov bl,Numsize
    start1: 
           cmp bl,0
           je endl1  
           mov al,[di] 
           mov final[si],al
           inc di
           inc si
           mov al,op
           mov final[si],al
           inc si  
           dec bl
           jmp start1
   endl1: 
         dec si       
         mov al,'='
         mov final[si],al
         
         mov cl,Numsize 
         looooaaap:
                   cmp cl,1
                   je naneeeee
                   dec si 
                   dec cl
                   jmp looooaaap
          
         naneeeee:
         mov ax,si
         mov finalSize, al    
    ret
 Finalize endp
;--------------------------------------------;    
                   
;--------------------------------------------;   
result proc near 
    
  mov si, offset final
  mov cl, finalsize
  mov ah, 02h
  
  loop_start:
             mov dl,[si]
             add dl,48
             int 21h
             inc si 
             mov dl,32
             int 21h 
             mov dl,[si]
             int 21h
             mov dl,32
             int 21h 
             inc si 
             dec cl
             cmp cl,0
             jne loop_start
    
  mov si, offset totalArr 
    ;mov cl,0
    ;ldadadfsaa:
           ;    cmp [si],'#'
           ;    je exit111 
           ;    inc si 
           ;    inc cl
           ;    jmp ldadadfsaa 
    ;exit111: 
           ;    dec si
           ;    mov dl,[si]
           ;    add dl,48
           ;    int 21h
           ;    dec cl
           ;    cmp cl,0
           ;    jl exit1111e1eqeqw
           ;    jmp exit111
  loop_start1:
              mov dl,[si]
              add dl,48
              int 21h
              inc si 
              cmp [si],'#' 
              jne loop_start1
                              
  exit123:        
  ret 
result endp 

;-----------------Search for number characters----------------------

find proc near
    lea di,array
    mov si,0 
    
 start:
      mov cx,di
      cmp [di],'$'
      je last
      cmp di,' '
      je div1 
  
 zero:
     mov di,cx  
     cmp [di],'z'
     jne one
     inc di 
     
     cmp [di],'e'
     jne one
     inc di 
     
     cmp [di],'r'
     jne one
     inc di   
     
     cmp [di],'o'
     jne one 
     mov Num[si],0
     inc si
     inc di
     jmp start
     
     
 one: 
     mov di,cx  
     cmp [di],'o' 
     jne two
     inc di 
     
     cmp [di],'n'      
     jne two
     inc di  
     
     cmp [di],'e'
     jne two 
     mov Num[si],1
     inc si
     inc di
     jmp start
  
 two: 
     mov di,cx  
     cmp [di],'t' 
     jne three
     inc di 
     
     cmp [di],'w'
     jne three
     inc di 
     
     cmp [di],'o'
     jne three 
     mov Num[si],2
     inc si 
     inc di
     jmp start  
      
 three:
     mov di,cx  
     cmp [di],'t' 
     jne four
     inc di                                  
     
     cmp [di],'h'                              
     jne four                                    
     inc di  
     
     cmp [di],'r'
     jne four
     inc di 
     
     cmp [di],'e'
     jne four
     inc di 
     
     cmp [di],'e'
     jne four 
     mov Num[si],3
     inc si
     inc di
     jmp start  
     
 four:
     mov di,cx  
     cmp [di],'f' 
     jne five
     inc di 
     
     cmp [di],'o'
     jne five
     inc di  
                   `
     cmp [di],'u'
     jne five
     inc di 
     
     cmp [di],'r'
     jne five 
     mov Num[si],4
     inc si
     inc di
     jmp start 
     
 five:   
     mov di,cx  
     cmp [di],'f' 
     jne six
     inc di 
     
     cmp [di],'i'
     jne six
     inc di  
     
     cmp [di],'v'
     jne six
     inc di 
     
     cmp [di],'e'
     jne six 
     mov Num[si],5
     inc si
     inc di
     jmp start 
     
 six:
     mov di,cx  
     cmp [di],'s' 
     jne seven
     inc di 
     
     cmp [di],'i'
     jne seven
     inc di 
     
     cmp [di],'x'
     jne seven 
     mov Num[si],6
     inc si  
     inc di
     jmp start
     
      
 seven: 
     mov di,cx  
     cmp [di],'s' 
     jne eight
     inc di 
     
     cmp [di],'e'
     jne eight
     inc di
     
     cmp [di],'v'
     jne eight
     inc di
     
     cmp [di],'e'
     jne eight
     inc di 
     
     cmp [di],'n'
     jne eight 
     mov Num[si],7
     inc si 
     inc di
     jmp start  
     
     
 eight: 
     mov di,cx  
     cmp [di],'e' 
     jne nine
     inc di 
     
     cmp [di],'i'
     jne nine
     inc di
     
     cmp [di],'g'
     jne nine
     inc di
     
     cmp [di],'h'
     jne nine
     inc di 
     
     cmp [di],'t'
     jne nine 
     mov Num[si],8
     inc si
     inc di
     jmp start  
     
 nine: 
     mov di,cx  
     cmp [di],'n' 
     jne addition
     inc di 
     
     cmp [di],'i'
     jne addition
     inc di  
     
     cmp [di],'n'
     jne addition
     inc di 
     
     cmp [di],'e'
     jne addition 
     mov Num[si],9
     inc si
     inc di
     jmp start  
                       
 addition:
     mov di,cx  
     cmp [di],'a' 
     jne multiply
     inc di 
     
     cmp [di],'d'
     jne multiply
     inc di  
     
     cmp [di],'d'
     jne multiply 
     mov op,'+'
     inc di 
     jmp start
     
 multiply: 
     mov di,cx  
     cmp [di],'m' 
     jne divide
     inc di 
     
     cmp [di],'u'
     jne divide
     inc di
     
     cmp [di],'l'
     jne divide
     inc di
     
     cmp [di],'t'
     jne divide
     inc di  
     
     cmp [di],'i'
     jne divide
     inc di   
     
     cmp [di],'p'
     jne divide
     inc di  
     
     cmp [di],'l'
     jne divide
     inc di
     
     cmp [di],'y'
     jne divide 
     mov op,'*'
     inc di
     jmp start  
     
 divide:
     mov di,cx  
     cmp [di],'d'  
     jne div1  
     inc di
     
     
     cmp [di],'i'
     jne div1  
     inc di 
     
     cmp [di],'v'
     jne div1  
     inc di
     
     cmp [di],'i'
     jne div1  
     inc di  
     
     cmp [di],'d'
     jne div1  
     inc di   
     
     cmp [di],'e'
     jne div1 
     mov op,'/'
     inc di 
     jmp start 
     
 div1:
     inc di 
     jmp start
        
 last:  
    mov ax,si
    mov Numsize, al
         
    ret
find endp

end