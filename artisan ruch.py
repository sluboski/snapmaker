import serial
import time

# Otwarcie połączenia z drukarką (zmienić port na odpowiedni)
ser = serial.Serial('COM3', 115200)

# Nazwa pliku G-code do zapisu
nazwa_pliku = "ruch1.gcode"

# Definiowanie pozycji początkowej
start_x = 0
start_y = 0
start_z = 50
dolne_z = 20

# Otwarcie pliku G-code do zapisu
with open(nazwa_pliku, "w") as plik_gcode:

    # Powtarzaj 12 razy
    for i in range(1,13):
        # Opuszczenie głowicy
        komenda = f'G1 Z{dolne_z} f500\n'
        ser.write(komenda.encode())  # Opuść głowicę
        time.sleep(0.2)
        print(f"Głowica opuszczona")
        plik_gcode.write(komenda)  # Zapisz komendę G-code do pliku

        # Podniesienie głowicy
        
        komenda = f'G1 Z{start_z} f500\n'
        ser.write(komenda.encode())  # Podnieś głowicę
        time.sleep(0.2)
        print(f"Głowica podniesiona")
        plik_gcode.write(komenda)  # Zapisz komendę G-code do pliku

        # Przesunięcie głowicy do przodu z coraz większym X
        target_x = start_x + i * 9
        
        komenda = f'G0 X{target_x} Y{start_y} Z{start_z} f1000\n'
        ser.write(komenda.encode())
        time.sleep(0)
        print(f"Głowica przesunięta do X={target_x}")
        plik_gcode.write(komenda)  # Zapisz komendę G-code do pliku

        # Opuszczenie głowicy
        komenda = f'G1 Z{dolne_z} f500\n'
        ser.write(komenda.encode())  # Opuść głowicę
        time.sleep(0.2)
        print(f"Głowica opuszczona")
        plik_gcode.write(komenda)  # Zapisz komendę G-code do pliku

        # Podniesienie głowicy
        komenda = f'G1 Z{start_z} f500\n'
        ser.write(komenda.encode())  # Podnieś głowicę
        time.sleep(0.2)
        print(f"Głowica podniesiona")
        plik_gcode.write(komenda)  # Zapisz komendę G-code do pliku

        # Wróć na miejsce początkowe
        komenda = f'G0 X{start_x} Y{start_y} Z{start_z} f1000\n'
        ser.write(komenda.encode())
        time.sleep(0)
        print(f"Głowica wróciła na pozycję początkową")
        plik_gcode.write(komenda)  # Zapisz komendę G-code do plik
        

    # Proces mycia
    # Opuszczenie głowicy
    komenda = f'G1 Z{dolne_z} f500\n'
    ser.write(komenda.encode())  # Opuść głowicę
    time.sleep(0.2)
    print(f"Głowica opuszczona")
    plik_gcode.write(komenda)  # Zapisz komendę G-code do pliku

    # Podniesienie głowicy
    komenda = f'G1 Z{start_z} f500\n'
    ser.write(komenda.encode())  # Podnieś głowicę
    time.sleep(0.2)
    print(f"Głowica podniesiona")
    plik_gcode.write(komenda)  # Zapisz komendę G-code do pliku

    # Przesunięcie głowicy do czystej wody
    cleaning_x = 150
    komenda = f'G0 X{cleaning_x} Y{start_y} Z{start_z} f1000\n'
    ser.write(komenda.encode())
    time.sleep(0)
    print(f"Głowica przesunięta do X={cleaning_x}")
    plik_gcode.write(komenda)  # Zapisz komendę G-code do pliku


    # 2 krotne opuszczenie i podniesienie w wodzie
    for i in range (2):
        # Opuszczenie głowicy
        komenda = f'G1 Z{dolne_z} f500\n'
        ser.write(komenda.encode())  # Opuść głowicę
        time.sleep(0.5)
        print(f"Głowica opuszczona")
        plik_gcode.write(komenda)  # Zapisz komendę G-code do pliku

        # Podniesienie głowicy
        komenda = f'G1 Z{start_z} f500\n'
        ser.write(komenda.encode())  # Podnieś głowicę
        time.sleep(0.5)
        print(f"Głowica podniesiona")
        plik_gcode.write(komenda)  # Zapisz komendę G-code do pliku

    # Szybkie ruchy lewo-prawo
    for i in range(3):  # Wykonaj ruch lewo-prawo trzy razy
        # Ruch w lewo
        komenda_lewo = f'G0 X{start_x} Y{start_y - 2} Z{start_z} f500\n'
        ser.write(komenda_lewo.encode())
        time.sleep(0)
        print(f"Głowica przeunięta o -2 Y")
        plik_gcode.write(komenda_lewo)  # Zapisz komendę G-code do pliku

        # Ruch w prawo
        komenda_prawo = f'G0 X{start_x} Y{start_y + 2} Z{start_z} f500\n'
        ser.write(komenda_prawo.encode())
        time.sleep(0)
        print(f"Głowica przeunięta o +2 Y")
        plik_gcode.write(komenda_prawo)  # Zapisz komendę G-code do pliku

    # Podniesienie głowicy
    komenda = f'G1 Z{start_z} f500\n'
    ser.write(komenda.encode())  # Podnieś głowicę
    time.sleep(0.2)
    print(f"Głowica podniesiona")
    plik_gcode.write(komenda)  # Zapisz komendę G-code do pliku

    # Wróć na miejsce początkowe
    komenda = f'G0 X{start_x} Y{start_y} Z{start_z} f1000\n'
    ser.write(komenda.encode())
    time.sleep(0)
    print(f"Głowica wróciła na pozycję początkową")
    plik_gcode.write(komenda)  # Zapisz komendę G-code do pliku

# Zakończenie połączenia
ser.close()