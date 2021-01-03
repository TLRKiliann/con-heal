try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        fig = plt.figure()
        fig.set_facecolor("black")
        lab = fig.suptitle('Blood Pressure (TA) by Month',
            fontsize=18)
        lab.set_color('aquamarine')
        ax = plt.subplot()
        ax.tick_params(axis='x', colors='aquamarine')
        #for tick in ax.get_xticklabels():
        #    tick.set_color('black')
        ax.tick_params(axis='y', colors='aquamarine')
        #for tick in ax.get_yticklabels():
        #    tick.set_color('black')
        # with bmh style context :
        #ax.spines['top'].set_color('cyan')
        #ax.spines['left'].set_color('cyan')
        #ax.spines['right'].set_color('cyan')
        #ax.spines['bottom'].set_color('cyan')
        labelc = plt.ylabel("y-label")
        labelc.set_color("aquamarine")
        labelc2 = plt.xlabel("x-label")
        labelc2.set_color("aquamarine")
        #labelc3 = plt.title("Relevé des tensions (TA) par date",
        #   fontsize=18)
        #labelc3.set_color('aquamarine')

        plt.plot(x_axis, y_axis, 'o', color='red')
        plt.plot(x_axis, z_axis, 'o', color='red')
        #plt.ylim(30, 240)
        plt.vlines(x = x_axis, ymin = z_axis, ymax = y_axis,
           colors = 'blue',
           label = 'vline_multiple - full height')

        for x,y in zip(x_axis, y_axis):
            label = "{}".format(y)
            plt.annotate(label, (x,y), textcoords="offset points",
                xytext=(0,10), ha='center')

        for x,z in zip(x_axis, z_axis):
            label2 = "{}".format(z)
            plt.annotate(label2, (x,z), textcoords="offset points",
                xytext=(0,-15), ha='center')
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        plt.ylabel('TA (blood pressure)', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        #plt.title('Relevé des tensions (TA) par date', fontsize=18)
        plt.xticks(rotation=45)
        plt.legend(['TA (blood pressure)'])
        plt.grid(show_grid)
        plt.show()
except ValueError as val:
    print("+ False entry value, ", val)
