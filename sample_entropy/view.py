import matplotlib.pyplot as plt
import numpy as np

def view(data, xrange, m_values):
    fig = plt.figure()
    colors = plt.cm.plasma(np.linspace(0, 1, len(m_values)))

    ax1 = fig.add_subplot(311)
    for i, m in enumerate(m_values):
        ax1.plot(xrange, data[0, i, :], label=f"m={m}", color=colors[i])
    ax1.set_ylabel("SampEn")
    ax1.legend()
    ax1.grid()

    ax2 = fig.add_subplot(312)
    for i, m in enumerate(m_values):
        ax2.plot(xrange, data[1, i, :], label=f"m={m}", color=colors[i])
    ax2.set_ylabel("SampEn")
    ax2.legend()
    ax2.grid()

    ax3 = fig.add_subplot(313)
    for i, m in enumerate(m_values):
        ax3.plot(xrange, data[2, i, :], label=f"m={m}", color=colors[i])
    ax3.set_ylabel("SampEn")
    ax3.set_xlabel("r")
    ax3.legend()
    ax3.grid()

    plt.tight_layout()
    plt.show()