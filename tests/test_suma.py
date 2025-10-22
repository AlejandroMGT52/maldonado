from app import sumar

def test_suma_correcta():
    assert sumar(2, 2) == 5 # ❌ intencionalmente incorrecto para fallo inicial
