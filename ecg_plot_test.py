from scipy.io import loadmat
import ecg_plot

def load_ecg_from_mat(file_path):
    mat = loadmat(file_path)
    data = mat["data"]
    feature = data[0:12]
    return(feature)

test_ecg = load_ecg_from_mat('example_ecg.mat')
ecg_plot.plot_1(test_ecg[1])
ecg_plot.show()
ecg_plot.plot_12(test_ecg)
ecg_plot.show()
ecg_plot.plot_12(test_ecg)
ecg_plot.save_as_png('example_ecg','tmp/')
ecg_plot.plot_12(test_ecg)
ecg_plot.save_as_jpg('example_ecg','tmp/')
ecg_plot.plot_12(test_ecg)
ecg_plot.save_as_svg('example_ecg','tmp/')
ecg_plot.plot_12(test_ecg)
ecg_plot.show_svg()

