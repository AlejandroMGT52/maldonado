from app import sumar

def test_suma_correcta():
    assert sumar(2, 2) == 4  # ❌ intencionalmente incorrecto para fallo inicial
