rivers = {
    'nile': 'egypt',
    'Yangtze River': 'china',
    'amazon': 'brazil',
}

for river, nation in rivers.items():
    print(f"{river} runs through {nation}")

for river in sorted(rivers.keys()):
    print(river)

for nation in set(rivers.values()):
    print(nation)
