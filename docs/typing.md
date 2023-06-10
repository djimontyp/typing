## Any

:   Спеціальний тип, що вказує на необмежений тип.


## Annotated

:   `Анотація[<тип>, <метадані>]`  

    Спеціальна форма набору тексту для додавання контекстно-специфічних метаданих до анотації.  
    
    *Нове в версії 3.9*
    
    !!! example ""
        ```python
        --8<-- "docs/code/py_types/annotated.py"
        ```
        ```bash
        ❯ annotated.py
        (ValueRange(lo=-10, hi=5), ValueRange(lo=-20, hi=3))
        ```
    
    
## Callable

:   === "Sync"
        `Callable[..., ReturnType]`  
    === "Async"
        `Callable[..., Awaitable[ReturnType]]`  

    *Змінено в версії 3.10: now supports ParamSpec and Concatenate.*

    !!! example ""
        ```python
        --8<-- "docs/code/py_types/paramspec.py"
        ```
    
## ParamSpec

:   Змінна специфікації параметра. Спеціалізована версія типу змінних.
    
    *Нове в версії 3.10*
    
    !!! example ""
        ```python
        --8<-- "docs/code/py_types/paramspec.py"
        ```
    
## ForwardRef

:   `List["SomeClass"]`
    `List[ForwardRef("SomeClass")]`

    Клас, який використовується для внутрішнього представлення типізації посилань на рядки.
    
    *Нове в версії 3.7.4*
    
    
## Final

:   Спеціальна конструкція введення для вказівки кінцевих імен для перевірок типу.
    
    *Нове в версії 3.8*
    
    !!! example ""
        ```python
        --8<-- "docs/code/py_types/final.py"
        ```
    
## Generic

:   Є базовим класом для створення обобщених класів. 
    
    !!! example ""
        ```python
        --8<-- "docs/code/py_types/generic.py"
        ```
    
## Optional

:   Необов’язковий аргумент із значенням за замовчуванням не потребує кваліфікатора Optional в анотації свого типу лише тому, що він є необов’язковим. Наприклад:
    
    !!! example ""
        ```python
        def foo(arg: int = 0) -> None:
            ...
        ```
    З іншого боку, якщо дозволено явне значення None, використання Optional є доречним, незалежно від того, чи є аргумент необов’язковим. Наприклад:
    !!! example ""
        ```python    
        def foo(arg: Optional[int] = None) -> None:
            ...
        ```


## Union

:   Є базовим класом для створення обобщених класів. 
    
    !!! example ""
        ```python
        --8<-- "docs/code/py_types/generic.py"
        ```
    
## TypeAlias

:   Спеціальна анотація для явного оголошення псевдоніма типу.
    
    !!! example ""
        ```python
        Symbol: TypeAlias = str
        Atom: TypeAlias = float | int | Symbol
        Expression: TypeAlias = Atom | list
        ```
    
## Literal

:   Спеціальна форма введення для визначення «літеральних типів».
    
    !!! example ""
        ```python
        def validate_simple(data: Any) -> Literal[True]:  # always returns True
            ...

        Mode: TypeAlias = Literal['r', 'rb', 'w', 'wb']
        def open_helper(file: str, mode: Mode) -> str:
            ...

        open_helper('/some/path', 'r')      # Passes type check
        open_helper('/other/path', 'typo')  # Error in type checker
        ```