from pynput import keyboard

"""
문자 눌렀을 때 try:
	if 조건 1: 소문자 눌렀을때 => 자기번호까지전부출력 .upper
	   조건 2: 대문자 눌렀을때 => 자기번호까지전부출력 .lower 
그 외 눌렀을때 except:

"""
def ex(key):
    # ascii +- 65[A] 97[a] - string
    # upper, lower - string
    try:
        if str.islower(key.char):
            for i in range(ord('a'),ord(key.char)+1):
                print(chr(i).upper(), end="")
        elif str.isupper(key.char):
            for i in range(ord('A'),ord(key.char)+1):
                print(chr(i).lower(), end="")
        print()
    except Exception:
        if key == keyboard.Key.esc:
            return False
        pass



with keyboard.Listener(on_press=ex) as listener:
    listener.join()