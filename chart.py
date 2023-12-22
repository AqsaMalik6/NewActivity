# plot_chart.py
import matplotlib.pyplot as plt
import pandas as pd

csv_filename = "dataset.csv"
df = pd.read_csv(csv_filename)

# Assuming df is the DataFrame from the dataset
plt.scatter(df['Age'], df['Occupation'])  # Assuming 'Occupation' as the y-axis variable
plt.xlabel('Age')
plt.ylabel('Occupation')
plt.title('Scatter Plot: Age vs. Occupation')
plt.show()
