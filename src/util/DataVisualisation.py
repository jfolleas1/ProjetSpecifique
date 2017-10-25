# -----------------------------------------------------------------------------------------
# Aim of the file

# This file function to visualize the curve that show how the variable ratio (filter_size/number_of_item), dim, delta
# change in function of others.

# -----------------------------------------------------------------------------------------
# Import

from matplotlib import pyplot as plt

# -----------------------------------------------------------------------------------------
# Constant

# -----------------------------------------------------------------------------------------
# Code

def visualize_curve( data, x_label, y_label, title, filename=None):
    """
    Allow to visualize curve build with the data in paramters or store it into the file specified.
    :param data: the data that we want to visualize with the following form : [(curve_title, [m/n_ratio], [fp_rate])]
    :param x_label: label of x (string)
    :param y_label: label of y (string)
    :param title: title of the figure (string)
    :param filename: filename for save the figure. (string) if it is not specified, the figure will be plot
    :return:
    """
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    for data_tuple in data:
        if len(data_tuple[1]) == len(data_tuple[2]):
            plt.plot(data_tuple[1], data_tuple[2], label=data_tuple[0])
        else :
            # TODO add log for say ignored data
            pass
    plt.legend()
    if filename:
        plt.savefile(filename)
    else:
        plt.show()

