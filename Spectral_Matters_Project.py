import tkinter as tk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class SpectrumAnalyzer:
    def __init__(self, root):
        # Assigns the Tkinter window to the instance variable
        self.root = root
        self.root.title("Spectrum Analyzer")

        # Initializes an instance variable self.data to store the loaded data
        self.data = None
        self.background_line = None
        # Store the selected interval for intensity calculation
        self.selected_interval = None

        # Calls a method to create GUI widgets and set up the initial layout
        self.create_widgets()

    def create_widgets(self):
        # Set up the menu bar and Matplotlib figure
        self.setup_menu()
        self.setup_matplotlib_figure()

    def setup_menu(self):
        # Create menus for file-related and analysis-related actions
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load Data", command=self.load_data)
        file_menu.add_command(label="Save Figure", command=self.save_figure)

        analysis_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Analysis", menu=analysis_menu)
        analysis_menu.add_command(label="Plot Data", command=self.plot_data)
        analysis_menu.add_command(label="Remove Linear Background", command=self.remove_linear_background)
        analysis_menu.add_command(label="Calculate Intensities", command=self.calculate_intensities)

    def setup_matplotlib_figure(self):
        # Create Matplotlib figure and canvas
        self.fig = Figure(figsize=(6, 4))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def load_data(self):
        # Opens a file dialog to allow the user to select a data file
        file_path = filedialog.askopenfilename(title="Select data file", filetypes=[("Text files", "*.txt")])
        if file_path:
            # Loads the data from the selected file using NumPy's loadtxt function
            self.data = np.loadtxt(file_path)
            # Calls the method to plot the loaded data
            self.plot_data()

    def plot_data(self):
        # Checks if there is loaded data
        if self.data is not None:
            self.ax.clear()
            # Plots the loaded data on the Matplotlib subplot
            self.ax.plot(self.data[:, 0], self.data[:, 1], label='Original Data')
            # Sets the x-axis label
            self.ax.set_xlabel('Measured Kinetic Energy (eV)')
            # Sets the y-axis label
            self.ax.set_ylabel('Intensity')
            # Displays the legend
            self.ax.legend()
            # Redraws the Matplotlib figure on the Tkinter canvas
            self.canvas.draw()

    def remove_linear_background(self):
        # Checks if there is loaded data
        if self.data is not None:
            # Plots an empty line for the linear background
            self.background_line, = self.ax.plot([], [], 'r--', label='Linear Background')
            # Displays the legend
            self.ax.legend()
            # Implement logic to get two points from the user and fit a line
            self.fit_linear_background()
            # Subtract the background line from the loaded data
            self.subtract_background()
            # Calls the method to plot the updated data
            self.plot_data()

    def fit_linear_background(self):
        # Implement logic to get two points from the user and fit a line
        pass

    def subtract_background(self):
        # Subtract the background line from the loaded data
        self.data[:, 1] -= np.interp(self.data[:, 0], self.background_line.get_xdata(), self.background_line.get_ydata())

    def calculate_intensities(self):
        # Checks if there is loaded data
        if self.data is not None:
            # Implement logic to let the user select an interval
            # Use np.trapz to calculate the area under the curve within the selected interval
            result = self.calculate_area_under_curve()
            # Prints the calculated intensity
            print(f"Calculated intensity: {result}")

    def calculate_area_under_curve(self):
        # Use np.trapz to calculate the area under the curve within the selected interval
        return np.trapz(self.data[self.selected_interval[0]:self.selected_interval[1], 1],
                        self.data[self.selected_interval[0]:self.selected_interval[1], 0])

    def save_figure(self):
        # Checks if there is loaded data
        if self.data is not None:
            # Opens a file dialog to let the user specify the file path for saving the figure
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                # Saves the Matplotlib figure as an image file
                self.fig.savefig(file_path)
                # Prints a success message
                print("Figure saved successfully")

# Checks if the script is being run as the main program
if __name__ == "__main__":
    # Creates the main Tkinter window
    root = tk.Tk()
    # Creates an instance of the SpectrumAnalyzer class with the main window as a parameter
    analyzer = SpectrumAnalyzer(root)
    # Enters the Tkinter main loop to start the GUI application
    root.mainloop()
