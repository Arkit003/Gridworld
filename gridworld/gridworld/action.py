class Action:
    def __init__(self,row,col,n_rows,n_cols) -> None:
        self.up = (row-1,col) if row >0 else None
        self.down = (row+1,col) if row <n_rows else None
        self.left = (row,col-1) if col >0 else None
        self.right = (row,col+1) if col <n_cols else None
