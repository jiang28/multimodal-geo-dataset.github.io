import os
import numpy as np


# Define the value to be converted in mm/hour
mm_hour = 10.0

# Conversion factor from mm/hour to mm/s
mm_hour_to_mm_s = 1 / (60 * 60)

# Conversion factor from mm/s to kg/m2/s
mm_s_to_kg_m2_s = 24 * 60 * 60 / 1000

# Convert mm/hour to kg/m2/s
kg_m2_s = mm_hour * mm_hour_to_mm_s * mm_s_to_kg_m2_s**(-1)

print('kg_m2_s:',kg_m2_s )

# Define a function to convert the numbers in an array to 0 or 1
def convert_numbers(arr):
    return np.where(arr >= kg_m2_s, 1, 0)

# Get the input and output directory paths from user input
#input_dir_path = input("Enter input directory path: ")
#output_dir_path = input("Enter output directory path: ")
input_dir_path = "E:/hrrr/Prep_rate_24h_crop_100_npy"
output_dir_path = "E:/hrrr/hotspot_index"

# Get the list of npy files in the input directory
files = [f for f in os.listdir(input_dir_path) if f.endswith('.npy')]

# Loop through each file and convert its numbers
for f in files:
    data = np.load(os.path.join(input_dir_path, f))
    converted_data = convert_numbers(data)
    output_file_path = os.path.join(output_dir_path, f[:-4] + '.npy')
    np.save(output_file_path, converted_data)

    max_num = np.max(data)

    # Count the number of 1s and 0s in the converted data
    num_ones = np.count_nonzero(converted_data)
    num_zeros = converted_data.size - num_ones
    print(f"File {f} converted: {np.count_nonzero(converted_data)} ones, {converted_data.size - np.count_nonzero(converted_data)} zeros. Max number in original file: {max_num}")
