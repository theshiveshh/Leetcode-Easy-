class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        def i_row_indices(i: int, r: int) -> Iterator[int]:
            if r == 1: yield from count(i)
            
            yield i            
            for x in count(2 * (r - 1), 2 * (r - 1)):
                yield from (x - i, x + i) if 0 < i < r - 1 else (x + i,)
        
        return ''.join(chain.from_iterable(
            (s[index] for index in takewhile(lambda x: x < len(s), i_row_indices(i, num_rows)))
            for i in range(num_rows)
        ))
