import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('data/patient_data.csv')

# Display first rows
print(df.head())

# Disease count
disease_count = df['Disease'].value_counts()
print(disease_count)

# Plot graph
disease_count.plot(kind='bar')
plt.title('Disease Distribution')
plt.xlabel('Disease')
plt.ylabel('Count')
plt.show()
