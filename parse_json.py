import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'sample-data.json')
with open(file_path) as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print(f"{'-'*50} {'-'*20} {'-'*8} {'-'*6}")

for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    
    dn = attributes['dn']
    descr = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    
    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")