from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from mlproject.pipeline.stage_02_data_validation import DataValidtationTrainingPipeline
from mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlproject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlproject.pipeline.stage_05_model_evalution import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f" <<<<<----- {STAGE_NAME} started ----->>>>> ")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f" ----->>>>> {STAGE_NAME} completed <<<<<----- ")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f" <<<<<----- {STAGE_NAME} started ----->>>>> ")
    data_validation = DataValidtationTrainingPipeline()
    data_validation.main()
    logger.info(f" ----->>>>> {STAGE_NAME} completed <<<<<----- ")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f" <<<<<----- {STAGE_NAME} started ----->>>>> ")
    data_validation = DataTransformationTrainingPipeline()
    data_validation.main()
    logger.info(f" ----->>>>> {STAGE_NAME} completed <<<<<----- ")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f" <<<<<----- {STAGE_NAME} started ----->>>>> ")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f" ----->>>>> {STAGE_NAME} completed <<<<<----- ")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f" <<<<<----- {STAGE_NAME} started ----->>>>> ")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f" ----->>>>> {STAGE_NAME} completed <<<<<----- ")
except Exception as e:
    logger.exception(e)
    raise e