import requests

BASE_URL = "http://127.0.0.1:8000/api"

# Пример данных для ноутбуков
laptops = [
    {"model": "Dell Inspiron", "processor": "Intel i5", "gpu": "NVIDIA GTX 1050", "screen_size": 15.6, "memory_size": 8},
    {"model": "HP Pavilion", "processor": "AMD Ryzen 5", "gpu": "AMD Radeon Vega", "screen_size": 14.0, "memory_size": 16},
    {"model": "MacBook Air", "processor": "Apple M1", "gpu": "Integrated", "screen_size": 13.3, "memory_size": 8},
    {"model": "Lenovo ThinkPad", "processor": "Intel i7", "gpu": "Intel Iris Plus", "screen_size": 14.0, "memory_size": 16},
    {"model": "Asus ZenBook", "processor": "AMD Ryzen 7", "gpu": "NVIDIA GTX 1650", "screen_size": 15.6, "memory_size": 32},
]

# Пример данных для производителей
manufacturers = [
    {"name": "Dell", "country": "USA", "location": "Round Rock, TX", "warranty": 24},
    {"name": "HP", "country": "USA", "location": "Palo Alto, CA", "warranty": 12},
    {"name": "Apple", "country": "USA", "location": "Cupertino, CA", "warranty": 36},
    {"name": "Lenovo", "country": "China", "location": "Beijing", "warranty": 24},
    {"name": "Asus", "country": "Taiwan", "location": "Taipei", "warranty": 18},
]

# Пример данных для рыночных предложений
market_offers = [
    {"batch_size": 100, "price": 1200.00, "date": "2025-01-01", "laptop_id": 1, "manufacturer_id": 1},
    {"batch_size": 50, "price": 1500.00, "date": "2025-01-02", "laptop_id": 2, "manufacturer_id": 2},
    {"batch_size": 200, "price": 999.99, "date": "2025-01-03", "laptop_id": 3, "manufacturer_id": 3},
    {"batch_size": 75, "price": 1400.00, "date": "2025-01-04", "laptop_id": 4, "manufacturer_id": 4},
    {"batch_size": 150, "price": 1300.00, "date": "2025-01-05", "laptop_id": 5, "manufacturer_id": 5},
]

def populate_laptops():
    for laptop in laptops:
        response = requests.post(f"{BASE_URL}/laptops/", json=laptop)
        print(f"Laptop {laptop['model']} - Status: {response.status_code}")

def populate_manufacturers():
    for manufacturer in manufacturers:
        response = requests.post(f"{BASE_URL}/manufacturers/", json=manufacturer)
        print(f"Manufacturer {manufacturer['name']} - Status: {response.status_code}")

def populate_market_offers():
    for offer in market_offers:
        response = requests.post(f"{BASE_URL}/market_offers/", json=offer)
        print(f"Market Offer (Batch: {offer['batch_size']}) - Status: {response.status_code}")

if __name__ == "__main__":
    populate_laptops()
    populate_manufacturers()
    populate_market_offers()
