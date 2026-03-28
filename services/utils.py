def run_query(con, query):

    try:
        result = con.execute(query).fetchdf()
        return result

    except Exception as e:
        return f"SQL Error: {str(e)}"