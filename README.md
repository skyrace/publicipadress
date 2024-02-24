# public ip adress
A sleek, dark-themed Public IP Information Widget using Python and Tkinter. Displays real-time public IP, country, and ISP. Features automatic hourly updates, lightweight design, and user-friendly interface. Ideal for quick internet connectivity insights.
# Public IP Information Widget
# Overview
This Public IP Information Widget is a sleek and user-friendly graphical interface application designed to display real-time information about your current public IP address, the country of origin, and your Internet Service Provider (ISP). Built with Python and Tkinter, it offers a dark-themed, professional appearance that is both modern and easy on the eyes, making it an excellent addition to any desktop environment.

# Features
Real-Time IP Information: Fetches and displays your public IP address, the country you are in, and your ISP, providing a quick glance at your internet connectivity details.
Dark Theme UI: Comes with a professional and modern dark-themed user interface that enhances readability and user experience, especially in low-light conditions.
Automatic Updates: The widget automatically refreshes the displayed information every hour, ensuring that you always have the latest data at your fingertips.
Easy to Use: Simple and straightforward functionality, perfect for users of all technical levels.
Lightweight and Efficient: Designed to be resource-efficient, ensuring minimal impact on your system's performance.
Installation
The widget is easy to install. Simply download the executable from the GitHub repository and run it on your system. There are no complex dependencies or setups required, making it accessible for everyone.

# Usage
Upon launching, the widget will immediately fetch and display your current public IP information. The interface is designed to be non-intrusive, providing essential information at a glance without overwhelming the user with unnecessary details.

# Getting Started
Pre-Compiled Executable
In the dist directory, you'll find a pre-compiled executable of the IP Widget program, ready for immediate use. This executable is built for Ubuntu and allows for quick setup without the need for manual compilation.

# To use the pre-compiled executable:

# Navigate to the dist directory.
Make the executable file runnable with the command: chmod +x ip_widget
Execute the program by double-clicking on it or running ./ip_widget from the terminal.
Compiling From Source
For those who prefer to compile the IP Widget themselves or are looking to modify and rebuild the application, follow these steps:

#Prerequisites
Ensure Python 3 and pip are installed on your system.
Install necessary Python packages: requests and tkinter (usually comes with Python 3).
Steps to Compile
Clone the repository or download the source code.
Navigate to the root directory of the source code.
Install PyInstaller: pip install pyinstaller
Compile the program: pyinstaller --onefile --windowed ip_widget.py
--onefile creates a single executable.
--windowed prevents a terminal window from opening alongside the application (optional for GUI applications).
After compiling, the dist directory will contain the newly created executable, which you can run as described above.

#Adding to Startup
If you wish to have the IP Widget automatically start upon logging into your Ubuntu desktop, please refer to the instructions provided in the text file named startup-instructions.txt within this repository. These instructions guide you through setting up the application to run at startup either via the "Startup Applications" GUI or by creating a .desktop file in ~/.config/autostart.

#Conclusion
IP Widget provides a simple yet effective way to keep track of your public IP and connection details. Whether using the pre-compiled executable for convenience or compiling the source code for customization, IP Widget is a versatile tool for any Ubuntu user.

If the standard method through "Startup Applications" does not work on your Ubuntu machine, another approach involves using the .config/autostart directory in your home folder. This method manually adds applications to startup by creating .desktop files. Here's how to do it:

# Creating a .desktop File for Your Application
Open a terminal and create a new .desktop file in the autostart folder:
bash

nano ~/.config/autostart/ipwidget.desktop
Insert the following content into the file, replacing /path/to/your/executable with the absolute path to your executable:
ini

[Desktop Entry]
Type=Application
Name=IP Widget
Exec=/path/to/your/executable
X-GNOME-Autostart-enabled=true
Save and close the file. If you're using nano, do this with Ctrl+O, Enter then Ctrl+X.
Explanation of Fields:
Type=Application indicates it's an application.
Name=IP Widget is the name of your application as it will appear in startup management tools.
Exec=/path/to/your/executable should point to your widget's executable.
X-GNOME-Autostart-enabled=true ensures the application is enabled at startup.

# Testing the Setup
After creating and configuring your .desktop file, restart your computer to test if the application launches correctly at startup.

This method should work on most Linux distributions that use GNOME or compatible desktop environments. If your system uses a different desktop environment, autostart support may vary.
