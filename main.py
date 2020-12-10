while True:
    if input.button_is_pressed(Button.B):
        for i in range(5):
         led.unplot(i, i)
         led.unplot(i, 4-i)
    basic.pause(10)
    if input.button_is_pressed(Button.A):
        for i in range(5):
         led.plot(i, i)  
         led.plot(i, 4-i)    
    basic.pause(10)    