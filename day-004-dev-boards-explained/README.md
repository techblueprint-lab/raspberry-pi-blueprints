# Day 004 — Arduino vs. ESP32 vs. Raspberry Pi (Stop Buying the Wrong Board!)

Beginners waste money and weeks of debugging by buying a **\$60 Raspberry Pi** to blink a relay, or trying to run **OpenCV/AI** on an **Arduino Uno** with `2 KB` of RAM. Here is the clean, practical cheat sheet for picking the right board in 10 seconds.

## Side-by-Side Specs

| Spec | Arduino Uno | ESP32 | Raspberry Pi 5 |
| :--- | :---: | :---: | :---: |
| **Price (USD)** | **~$4.50** | **~$5.00** | **~$60.00** |
| **CPU** | 16 MHz (8-bit, 1 core) | 240 MHz (32-bit, 2 cores) | 2.4 GHz (64-bit, 4 cores) |
| **RAM** | **2 KB** | **520 KB** | **4 GB – 8 GB** |
| **Wi-Fi / Bluetooth** | None | **Built-in Wi-Fi + BLE** | **Wi-Fi + BT + Gigabit Eth** |
| **OS** | None (Bare Metal) | FreeRTOS / Arduino / MicroPython | **Full Linux OS** |
| **Power Draw** | ~45 mA | ~80 mA *(10 µA deep sleep!)* | 1,200–3,000 mA *(Wall power)* |

## 3-Second Decision Rule
1. **Need Full Linux, Cameras, HDMI, Docker, or Python ML/OpenCV?** → **Raspberry Pi 5** (`$60`)
2. **Need Wi-Fi, Bluetooth, or Battery-Powered IoT on a budget?** → **ESP32** (`$5` — 15× faster than Uno!)
3. **Learning 5V electronics, simple sensors, and rock-solid instant-boot relays?** → **Arduino Uno** (`$4.50`)

## Run the Interactive Comparison CLI

```bash
python board_picker.py
```
