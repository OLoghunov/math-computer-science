import matplotlib.pyplot as plt


def view(data, xrange):
    fig = plt.figure()
    ax1 = fig.add_subplot(311)
    ax1.plot(xrange, data[0])
    ax1.set_ylabel("SampEn")
    
    ax2 = fig.add_subplot(312)
    ax2.plot(xrange, data[1])
    ax2.set_ylabel("SampEn")

    ax3 = fig.add_subplot(313)
    ax3.plot(xrange, data[2])
    ax3.set_ylabel("SampEn")
    ax3.set_xlabel("r")

    plt.tight_layout()
    plt.show()
