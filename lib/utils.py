from pyspark.sql import SparkSession


def get_spark_session(env):
    if env == "LOCAL":
        return SparkSession.builder \
            .config('spark.driver.extraJavaOptions',
                    '-Dlog4j.configuration=file:log4j.properties -Dspark.yarn.app.container.log.dir=app-logs '
                    '-Dlogfile.name=sbdl-log') \
            .master("local[2]") \
            .enableHiveSupport() \
            .getOrCreate()
    else:
        return SparkSession.builder \
            .enableHiveSupport() \
            .getOrCreate()