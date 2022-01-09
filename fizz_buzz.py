def fizz_buzz(start: int, stop: int) -> list[str]:
    fizz_buzz_generator = iter(_FizzBuzzGenerator(start))
    return [next(fizz_buzz_generator) for _ in range(stop - start + 1)]


class _FizzBuzzGenerator:
    
    def __init__(self, start: int, *, fizz_mod: int = 3, buzz_mod: int = 5):
        self._current = start
        self._fizz_mod = fizz_mod
        self._buzz_mod = buzz_mod

    def __iter__(self):
        while True:
            yield self._get_string()
            self._current += 1

    def _get_string(self):
        string = ""
        if self._current % self._fizz_mod == 0:
            string += "Fizz"
        if self._current % self._buzz_mod == 0:
            string += "Buzz"
        return string or str(self._current)

if __name__ == "__main__":
    print(fizz_buzz(4, 14))