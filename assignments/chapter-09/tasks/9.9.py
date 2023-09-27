import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data1 = {'types': ['project', 'quizzes', 'midterm', 'final'],
         'result_in_%': [20, 10, 30, 40]
         }
df1 = pd.DataFrame(data1)


root = tk.Tk()

figure1 = plt.Figure(figsize=(6, 5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['types', 'result_in_%']].groupby('types').sum()
df1.plot(kind='bar', legend=True, ax=ax1)

root.mainloop()
