import pandas as pd
import numpy as np

def load_and_prepare_data(file_path, start_row, end_row):
    """Load and prepare mortality data from Excel file."""
    print("Loading the mortality data from the Excel file...")
    data = pd.read_excel(file_path)
    
    print("Filtering data for Egypt (Country Code: 1125), Year 2019...")
    egypt_2019_data = data.iloc[start_row-1:end_row]
    
    print("Separating data by sex...")
    females_data = egypt_2019_data[egypt_2019_data['Sex'] == 1]
    males_data = egypt_2019_data[egypt_2019_data['Sex'] == 2]
    
    death_cols = [col for col in data.columns if 'Deaths' in col]
    
    print("Extracting all-cause death counts (nDx)...")
    females_ndx = females_data[death_cols].sum().values
    males_ndx = males_data[death_cols].sum().values
    
    return females_ndx, males_ndx

def construct_life_table(nDx, initial_population=100000):
    """
    Construct a life table using death counts (nDx) with proper scaling.
    """
    n = len(nDx)
    age_groups = [f"{5*i}-{5*(i+1)-1}" for i in range(n)]
    
    # Initialize arrays
    lx = np.zeros(n)
    dx = np.zeros(n)
    qx = np.zeros(n)
    Lx = np.zeros(n)
    Tx = np.zeros(n)
    ex = np.zeros(n)
    
    # Scale factor to convert absolute deaths to deaths per 100,000
    scale_factor = initial_population / sum(nDx)
    dx = nDx * scale_factor
    
    # Calculate survival (lx)
    lx[0] = initial_population
    for i in range(1, n):
        lx[i] = lx[i-1] - dx[i-1]
    
    # Calculate probability of dying (qx)
    for i in range(n):
        if lx[i] > 0:
            qx[i] = dx[i] / lx[i]
    
    # Calculate person-years lived (Lx)
    for i in range(n):
        if i == 0:
            Lx[i] = 5 * lx[i] - 2.5 * dx[i]  # Special calculation for first age group
        else:
            Lx[i] = 5 * (lx[i] - dx[i]/2)
    
    # Calculate total person-years lived (Tx)
    for i in range(n-1, -1, -1):
        if i == n-1:
            Tx[i] = Lx[i]
        else:
            Tx[i] = Tx[i+1] + Lx[i]
    
    # Calculate life expectancy (ex)
    for i in range(n):
        if lx[i] > 0:
            ex[i] = Tx[i] / lx[i]
    
    return pd.DataFrame({
        'Age Group': age_groups,
        'lx': lx.round(2),
        'dx': dx.round(2),
        'qx': qx.round(4),
        'Lx': Lx.round(2),
        'Tx': Tx.round(2),
        'ex': ex.round(2)
    })

def main():
    file_path = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/03 nov 20/mortality_data.xlsx'
    start_row = 7684
    end_row = 9479
    
    females_ndx, males_ndx = load_and_prepare_data(file_path, start_row, end_row)
    
    print("\nConstructing life tables...")
    females_life_table = construct_life_table(females_ndx)
    males_life_table = construct_life_table(males_ndx)
    
    print("\n--- Life Table for Egypt 2019 Females ---")
    print(females_life_table)
    print("\n--- Life Table for Egypt 2019 Males ---")
    print(males_life_table)

if __name__ == "__main__":
    main()


















































    import pandas as pd
import numpy as np

def load_and_prepare_data(file_path, start_row, end_row):
    """Load and prepare mortality data from Excel file."""
    print("Loading the mortality data from the Excel file...")
    data = pd.read_excel(file_path)
    
    print("Filtering data for Egypt (Country Code: 1125), Year 2019...")
    egypt_2019_data = data.iloc[start_row-1:end_row]
    
    print("Separating data by sex...")
    females_data = egypt_2019_data[egypt_2019_data['Sex'] == 1]
    males_data = egypt_2019_data[egypt_2019_data['Sex'] == 2]
    
    # Get all death columns
    death_cols = [col for col in data.columns if 'Deaths' in col]
    
    print("Extracting all-cause death counts (nDx)...")
    # Use raw death counts without any adjustments
    females_ndx = females_data[death_cols].sum().values
    males_ndx = males_data[death_cols].sum().values
    
    return females_ndx, males_ndx

def construct_life_table(nDx, initial_population=100000):
    """
    Construct a life table using raw death counts (nDx).
    """
    n = len(nDx)
    age_groups = [f"{5*i}-{5*(i+1)-1}" for i in range(n)]
    
    # Initialize arrays
    lx = np.zeros(n)
    dx = nDx  # Use raw death counts
    qx = np.zeros(n)
    Lx = np.zeros(n)
    Tx = np.zeros(n)
    ex = np.zeros(n)
    
    # Calculate lx (survivors to age x)
    lx[0] = initial_population
    for i in range(1, n):
        lx[i] = lx[i-1] - dx[i-1]
    
    # Calculate qx (probability of dying)
    for i in range(n):
        if lx[i] > 0:
            qx[i] = dx[i] / lx[i]
            if qx[i] > 1:  # Cap at 1 as probability cannot exceed 1
                qx[i] = 1
    
    # Calculate Lx (person-years lived)
    for i in range(n):
        if i == 0:
            # Special calculation for first age group
            Lx[i] = 5 * lx[i] - 2.5 * dx[i]
        else:
            Lx[i] = 5 * (lx[i] - dx[i]/2)
    
    # Calculate Tx (person-years lived beyond age x)
    for i in range(n-1, -1, -1):
        if i == n-1:
            Tx[i] = Lx[i]
        else:
            Tx[i] = Tx[i+1] + Lx[i]
    
    # Calculate ex (life expectancy)
    for i in range(n):
        if lx[i] > 0:
            ex[i] = Tx[i] / lx[i]
    
    return pd.DataFrame({
        'Age Group': age_groups,
        'lx': lx.round(2),
        'dx': dx.round(2),
        'qx': qx.round(4),
        'Lx': Lx.round(2),
        'Tx': Tx.round(2),
        'ex': ex.round(2)
    })

def main():
    file_path = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/03 nov 20/mortality_data.xlsx'
    start_row = 7684
    end_row = 9479
    
    females_ndx, males_ndx = load_and_prepare_data(file_path, start_row, end_row)
    
    print("\nConstructing life tables...")
    females_life_table = construct_life_table(females_ndx)
    males_life_table = construct_life_table(males_ndx)
    
    print("\n--- Life Table for Egypt 2019 Females ---")
    print(females_life_table)
    print("\n--- Life Table for Egypt 2019 Males ---")
    print(males_life_table)

if __name__ == "__main__":
    main()