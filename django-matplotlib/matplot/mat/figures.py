import matplotlib.pyplot as plt

def my_figure():
    fig, ax = plt.subplots()
    ax.bar([16, 24, 9, 49], [4, 5, 3, 12])
    return fig