

from dataclasses import dataclass


@dataclass
class CrimeModel:
    _dname : str = ''
    _sname : str = ''
    _crime : str = ''
    _cctv : str = ''

    @property
    def dname(self) -> str: return self._dname

    @dname.setter
    def dname(self, dname): self._dname = dname

    @property
    def sname(self) -> str: return self._sname

    @sname.setter
    def sname(self, sname): self._sname = sname

    @property
    def crime(self) -> str: return self._crime

    @crime.setter
    def crime(self, crime): self._crime = crime

    @property
    def cctv(self) -> str: return self._cctv

    @cctv.setter
    def cctv(self, cctv): self._cctv = cctv



