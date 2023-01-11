import sys,os,time

"""Uma clase cum um metodo que faz os texto imprimirem devagar"""
class texto_devagar:
    def texto(texto):
        for char in texto:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.001)
        return ''