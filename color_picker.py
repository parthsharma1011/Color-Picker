import tkinter as tk

class MouseControl:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.bind('<Motion>', self.moved)
        self.canvas.pack()

    def moved(self, event):
        x = event.x
        y = event.y
        x = min(x, len(pixels)-1 )
        x = max(x, 1 )
        y = min(y, 255 )
        y = max(y, 1 )
        self.canvas.create_rectangle( 0, 525, 1400, 780, fill=pixels[x][y])


def main():
    root = tk.Tk()
    window = tk.Canvas(root, width=1400, height=780, bg='white')
    window.grid()

    mxR = 256//7
    for i in range(mxR):
        for j in range(mxR):
            for k in range(256):
                cg = i*7
                cb = ((mxR-j)*7) if (i&1) else (j*7)
                cr = k
                x = i*mxR + j
                y = k
                colorVal = "#%02x%02x%02x" % ( cr, cg, cb )
                window.create_line( x, 2*y, x+1, 2*y+2, fill=colorVal )
                pixels[x][y] = colorVal

    mouse = MouseControl(window)
    window.mainloop()


if __name__ == "__main__":
    pixels = [ [ 'grey' for j in range(256) ] for i in range((256//7)**2) ]
    main()