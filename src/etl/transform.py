def transform_data(df):
    # remove nulls
    df = df.dropna()

    # ensure correct types
    df["temperature"] = df["temperature"].astype(float)
    df["humidity"] = df["humidity"].astype(int)

    # optional: remove duplicates
    df = df.drop_duplicates()

    print(f"Transformed data: {len(df)} rows")
    return df