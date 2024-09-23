import psycopg2


# Function to create the ask_weather_train table
def create_ask_weather_train_table(conn):
    """Function to create the ask_weather_train table in PostgreSQL."""

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS ask_weather_train (
        CID SERIAL PRIMARY KEY,      -- Conversation ID, automatically incremented
        Conversation INTEGER,                -- The turn number within the conversation
        Speaker VARCHAR(100),        -- Name or identifier of the speaker
        Text TEXT,                   -- The actual text spoken or written
        City VARCHAR(100),           -- The city referenced in the conversation
        Date DATE,                   -- The date mentioned or associated with the conversation
        Status VARCHAR(50)           -- The status of the conversation or turn (e.g., ongoing, completed)
    );
    '''

    with conn.cursor() as cur:
        # Execute the query to create the table
        cur.execute(create_table_query)
        conn.commit()  # Commit the transaction
        print("Table 'ask_weather_train' created successfully!")


# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host="localhost",  # Update with your host
    database="main_dst",  # Update with your database name
)

# # Call the function to create the table
# create_ask_weather_train_table(conn)


# Example function to insert data into the table
def add_to_ask_weather_train(conn, conversation_id, turn, speaker, text, city, date, status):
    """Function to insert a record into the ask_weather_train table."""

    insert_query = '''
    INSERT INTO ask_weather_train (CID, Turn, Speaker, Text, City, Date, Status)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    '''

    values = (conversation_id, turn, speaker, text, city, date, status)

    with conn.cursor() as cur:
        # Print the query and values for debugging
        print(cur.mogrify(insert_query, values).decode('utf-8'))

        # Execute the insert query
        cur.execute(insert_query, values)
        conn.commit()  # Commit after each insert


# # Example usage: Insert a record into the table
# add_to_ask_weather_train(
#     conn=conn,
#     conversation_id=1,
#     turn=1,
#     speaker="John",
#     text="Hello, I need weather information for New York.",
#     city="New York",
#     date="2023-09-12",
#     status="ongoing"
# )

# Close the connection after use
conn.close()

print("Operation completed successfully!")
