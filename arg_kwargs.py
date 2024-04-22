

def find_id(*args, **kwargs):
    for person, atributes in kwargs.items():
        equal = True
        for arg in args:
            if arg not in atributes.values():
                equal = False
                break
        if equal:
            return person
    return 'Not in database'

database0 = {
    "person0": {
        "primer_nombre": "Menem",
        "segundo_nombre": "Heroe",
        "primer_apellido": "Nacional",
        "segundo_apellido": "Intergalactico"
    },
    "person1": {
        "primer_nombre": "Armando",
        "segundo_nombre": "esteban",
        "primer_apellido": "quito",
        "segundo_apellido": "roble"
    },
    "person2": {
        "primer_nombre": "Messi",
        "segundo_nombre": "Dios",
        "primer_apellido": "Todo",
        "segundo_apellido": "Poderoso"
    },
    "person3": {
        "primer_nombre": "Fran",
        "segundo_nombre": "Ariel",
        "primer_apellido": "Martinez",
        "segundo_apellido": "Escaala"
    }
}

ID = find_id("Fran", "Ariel", "Martinez", "Escala", **database0)
print('Person in data base | person_id:', ID)


