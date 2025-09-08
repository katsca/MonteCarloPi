# My Matplotlib Project

This project gives visualization of finding $\pi$ using Monte Carlo method. It makes use of **Matplotlib** and **Numpy** in Python.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/my-matplotlib-project.git
   cd my-matplotlib-project
   
2. Create a virtual Environment 
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   
## Usage

Run the main Script
   ```bash
   python main.py --pause 0.01 --num_points 100
   ```
--pause:
   The number of seconds you have to wait between each newly randomly generated point being plotted on the graph
   Default: 0.001

--num_points:
   The number of randomly generated points we will create
   Default: 10000
