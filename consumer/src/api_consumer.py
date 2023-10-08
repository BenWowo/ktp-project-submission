import requests, json, csv
from datetime import datetime, timedelta

class api_consumer:
    def __init__(self):
        pass

    def _get_recent_ratings(self, date_ratings: list[list[int]], days: int) -> list[list[int]]: 
        """
        returns list date_ratings of no older than 'days' days

        param date_ratings: date_ratings of a player
        return: filtered list of date_ratings
        """
        recent_ratings = []

        for date_rating in date_ratings:
            year, month, day = date_rating[0], date_rating[1] + 1, date_rating[2]
            date_difference = datetime.now() - datetime(year, month, day)

            if date_difference < timedelta(days=days):
                recent_ratings.append(date_rating)
        
        return recent_ratings

    def _get_interpolated_ratings(self, date_ratings: list[list[int]], days: int) -> list[list[int]]:
        """
        Inserts duplicate rating values on days in between data 
        points separated by more than one day
        
        param date_ratings: list of date_ratings
        return: list of date_ratings with interpolated
        """

        interpolated_ratings = []

        # Create an empty dictionary to store data for each day
        date_dict = {}
        for date_rating in date_ratings:
            year, month, day, rating = date_rating
            date_dict[datetime(year, month + 1, day).date()] = rating

        # also get the latest date value
        prev_rating = date_ratings[-1][3]

        # make backward pass through the data and fill in missing dates
        for i in range(days):
            date = datetime.now().date() - timedelta(days=i)
            year, month, day = date.year, date.month, date.day

            # If you have data for this date, use it; otherwise, fill with placeholder data
            if date in date_dict:
                rating = date_dict[date]
                interpolated_ratings.append([year, month, day, rating])
                prev_rating = rating
            else:
                interpolated_ratings.append([year, month, day, prev_rating])

        interpolated_ratings.reverse()

        return interpolated_ratings

    def _get_top_users(self, num_users: int, game_type: str) -> list[str]:
        top_users = []

        url = f'https://lichess.org/api/player/top/{num_users}/{game_type}'
        response = requests.get(url)

        if response.status_code == 200:
            top_users_json = response.json()

            for user in top_users_json['users']:
                top_users.append(user['username'])

        else:
            print('Request failed with status code: ', response.status_code)
        
        return top_users

    def _get_rating_history(self, username: str, game_type: str) -> list[list[int]]:
        rating_history = []

        url = f'https://lichess.org/api/user/{username}/rating-history'
        response = requests.get(url)

        if response.status_code == 200:
            rating_history_json = response.json()

            for history in rating_history_json:
                # TODO - user validation on game_type
                if history['name'] == game_type:
                    rating_history = history['points']
                    break
        else:
            print("Request failed with status code: ", response.status_code)

        return rating_history

    def consume(self) -> None:
        #TODO - retry api requests and log user warning
        print('This is my debug message to see that it is running')

        top_users = self._get_top_users(num_users=50, game_type='classical')
        print(f'This is the list of top users: {top_users}')

        top_user = top_users[0]
        top_user_rating_history = self._get_rating_history(username=top_user, game_type='Classical')
        recent_ratings = self._get_recent_ratings(top_user_rating_history, days=30)
        interpolated_ratings = self._get_interpolated_ratings(recent_ratings, days=30)
        print(f'These are the recent ratings of top user: {top_user} in the classical game mode ratings: {interpolated_ratings}')

        with open('data.csv', mode='w', newline='') as file:
            for user in top_users:
                # I should do some try catches on these ratings
                rating_history = self._get_rating_history(username=user, game_type='Classical')
                recent_ratings = self._get_recent_ratings(date_ratings=rating_history, days=30)
                interpolated_ratings = self._get_interpolated_ratings(recent_ratings, days=30)
                csv_writer = csv.writer(file)

                # get only the rating value and also append their name to start
                interpolated_ratings = [rating[3] for rating in interpolated_ratings]
                interpolated_ratings.insert(0, user)
                csv_writer.writerow(interpolated_ratings)
        print('The recent rating of the top 50 players have been written to "data.csv" ')


        print('This is the ending debug message')


    