import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def visualize_data():
    """Retrieve user activity data and create visualizations."""
    connection = sqlite3.connect('user_activity.db')
    query = 'SELECT action, COUNT(*) as count FROM user_activity GROUP BY action'
    
    # Load data into a pandas DataFrame
    df = pd.read_sql_query(query, connection)
    
    # Create a bar chart for user actions
    plt.figure(figsize=(8, 5))
    plt.bar(df['action'], df['count'], color='skyblue')
    plt.xlabel('User Actions')
    plt.ylabel('Count')
    plt.title('User Actions Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Show the plot
    plt.show()

    connection.close()

if __name__ == "__main__":
    visualize_data()