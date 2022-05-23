from numba import jit
from numba.pycc import CC
from math import radians, sin, cos, asin, sqrt
import pathlib

compile_path = pathlib.Path(__file__).parent.resolve()

cc = CC("compiled_haversine")
cc._source_module = "my_numba_package.haversine"
cc.output_dir = compile_path

@cc.export("fhaversine", "f8(f8,f8,f8,f8)")
def jit_haversine(lon1,lat1,lon2,lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * 6371 * asin(sqrt(a))

if __name__ == "__main__":
    print(compile_path)
    cc.compile()
