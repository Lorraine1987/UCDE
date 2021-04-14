# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()

# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()

# Import Pandas
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x="Spiders", data=df)

# Display the plot
plt.show()

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x="absences", y="G3",
                data=student_data,
                hue="location")

# Show plot
plt.show()

# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3",
                data=student_data,
                hue="location",
                hue_order=["Rural", "Urban"])

# Show plot
plt.show()

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x="school", data=student_data, hue="location", palette=palette_colors)

# Display plot
plt.show()