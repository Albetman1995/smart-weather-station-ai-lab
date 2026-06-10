"""Check that the initial data analysis environment is working."""

import matplotlib
import numpy as np
import pandas as pd


def main() -> None:
    """Print installed package versions and run a small calculation."""
    temperatures = np.array([18.5, 19.2, 20.1, 21.0, 20.4])

    dataframe = pd.DataFrame(
        {
            "temperature_c": temperatures,
        }
    )

    print("Environment is working.")
    print(f"NumPy version: {np.__version__}")
    print(f"pandas version: {pd.__version__}")
    print(f"matplotlib version: {matplotlib.__version__}")
    print(f"Average temperature: {dataframe['temperature_c'].mean():.2f} °C")


if __name__ == "__main__":
    main()