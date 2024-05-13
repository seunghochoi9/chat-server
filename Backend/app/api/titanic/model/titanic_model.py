
from dataclasses import dataclass


@dataclass
class TitanicModel:
    content: str
    fname: str
    train: object
    test: object
    id: str
    label: str

    @property
    def content(self) -> str: return self.content

    @content.setter
    def content(self, content): self._content = content

    @property
    def fname(self) -> str: return self._fname
    
    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> object: return self._train
    
    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label