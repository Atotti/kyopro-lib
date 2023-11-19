class SegmentTree:
    """
        Parms:
            size: int
                配列のサイズ
            op: function
                二項演算
            e: int
                単位限
    """
    def __init__(self, size, op, e):
        self.e = e
        self.op = op
        self.n = 1
        while self.n < size:
            self.n = self.n * 2
        self.a = [self.e for _ in range(2*self.n + 1)]

    def update(self, i, x) -> None:
        index = self.n + i
        self.a[index] = x
        index = index // 2
        while index > 0:
            self.a[index] = self.op(self.a[index*2], self.a[index*2 + 1])
            index = index // 2

    def find(self, l, r) -> int:
        return self._find(l, r, 1, 0, self.n)

    def _find(self, l, r, i, a, b) -> int:
        # 見ている区間が完全にクエリから外れている時
        if r <= a or b <= l:
            return self.e
        # 見ている区間が完全にクエリに含まれている時
        if l <= a and b <= r:
            return self.a[i]
        # 今見ている区間の一部がクエリに含まれている時
        left_value = self._find(l, r, i*2, a, (a + b) // 2)
        right_value = self._find(l, r, i*2 +1, (a+b)//2, b)
        return self.op(left_value, right_value)
    
    def debug_print(self):
        print(self.a)

if __name__=="__main__":
    n, q = map(int,input().split())
    segtree = SegmentTree(n, min, 2**31)
    for i in range(q):
        com, x, y = map(int,input().split())
        if com == 0:
            segtree.update(x, y)
        else:
            ans = segtree.find(x, y+1)
            print(ans)
