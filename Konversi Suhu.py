#Belajar perhitungan sederhana suhu

#Input Nilai Celcius 
celcius = float(input("Masukkan nilai celcius disini : "))

#Script Loading ..

from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep


class Loader:
    def __init__(self, desc="Loading Cek Suhu...", end="Done!", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


if __name__ == "__main__":
    with Loader("Running Script cek suhu © Doni......"):
        for i in range(10):
            sleep(0.25)

    loader = Loader("Sedang menghitung data..", "Berhasil Menghitung !", 0.05).start()
    for i in range(10):
        sleep(0.25)
    loader.stop()
    
# Tampilkan Nilai Celcius
print("\nNilai celcius yang kalian input adalah : ", celcius,"\n\n")
print("====================== ")
print("NILAI CELCIUS KE SUHU LAINNYA ")
print("====================== ")
# Ubah Nilai Celcius Ke Reamur rumus (4/5)*celcius
reamur = (4/5)*celcius
print("• Celcius --> Reamur : ",reamur,"R")

# Ubah Nilai Celcius Ke Farenheit rumus 9/5*celcius+32
farenheit = (9/5)*celcius+32
print("• Celcius --> Farenheit : ", farenheit,"F")

#Ubah Nilai Celcius Ke Kelvin rumus celcius+273
kelvin = celcius + 273.15
print("• Celcius --> Kelvin : ", kelvin, "°K")



print("\n\n====================== ")
print("NILAI REAMUR KE SUHU LAINNYA ")
print("====================== ")
#Ubah Dari Reamur ke celcius rumus 5/4*Reamur
reamur_c = 5/4*reamur
print("• Reamur --> Celcius : ",reamur_c)

#Ubah Reamur ke Farenheit rumus 9/4*Reamur+32
reamur_f = (9/4)*reamur+32
print("• Reamur --> Farenheit : ",reamur_f)

#Ubah Reamur ke Kelvin rumus 5/4*reamur+273
reamur_k = (5/4)*reamur+273.15
print("• Reamur --> Kelvin : ", reamur_k)



print("\n\n====================== ")
print("NILAI FARENHEIT KE SUHU LAINNYA ")
print("====================== ")
#Ubah Dari Farenheit ke Celcius == 5/9*(F-32)
farenheit_c = 5/9*(farenheit-32)
print("• Farenheit --> Celcius : ",farenheit_c)

#Ubah Farenheit ke Reamur == rumus 4/9*(F-32)
farenheit_r = 4/9*(farenheit-32)
print("• Farenheit --> Reamur : ",reamur_f)

#Ubah Farenheit ke Kelvin rumus 5/4*reamur+273
reamur_k = (5/4)*reamur+273.15
print("• Farenheit --> Kelvin : ", reamur_k)



print("\n\n====================== ")
print("NILAI KELVIN KE SUHU LAINNYA ")
print("====================== ")
#Ubah Dari Kelvin ke Celcius == K-273
kelvin_c = kelvin-273.15
print("• Kelvin --> Celcius : ",kelvin_c)

#Ubah Kelvin ke Reamur == 4/5(K-273)
kelvin_r = 4/5*(kelvin-273)
print("• Kelvin --> Reamur : ",kelvin_r)

#Ubah Kelvin ke farenheit 9/5*(K-273)+32
kelvin_f = (9/5)*(kelvin+273)+32
print("• Kelvin --> Farenheit : ", kelvin_f)
