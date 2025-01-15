from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_transforamtion import DataTransformation
from mlproject import logger


STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open("artifacts/data_validation/status.txt", "r") as f:
                status = f.read().split(" ")[-1]

                if status == "True":
                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(config=data_transformation_config)
                    data_transformation.train_test_spliting()
                else:
                    raise Exception("Your data schema is not valid")
                
        except Exception as e:
            print(e)



if __name__ == '__main__':
    try:
        logger.info(f" <<<<<----- {STAGE_NAME} started ----->>>>> ")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f" ----->>>>> {STAGE_NAME} completed <<<<<----- ")
    except Exception as e:
        logger.exception(e)
        raise e