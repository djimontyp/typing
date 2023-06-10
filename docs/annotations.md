На етапі імпорту Python читає анотації типів у функціях, класах і модулях і зберігає їх в атрибутах __annotations__.

!!! example "Анотована сигнатура функції кліпу"
    ```python
    def clip(text: str, max_len: int = 80) -> str: ...
    ```
    ```bash
        >>> from clip_annot import clip
        >>> clip.__annotations__
        {'text': <class 'str'>, 'max_len': <class 'int'>, 'return':
        <class 'str'>}
    ```