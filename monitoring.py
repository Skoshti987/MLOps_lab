import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset


def main():
    reference_data = pd.DataFrame({
        "temperature": [25, 26, 27, 25, 28, 26, 27, 25],
        "humidity": [60, 62, 61, 59, 63, 60, 62, 61]
    })

    current_data = pd.DataFrame({
        "temperature": [35, 36, 37, 34, 38, 36, 35, 37],
        "humidity": [40, 42, 41, 39, 43, 40, 42, 41]
    })

    report = Report([
        DataDriftPreset()
    ])

    result = report.run(
        current_data,
        reference_data
    )

    result.save_html("evidently_report.html")
    print("Evidently monitoring completed successfully!")


if __name__ == "__main__":
    main()