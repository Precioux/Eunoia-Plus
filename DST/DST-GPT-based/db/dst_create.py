import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host="localhost",     # Update with your host
    database="main_dst",  # Update with your database name
)

# Create a cursor object
cur = conn.cursor()

# SQL query to create the dst_table with City and Date columns
create_table_query = '''
CREATE TABLE IF NOT EXISTS dst_table (
    City VARCHAR(100),    -- The city referenced in the conversation
    Date DATE             -- The date mentioned in the conversation
);
'''

# Execute the query to create the table
cur.execute(create_table_query)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Table 'dst_table' created successfully!")
