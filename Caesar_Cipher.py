
def letter_shifter(text):
    Cipher = ''
    for char in text:
        if char ==' ':                                  #Ciclo for para recorrer el string.
            Cipher += char                              #En caso de un espacio lo mantenemos, se podria eliminar para que se trate como un caracter igual al resto.
        else:
            Cipher += chr((ord(char) + shift))          #Tomamos un caracter, al cual le extraemos su valor Unicode y le sumamos el valor que queremos cambiar. 
    return Cipher                                       #luego asignamos el resulado de esa suma con el metodo chr para convertirlo de nuevo al caracter nuevo.

#================================================================

in_Text = input('Please enter the desired text to cipher:\n\n==> ')

#================================================================



#================================================================   
validate_shift_value = False

while validate_shift_value == False:
    shift = int(input('Please enter a value to cipher beetwen 1 and 25:\n\n==> '))
    if shift == shift>0 and shift < 26:
        validate_shift_value = True
    else:
        validate_shift_value = validate_shift_value
#================================================================

cipher_text=letter_shifter(text=in_Text)
print('\n',cipher_text,'\n')