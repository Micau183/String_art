 lines_x = []
    lines_y = []
    for i, j in zip(pattern, pattern[1:]):
        lines_x.append((i[0], j[0]))
        lines_y.append((i[1], j[1]))

    xmin = 0.
    ymin = 0.
    xmax = generator.data.shape[0]
    ymax = generator.data.shape[1]

    plt.ion()
    plt.figure(figsize=(6, 6))
    plt.axis('off')
    axes = plt.gca()
    axes.set_xlim([xmin, xmax])
    axes.set_ylim([ymin, ymax])
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    axes.set_aspect('equal')
    plt.draw()

    batchsize = 10
    for i in range(0, len(lines_x), batchsize):
        plt.plot(lines_x[i:i+batchsize], lines_y[i:i+batchsize],
                 linewidth=0.1, color='k')
        plt.draw()
        plt.pause(0.000001)
