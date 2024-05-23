import pandas as pd

def generate_df(data):
    df = pd.DataFrame(data)
    expanded_df = df.explode('game_title').explode('game_price')
    return expanded_df