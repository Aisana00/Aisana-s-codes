import json

# Чтение JSON файла
with open('sample_data.json', 'r') as file:
    data = json.load(file)

# Заголовок таблицы
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU'}")
print("-" * 50 + " " + "-" * 20 + "  " + "-" * 6 + "  " + "-" * 5)

# Извлечение данных интерфейсов
interfaces = data.get('imdata', [])

for interface in interfaces:
    # Получаем атрибуты интерфейса
    attributes = interface.get('l1PhysIf', {}).get('attributes', {})
    
    # Извлекаем данные
    dn = attributes.get('dn', '')
    description = attributes.get('descr', '') or ' '
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')
    
    # Вывод данных в формате таблицы
    print(f"{dn:<50} {description:<20} {speed:<8} {mtu}")