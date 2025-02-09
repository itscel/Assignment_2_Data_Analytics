# Assignment_2_Data_Analytics

General Instructions : Use the same font and font size for all graphs.
Instructions:

a. For Bar Graph:

Create a horizontal stacked bar chart
Transform 1 into “Yes” and 0 into “No”
Follow the plot specification for bar plot

b. For Sankey Diagram:

Create a Sankey Diagram that connects ('PS', 'OMP', 'CNP', 'NRP', 'NMCCC', 'PEC', 'NCDM', 'RGS') to the LABELS to ('Reg', 'Aca', 'Oth')
Follow the Path Specifications


C. Network Graph

Create the network graph
D,F,I,N,S should created as a pentagram located at the center of the graph showing connection with each other.
The others should be outside of the the pentagram, still showing connections to other nodes.
The node color should be:

Blue: [D,F,I,N,S], Green: ['BIH', 'GEO', 'ISR', 'MNE', 'SRB', 'CHE', 'TUR', 'UKR', 'GBR', 'AUS', 'HKG', 'USA’], Yellow: ['AUT', 'BEL', 'BGR', 'HRV', 'CZE', 'EST', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LUX', 'NLD', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP']


Finally you are required to collate the separate graph into one single graph for printing, the single graph should be visible when copy pasted in a long bond paper.


# Documentation for Running the Script (Bar Chart, Network Graph, and Sankey Diagram)

## Overview

This Python script processes data from various CSV files to generate:
- A **horizontal stacked bar chart** using **Matplotlib**.
- A **network graph** using **NetworkX**.
- A **Sankey diagram** using **Plotly**.

These visualizations are saved as PNG files in the `images` folder and displayed on the screen.

### Dependencies

Before running the script, make sure the following Python libraries are installed:
- **Pandas**: For data manipulation and reading CSV files.
- **Matplotlib**: For creating the horizontal stacked bar chart and visualizing the network graph.
- **NetworkX**: For creating and plotting the network graph.
- **Plotly**: For generating the Sankey diagram.

To install the dependencies, run the following command:

```bash
pip install pandas matplotlib networkx plotly
```

### Files Needed
- **bar_assignment.csv**: This file is used for generating the horizontal stacked bar chart. It must be placed in the `csv/` directory.
- **networks_assignment.csv**: This file is used for creating the network graph. It should also be placed in the `csv/` directory.
- **sankey_assignment.csv**: This file is used for generating the Sankey diagram. It must be in the `csv/` directory.

### Expected File Structure

Ensure the following file structure:
```
project_directory/
│
├── csv/
│   ├── bar_assignment.csv
│   ├── networks_assignment.csv
│   └── sankey_assignment.csv
│
├── images/
│   └── (empty or contains previous output images)
│
└── graph_code/
    └── (codes here...)
```

### How to Run the Script

1. **Navigate to the project directory**:
   Open a terminal or command prompt and change the directory to the folder where the script is located.

   Example:
   ```bash
   cd /path/to/your/project_directory/script
   ```

2. **Run the Python script**:
   Execute the script by running the following command:

   ```bash
   python filename.py
   ```

3. **Verify the Output**:
   - Check the `images/` folder for the following image files:
     - `bar.png` (horizontal stacked bar chart).
     - `network.png` (network graph).
     - `sankey.png` (Sankey diagram).
   - Each chart will also be displayed in a window.

### Troubleshooting

- **Missing CSV Files**:
   Ensure the CSV files (`bar_assignment.csv`, `networks_assignment.csv`, and `sankey_assignment.csv`) are present in the `csv/` folder. If the folder or files don't exist, create them or adjust the script to match the correct file paths.

- **Missing Dependencies**:
   If you encounter errors related to missing packages (`pandas`, `matplotlib`, `networkx`, or `plotly`), install the required packages by running:
   ```bash
   pip install pandas matplotlib networkx plotly
   ```

- **Image Saving Issues**:
   If the script fails to save images, ensure that the `images/` directory exists and that the script has write permissions to that folder.

ing the `sankey_assignment.csv`.

The images will be saved in the `images/` folder as `bar.png`, `network.png`, and `sankey.png`.
