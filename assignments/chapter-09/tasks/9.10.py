import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()
frameChartsLT = tk.Frame(root)
frameChartsLT.pack()

stockListExp = ['project', 'quizzes', 'midterm', 'final']
stockSplitExp = [20, 10, 30, 40]

fig = Figure()
ax = fig.add_subplot(111)

ax.pie(stockSplitExp, radius=1, labels=stockListExp,autopct='%0.2f%%', shadow=True,)

chart1 = FigureCanvasTkAgg(fig,frameChartsLT)
chart1.get_tk_widget().pack()

root.mainloop()
