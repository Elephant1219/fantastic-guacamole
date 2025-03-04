import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('heart_disease_risk_dataset_earlymed.csv')

# Calculate the frequency of symptoms for each heart risk group
symptoms = ['Chest_Pain', 'Shortness_of_Breath', 'Fatigue', 'Palpitations', 'Dizziness', 'Swelling']
heart_risk_groups = data.groupby('Heart_Risk')[symptoms].mean()

# Create a bar chart
heart_risk_groups.plot(kind='bar', figsize=(12, 6))
plt.title('Symptom Frequency by Heart Risk')
plt.xlabel('Heart Risk')
plt.ylabel('Symptom Frequency')
plt.legend(title='Symptoms')
plt.show()