import os
from textsummarizer.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = True

            all_files = os.listdir(
                os.path.join(
                    "artifacts",
                    "data_ingestion",
                    "samsum_dataset"
                )
            )

            for file in self.config.all_required_files:
                if file not in all_files:
                    validation_status = False
                    break

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e