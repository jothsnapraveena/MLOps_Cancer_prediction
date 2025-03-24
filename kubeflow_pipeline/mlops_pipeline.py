import kfp
from kfp import dsl

# Define a function that generates a pipeline
def data_processing_op():
    return dsl.ContainerOp(
        name='Data Processing',
        image='jothsnapraveena/mlops-cancer:latest',
        command=['python', 'src/data_processing.py'],
        
    )

def model_training_op():
    return dsl.ContainerOp(
        name='Model Training',
        image='jothsnapraveena/mlops-cancer:latest',
        command=['python', 'src/model_training.py'],
        
    )


## Pipeline starts here

@dsl.pipeline(
    name='Cancer Detection Pipeline',
    description='A Kubeflow pipeline for detecting cancer using machine learning'
)
def mlops_pipeline():
    data_processing=data_processing_op()
    model_training=model_training_op().after(data_processing)

### RUN
if __name__=='__main__':
   from kfp.compiler import Compiler
   Compiler().compile(mlops_pipeline, "mlops_pipeline.yaml")
