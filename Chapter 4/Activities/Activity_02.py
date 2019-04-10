# Activity 2: Calculate Predicted Label

# calculate mode for each row
row_mode = labels_df.mode(axis=1)

# assign the row_mode array as a column in labels_df
labels_df['row_mode'] = row_mode

