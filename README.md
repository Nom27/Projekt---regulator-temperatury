# 🌡️ System regulacji temperatury (PID) — Nucleo + BMP280

Projekt zaliczeniowy z przedmiotu **Systemy mikroprocesorowe**.

Celem projektu było zaprojektowanie i fizyczna implementacja systemu regulacji temperatury grzałki (rezystor 5 W / 50 Ω) w oparciu o mikrokontroler z rodziny Nucleo. System reguluje temperaturę w zadanym zakresie za pomocą grzałki (podnoszenie temperatury) oraz wentylatora (obniżanie temperatury), a cały układ został zbudowany i przetestowany na rzeczywistych podzespołach — nie tylko zasymulowany. Pełny opis projektu, schemat elektryczny i założenia znajdują się w [`Raport.pdf`](./Raport.pdf).

---

## 📸 Układ rzeczywisty

<img width="540" alt="Regulator_temp" src="https://github.com/user-attachments/assets/3e430c9a-d39e-48f5-a41b-cbd9f72a5923" />

---

## 🧩 Opis systemu

Sterowany proces to temperatura grzałki, mierzona czujnikiem **BMP280** i regulowana za pomocą:

- **grzałki** (rezystor mocy 5 W) sterowanej sygnałem **PWM** przez tranzystor MOSFET (Q1) w układzie z otwartym drenem,
- **wentylatora** sterowanego sygnałem cyfrowym (0/1) przez osobny tranzystor MOSFET (Q2).

Dodatkowo układ zawiera:

- wyświetlacz **LCD** prezentujący temperaturę aktualną, zadaną i sygnał sterujący,
- interfejs komunikacji **szeregowej (UART)** umożliwiający zdalne zadawanie temperatury oraz odczyt parametrów pracy systemu.

### Schemat elektryczny

Pełny schemat połączeń (czujnik BMP280 na magistrali SPI, sterowanie grzałką i wentylatorem, podłączenie LCD) znajduje się w raporcie — patrz `Raport.pdf`, rozdział *Schemat systemu*.

---

## ✅ Zrealizowane wymagania

**Wymagania minimalne**
- Pomiar temperatury z okresem 0.1 s.
- Regulacja w bezpiecznym zakresie 15–55 °C.
- Uchyb ustalony w granicach ±2 °C (5% zakresu regulacji).
- Zadawanie temperatury docelowej przez UART.
- Prezentacja temperatury aktualnej, zadanej i sygnału sterującego na LCD oraz przez UART.

**Wymagania dodatkowe**
- Implementacja regulacji **PID**.
- Sterowanie zarówno wentylatorem, jak i grzałką.
- Skrypt zapisujący/wizualizujący dane sygnału pomiarowego w czasie rzeczywistym (`PID.py`, `Projekt.py`).
- Prezentacja danych na wyświetlaczu LCD.
- Podział kodu na moduły i dokumentacja Doxygen.
- Kontrola wersji w Git/GitHub.

---

## 🐍 Skrypty Python

Oba skrypty łączą się z mikrokontrolerem po porcie szeregowym (UART) i na bieżąco odczytują dane w formacie `Setpoint:..., Temperature:..., PWM:...`, rysując dwa wykresy (temperatura zadana vs. rzeczywista oraz wypełnienie PWM grzałki) aktualizowane co sekundę.

| Plik | Opis |
|---|---|
| `PID.py` | Odczyt danych z portu szeregowego i wizualizacja temperatury oraz PWM w czasie rzeczywistym (`matplotlib.animation`). |
| `Projekt.py` | To samo co `PID.py`, rozszerzone o dodatkowy wątek pozwalający na wysyłanie komend do mikrokontrolera z poziomu konsoli (np. zmiana temperatury zadanej komendą typu `T010`). |

### Uruchomienie

1. Podłącz zestaw Nucleo do komputera i sprawdź, pod jakim portem szeregowym się pojawił (w skryptach domyślnie ustawiony jest `COM5`).
2. Zmień wartość `SERIAL_PORT` w wybranym skrypcie na odpowiedni port.
3. Uruchom:

```bash
python Projekt.py   # z możliwością wysyłania komend z konsoli
# lub
python PID.py        # tylko podgląd wykresów
```

4. W `Projekt.py` w konsoli można wpisywać komendy sterujące (np. zmianę zadanej temperatury), które są wysyłane do mikrokontrolera przez UART.

### Wymagane biblioteki

```bash
pip install pyserial matplotlib numpy
```

---

## 📈 Wyniki — przebieg regulacji

Poniżej przykładowy przebieg temperatury (zadanej i rzeczywistej) oraz odpowiadający mu sygnał PWM grzałki, zarejestrowane w czasie rzeczywistym za pomocą `PID.py`/`Projekt.py`.

<img width="1002" height="875" alt="wykresy" src="https://github.com/user-attachments/assets/d63dca60-9db3-4953-b4f7-79c66e2bdde6" />

---

## 📁 Struktura repozytorium

| Plik | Opis |
|---|---|
| `Raport.pdf` | Raport laboratoryjny — cel projektu, schemat elektryczny, wymagania minimalne i dodatkowe. |
| `PID.py` | Wizualizacja danych z regulatora PID w czasie rzeczywistym. |
| `Projekt.py` | Wizualizacja + sterowanie systemem z poziomu konsoli. |
| `images/` | Zdjęcia rzeczywistego układu oraz zarejestrowane wykresy przebiegów. |
