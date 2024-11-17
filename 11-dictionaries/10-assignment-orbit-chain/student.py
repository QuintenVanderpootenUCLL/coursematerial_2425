def orbit_chain(orbits, start):
    chain = [start]
    current = start
    while current in orbits:
        chain.append(orbits[current])
        current = orbits[current]
    return chain

orbits = {
        'Moon': 'Earth',
        'Mars': 'Sun',
        'Earth': 'Sun',
        'Jupiter': 'Sun',
        'Saturn': 'Sun',
        'Sun': 'Sagittarius A*',
        'Phobos': 'Mars',
        'Ganymede': 'Jupiter',
        'Callisto': 'Jupiter',
        'Europa': 'Jupiter',
    }

print(orbit_chain(orbits, "Moon"))
print(orbit_chain(orbits, "Phobos"))
print(orbit_chain(orbits, "Earth"))