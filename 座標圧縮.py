# 座標圧縮 (座圧) https://drken1215.hatenablog.com/entry/2021/08/09/235400

def zaatu(A):
    B = sorted(set(A))
    D = { v: i for i, v in enumerate(B) }
    return(list(map(lambda v: D[v], A)))