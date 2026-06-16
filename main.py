from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummarizer.logging import logger


# Stage 1
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")

    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()

    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e


# Stage 2
STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")

    data_validation = DataValidationTrainingPipeline()
    data_validation.main()

    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e