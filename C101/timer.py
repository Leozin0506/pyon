import time

def crono(sec):
    while sec>0:
        min = int(sec/60);
        segundos = int(sec%60);
        timer = f'{min}:{segundos}';
        print(timer, end='\r');
        time.sleep(1)
        sec -=1;
    print("Tempo esgotado.");

sec = (input("Digite o tempo em segundos: "));
crono(int(sec));