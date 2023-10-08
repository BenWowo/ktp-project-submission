from pocketbase import PocketBase
import pandas as pd
import datetime

class db_writer:
    def __init__(self):
        pass

    # authenticate as regular user
    # user_data = client.collection("users").auth_with_password(
    #     "user@example.com", "0123456789")

    # list and filter "example" collection records
    # result = client.collection("example").get_list(
    #     1, 20, {"filter": 'status = true && created > "2022-08-01 10:00:00"'})

    def write_csv(self, filename: str) -> None:
        """
        writes data collected in csv file to
        pocketbase database
        """
        print('does this happen?')
        client = PocketBase('http://localhost:8080')

        df = pd.read_csv(filename)
        print('This is the dataframe')
        print(df)

        for row in df.itertuples():
            print('This is type of row', type(row))
            print('this is a row', row)
            username = row[:1]
            ratings = row[1:]

            client.collection("users").create({
                "username": username
            })

            for rating in ratings:
                pass
            # client.collection("ratings").create({
            #     "date": dateTime.now - datetime
            #     "rating": rating
            # })



        
