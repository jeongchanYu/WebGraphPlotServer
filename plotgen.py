def clear_plot_file(filename):
    with open(filename, 'w') as f:
        pass

def write_plot_file(filename, index, value):
    with open(filename, 'a') as f:
        f.write("{{x:{}, y:{}}},".format(index, value))