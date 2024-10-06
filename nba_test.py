import pandas as pd 
import backend

def getPrediction(playerInput, teamInput):
    #Things you need: Player & Team IDs
    from nba_api.stats.endpoints import cumestatsplayer

    from nba_api.stats.static import players
    player_dict = players.get_players()
    print("Number of players fetched: {}".format(len(player_dict)))
    # Use ternary operator or write function 
    player = [player for player in player_dict if player['full_name'] == playerInput][0]


    from nba_api.stats.endpoints import leaguegamefinder

    # Query for games where the Player was playing
    gamefinder = leaguegamefinder.LeagueGameFinder(player_id_nullable=player_id)
    # The first DataFrame of those returned is what we want.
    games = gamefinder.get_data_frames()[0]
    print(games.head())
    # Subset the games to when the last 4 digits of SEASON_ID were 2023.
    games_2324 = games[games.SEASON_ID.str[-4:] == '2023']
    print(games_2324.head())

    from nba_api.stats.static import teams

    team_dict = teams.get_teams()
    print("Number of teams fetched: {}".format(len(team_dict)))
    # Select the dictionary for the Celtics, which contains their team ID

    team = [team for team in team_dict if team['abbreviation'] == teamInput][0]


    team_id = team['id']

    teamgamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    # The first DataFrame of those returned is what we want.
    teamgames = teamgamefinder.get_data_frames()[0]
    print(teamgames.head())

    # Subset the games to when the last 4 digits of SEASON_ID were 2017.
    team_games_2324 = teamgames[teamgames.SEASON_ID.str[-4:] == '2023']
    dropped_team_games = team_games_2324.drop(columns=['PTS'])
    print(dropped_team_games.head())

    combined = pd.merge(dropped_team_games, games_2324, on=['SEASON_ID', 'GAME_ID', 'GAME_DATE', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'MATCHUP', 'WL'])
    combined_dropped = combined.drop(columns=['SEASON_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'MATCHUP', 'MIN_x', 'FGM_x', 'FGA_x', 'FG_PCT_x', 'FG3M_x', 'FG3A_x', 'FG3_PCT_x', 'FTM_x','FTA_x','FT_PCT_x','OREB_x','DREB_x', 'REB_x', 'AST_x', 'STL_x','BLK_x','TOV_x','PF_x','PLUS_MINUS_y','MIN_y', 'FGM_y', 'FGA_y', 'FG3M_y', 'FG3A_y', 'FTM_y', 'FTA_y', 'DREB_y', 'AST_y', 'BLK_y', 'PF_y'])
    combined_dropped['WL'] = combined_dropped['WL'].apply(lambda x: 1 if x == 'W' else 0)
    return predict(combined_dropped)
