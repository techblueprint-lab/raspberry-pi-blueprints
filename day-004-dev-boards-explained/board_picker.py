"""
TechBlueprint (@techblueprint-lab) — Day 004: Arduino vs. ESP32 vs. Raspberry Pi
Interactive Dev-Board Selector & Spec Comparison CLI
"""

BOARDS = {
    "arduino_uno": {
        "name": "Arduino Uno (ATmega328P)",
        "price_usd": "$4.50",
        "cpu": "16 MHz (8-bit, single core)",
        "ram": "2 KB",
        "wireless": "None (external module needed)",
        "os": "None (Bare-metal C++)",
        "power_ma": "~45 mA (very low)",
        "best_for": [
            "Learning electronics & 5V sensors safely",
            "Simple relays, motors, LEDs & deterministic timing",
            "Instant boot (< 1 sec) & bulletproof reliability",
        ],
    },
    "esp32": {
        "name": "ESP32 (Dual-Core Xtensa)",
        "price_usd": "$5.00",
        "cpu": "240 MHz (32-bit, dual core)",
        "ram": "520 KB",
        "wireless": "Built-in Wi-Fi + Bluetooth (BLE)",
        "os": "FreeRTOS / Arduino C++ / MicroPython",
        "power_ma": "~80 mA active (10 µA deep sleep!)",
        "best_for": [
            "Battery-powered Wi-Fi / Bluetooth IoT sensors",
            "Smart home devices & web dashboards for ~$5",
            "15x faster than Arduino Uno at nearly the same price",
        ],
    },
    "raspberry_pi": {
        "name": "Raspberry Pi 5 (ARM Cortex-A76)",
        "price_usd": "$60.00",
        "cpu": "2.4 GHz (64-bit, quad core)",
        "ram": "4 GB / 8 GB",
        "wireless": "Dual-band Wi-Fi + Bluetooth + Gigabit Ethernet",
        "os": "Full Linux (Raspberry Pi OS / Ubuntu)",
        "power_ma": "~1,200–3,000 mA (needs wall power)",
        "best_for": [
            "Running Python ML models, OpenCV cameras & Edge AI",
            "Home servers, Docker containers & web apps",
            "Projects needing HDMI displays, USB webcams & full Linux",
        ],
    },
}


def recommend_board(needs_linux_or_ai: bool, needs_wifi_or_battery: bool) -> str:
    if needs_linux_or_ai:
        return "raspberry_pi"
    if needs_wifi_or_battery:
        return "esp32"
    return "arduino_uno"


def print_comparison():
    print("\n=== TECHBLUEPRINT DEV-BOARD COMPARISON ===\n")
    print(f"{'Spec':<12} | {'Arduino Uno':<24} | {'ESP32':<26} | {'Raspberry Pi 5'}")
    print("-" * 98)
    rows = [
        ("Price", "price_usd"),
        ("CPU", "cpu"),
        ("RAM", "ram"),
        ("Wireless", "wireless"),
        ("OS", "os"),
        ("Power", "power_ma"),
    ]
    for label, key in rows:
        print(
            f"{label:<12} | {BOARDS['arduino_uno'][key]:<24} | "
            f"{BOARDS['esp32'][key]:<26} | {BOARDS['raspberry_pi'][key]}"
        )


def main():
    print_comparison()
    print("\n--- Quick Decision Rules ---")
    scenarios = [
        ("Running OpenCV + YOLO / Python ML server", True, True),
        ("Battery-powered Wi-Fi temperature alert sensor", False, True),
        ("Simple 5V relay & ultrasonic sensor beginner build", False, False),
    ]
    for desc, ai, wifi in scenarios:
        pick = BOARDS[recommend_board(ai, wifi)]["name"]
        print(f"  • {desc}\n      -> Best Pick: {pick}")


if __name__ == "__main__":
    main()
