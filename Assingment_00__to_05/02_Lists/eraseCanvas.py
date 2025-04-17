import tkinter as tk

CANVAS_WIDTH = 400

CANVAS_HEIGHT = 400
CELL_SIZE = 40

def create_grid(canvas):
    cells = []
    
    
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        
        row_cells = []
        
        for column in range(0, CANVAS_WIDTH, CELL_SIZE):
            
            rect = canvas.create_rectangle(column, row, column + CELL_SIZE, row + CELL_SIZE, fill="white", outline="blue")
            
            row_cells.append(rect)
            
        cells.append(row_cells)
        
        
    return cells

def erase_grid(event):
    
    x, y = event.x, event.y
    
    row = y // CELL_SIZE
    column = x // CELL_SIZE
    
    if 0 <= row < len(grid) and 0 <= column < len(grid[0]):
        canvas.itemconfig(grid[row][column], fill="black")

def main():
    
    global canvas, grid
    
    root = tk.Tk()
    root.title("Grid Canvas")
    
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.bind("<B1-Motion>", erase_grid)
    canvas.pack()
    
    grid = create_grid(canvas)
    
    root.mainloop()



if __name__ == "__main__":
    main()