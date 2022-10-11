def tree_by_levels(node):
    p, q = [], [node]
    while q:
        v = q.pop(0)
        if v is not None:
            p.append(v.value)
            q += [v.left,v.right]
    return p if not node is None else []
