from my_numba_package.haversine import jit_haversine

def test_haversine():
    assert(jit_haversine(1,2,3,4)==314.2832550736839)
    assert(type(jit_haversine(1,2,3,4)==float))
