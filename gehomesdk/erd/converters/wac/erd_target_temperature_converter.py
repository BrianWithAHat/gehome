from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.wac import *

class ErdTargetTemperatureConverter(ErdReadWriteConverter[int]):
    def erd_decode(self, value: str) -> int:
        try:
            return erd_decode_int(value)
        except:
            return 86

    def erd_encode(self, value: int) -> str:
        return erd_encode_int(value, 2)
