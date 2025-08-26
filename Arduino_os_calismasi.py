import serial
import time
import os 
import datetime
result=os.getcwd()
print(result)
try:
    ser=serial.Serial('COM3',9600,timeout=1)
    print(f"COM3 portu başariyla açildi")
    time.sleep(2)
except serial.SerialException as error:
    print(f" Hata seri porta bağlanilamadi. Lütfen COM3 portunu kontrol ediniz. {error}")
    exit()
except PermissionError:
    print(f"Port erişimi engellendi. Lütfen kontrol ediniz")
    exit()

tarih=datetime.date.today() 
günlük_klasör=f"{tarih}_logs"
if not os.path.exists(günlük_klasör):
   os.mkdir(günlük_klasör)
dosya_yolu=os.path.join(günlük_klasör,"gunluk.txt")
print("Günlük klasörü:", os.path.abspath(günlük_klasör))
  
try:  
   while True:
      
    veri=ser.readline().decode('utf-8').strip()
    if not veri:
     raise ValueError("Boş veri alindi.")
    veri_ayirma=veri.split(",")
    sicaklik=float(veri_ayirma[0])
    pot=int(veri_ayirma[1])
    
    zaman=datetime.datetime.now().strftime("%H:%M:%S")
    if veri:
     print(f"Arduinodan gelen veri: {veri}")
    print(f"{zaman} --> Sicaklik: {sicaklik} Pot: {pot}")
    with open(dosya_yolu,"a") as file:
     file.write(f"{zaman} --> Sicaklik: {sicaklik} °C | Pot: {pot}\n")
     file.flush()
     os.fsync(file.fileno()) 
    
except UnicodeDecodeError:
 print(f"Bozuk veri alindi.")
except ValueError as err:
 print("Sayiya çevrilemeyen veri: {err} ")
except IndexError:
 print("Veri eksik veya yanliş formatta geldi")
except OSError as e:
      print(f"Dosya yazma hatası:{e}")
finally:
     if ser.is_open:
        ser.close()
        