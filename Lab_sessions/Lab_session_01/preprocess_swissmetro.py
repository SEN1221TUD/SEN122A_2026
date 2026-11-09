from pathlib import Path
import pandas as pd


def process_swissmetro_data() -> pd.DataFrame:
    """
    Pandas implementation of the Swissmetro preprocessing following Biogeme requirements.
    """
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / 'data' / 'swissmetro.dat'
    output_dir = base_dir / 'data'

    # Read raw file
    df = pd.read_csv(input_path, sep='\t')

    # Exclude trips other than commuter (1) and business (3)
    df = df[df['PURPOSE'].isin([1, 3])].copy()

    # Transform Availability (SP restricted)
    df['TRAIN_AV_SP'] = (df['TRAIN_AV'] * (df['SP'] != 0)).astype(int)
    df['CAR_AV_SP']   = (df['CAR_AV'] * (df['SP'] != 0)).astype(int)

    # Transform Cost with GA discount and scale by 100
    df['TRAIN_COST_SCALED'] = (df['TRAIN_CO'] * (df['GA'] == 0)) / 100.0
    df['SM_COST_SCALED']    = (df['SM_CO'] * (df['GA'] == 0)) / 100.0
    df['CAR_CO_SCALED']     = df['CAR_CO'] / 100.0

    # Transform Travel Time scaled by 100
    df['TRAIN_TT_SCALED']   = df['TRAIN_TT'] / 100.0
    df['SM_TT_SCALED']      = df['SM_TT'] / 100.0
    df['CAR_TT_SCALED']     = df['CAR_TT'] / 100.0

    FINAL_COLUMNS = [
        'ID', 'CHOICE', 'TRAIN_AV_SP', 'SM_AV', 'CAR_AV_SP',
        'TRAIN_TT_SCALED', 'TRAIN_COST_SCALED', 'TRAIN_HE',
        'SM_TT_SCALED', 'SM_COST_SCALED', 'SM_HE',
        'CAR_TT_SCALED', 'CAR_CO_SCALED',
        'PURPOSE', 'FIRST', 'TICKET', 'WHO', 'LUGGAGE',
        'AGE', 'MALE', 'INCOME', 'GA', 'ORIGIN', 'DEST'
    ]

    df_final = df[FINAL_COLUMNS].copy()

    # Rename availability columns
    df_final.rename(columns={'TRAIN_AV_SP': 'TRAIN_AV', 'CAR_AV_SP': 'CAR_AV'}, inplace=True)
    df_final = df_final[df_final['AGE'].isin([1, 2, 3, 4, 5])].copy()
    csv_path = output_dir / 'swissmetro.csv'
    df_final.to_csv(csv_path, index=False)
    return df_final


if __name__ == '__main__':
    df = process_swissmetro_data()
